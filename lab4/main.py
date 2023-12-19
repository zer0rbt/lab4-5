import random
from typing import Type, List, Tuple
import numpy as np
import struct
from copy import deepcopy

class Gene:
    def __init__(self, bounds: Tuple[float, float], mutation_p: int, func: str):
        # Конструктор класса Gene, инициализирующий ген с заданными границами, процентом мутации и функцией
        self.mutation_percentage: int = mutation_p
        self.func: str = func
        self.bounds: Tuple[float, float] = bounds
        self.x: float = random.uniform(self.bounds[0], self.bounds[1])
        self.y: float = random.uniform(self.bounds[0], self.bounds[1])

    def __float__(self):
        # Преобразование гена в число, вычисляемое по заданной функции
        x = self.x
        y = self.y
        x1 = x
        x2 = y
        return float(eval(self.func))

    def set_coords(self, coord: Tuple[float, float]) -> None:
        # Установка координат гена
        self.x, self.y = coord

    def mutate(self) -> None:
        # Мутация гена - добавление случайной величины к координатам с учетом процента мутации
        mutation = random.uniform(-1, 1) * (self.bounds[1] - self.bounds[0]) * (self.mutation_percentage / 100.0)
        self.x += mutation
        self.y += mutation
        self.x = max(min(self.x, self.bounds[1]), self.bounds[0])  # Ограничение координат гена границами
        self.y = max(min(self.y, self.bounds[1]), self.bounds[0])

    def decoded(self, chromosomes: tuple[str, str] = tuple()) -> Tuple[float, float]:
        # Декодирование гена из бинарной строки в координаты
        if not chromosomes:
            return self.x, self.y
        out: list[float] = []
        for binary_string in chromosomes:
            bytes_list = [binary_string[i:i + 8] for i in range(0, len(binary_string), 8)]
            byte_object = bytes([int(byte, 2) for byte in bytes_list])
            out.append(struct.unpack('!f', byte_object)[0])
        if np.nan not in out:
            self.set_coords(tuple(out))
        return tuple(out)

    def encoded(self) -> Tuple[str, str]:
        # Кодирование координат гена в бинарные строки
        x_bytes = struct.pack('!f', self.x)
        y_bytes = struct.pack('!f', self.y)
        x_binary = ''.join(format(byte, '08b') for byte in x_bytes)
        y_binary = ''.join(format(byte, '08b') for byte in y_bytes)
        return x_binary, y_binary

class GeneticAlgorithm:
    def __init__(self, GeneClass: Type[Gene], genes_amount: int, mutation_p: int,
                 bounds: Tuple[float, float], func: str, crossover_points: int, generations: int):
        # Конструктор класса GeneticAlgorithm, инициализирующий параметры алгоритма и создающий начальную популяцию генов
        self.genes: List[GeneClass] = self._make_genes(GeneClass, genes_amount, mutation_p, bounds, func)
        self.crossover_points: int = crossover_points
        self.generations: int = generations
        self.genes_amount = genes_amount
        self.iterations: list[list[GeneClass]] = []

    def _make_genes(self, GeneClass, genes_amount, mutation_p, bounds, func) -> List[Gene]:
        # Создание начальной популяции генов
        genes = []
        for _ in range(genes_amount):
            gene = GeneClass(bounds, mutation_p, func)
            genes.append(gene)
        return genes

    def solve(self) -> Gene:
        # Решение задачи оптимизации с использованием генетического алгоритма
        self.iterations.append(self.genes.copy())
        for _ in range(self.generations):
            crossovered_genes = self.crossover_population(deepcopy(self.genes))
            mutated_genes = self.mutate_population(deepcopy(self.genes))
            self.genes += crossovered_genes + mutated_genes
            self.selection()
            self.iterations.append(self.genes.copy())
        best_gene = max(self.genes, key=float)
        return best_gene

    def selection(self) -> None:
        # Отбор лучших генов методом турнирного отбора
        new_genes = []
        for _ in range(self.genes_amount):
            tournament_size = max(2, int(self.genes_amount * 0.1))  # Размер турнира, настраиваемый параметр
            tournament = random.sample(self.genes, tournament_size)
            winner = min(tournament, key=float)
            new_genes.append(deepcopy(winner))
        self.genes = new_genes

    def crossover_population(self, genes_list: list[Gene]) -> list[Gene]:
        # Кроссовер популяции генов
        new_genes = []
        fitness_values = np.array([float(gene) for gene in genes_list], dtype=float)
        weights = 1 / (0.1 + abs(fitness_values - np.min(fitness_values)))
        normalised_weights = weights / np.sum(weights)
        print(normalised_weights)
        was = []
        for _ in range(len(genes_list) // 2):
            parent1, parent2 = self.select_parents(genes_list, normalised_weights)
            if (parent1.decoded(), parent2.decoded()) in was:
                continue
            was += [(parent1.decoded(), parent2.decoded()), (parent2.decoded(), parent1.decoded())]
            child1, child2 = self.crossover(parent1, parent2)
            new_genes.extend([child1, child2])
        return new_genes

    def mutate_population(self, genes_list: list[Gene]) -> list[Gene]:
        # Мутация популяции генов
        for gene in genes_list:
            gene.mutate()
        return genes_list

    def select_parents(self, genes_list, weights) -> Tuple[Gene, Gene]:
        # Выбор родителей для кроссовера
        while True:
            ind_p1, ind_p2 = np.random.choice(self.genes_amount, size=2, p=weights)
            if ind_p1 != ind_p2:
                break
        return genes_list[ind_p1], genes_list[ind_p2]

    def crossover(self, parent1: Gene, parent2: Gene) -> Tuple[Gene, Gene]:
        # Кроссовер между двумя генами
        crossover_points = sorted(random.sample(range(len(parent1.encoded()[0])), self.crossover_points))

        parent1_encoded = list(parent1.encoded())
        parent2_encoded = list(parent2.encoded())

        print(parent1.decoded(), parent2.decoded())
        for i in range(1, len(crossover_points), 2):
            start = crossover_points[i - 1]
            end = crossover_points[i]

            # Выполнение кроссовера на списках
            parent1_encoded[0] = parent1_encoded[0][:start] + parent2_encoded[0][start:end] + parent1_encoded[0][end:]
            parent2_encoded[0] = parent2_encoded[0][:start] + parent1_encoded[0][start:end] + parent2_encoded[0][end:]

            parent1_encoded[1] = parent1_encoded[1][:start] + parent2_encoded[1][start:end] + parent1_encoded[1][end:]
            parent2_encoded[1] = parent2_encoded[1][:start] + parent1_encoded[1][start:end] + parent2_encoded[1][end:]

        child1 = deepcopy(parent1)
        child2 = deepcopy(parent2)
        # Преобразование списков обратно в строки
        child1.decoded(tuple(parent1_encoded))
        child2.decoded(tuple(parent2_encoded))
        if np.nan in child1.decoded():
            child1 = parent1
        if np.nan in child2.decoded():
            child2 = parent2
        return child1, child2