import random
from typing import Type, List, Tuple
import numpy as np
import struct


class Gene:
    def __init__(self, bounds: Tuple[float, float], mutation_p: int, func: str):
        self.mutation_percentage: int = mutation_p
        self.func: str = func
        self.bounds: Tuple[float, float] = bounds
        self.x: float = random.uniform(-1, 1) * (self.bounds[1] - self.bounds[0])
        self.y: float = random.uniform(-1, 1) * (self.bounds[1] - self.bounds[0])

    def __float__(self):
        return float(eval(self.func))

    def set_coords(self, coord: Tuple[float, float]) -> None:
        self.x, self.y = coord

    def mutate(self) -> None:
        mutation = random.uniform(-1, 1) * (self.bounds[1] - self.bounds[0]) * (self.mutation_percentage / 100.0)
        self.x += mutation
        self.y += mutation
        self.x = max(min(self.x, self.bounds[1]), self.bounds[0])
        self.y = max(min(self.y, self.bounds[1]), self.bounds[0])

    def decoded(self, chromosomes: tuple[str, str] = tuple()) -> Tuple[float, float]:
        if not chromosomes:
            return self.x, self.y
        out: list[float] = []
        for binary_string in chromosomes:
            bytes_list = [binary_string[i:i + 8] for i in range(0, len(binary_string), 8)]
            byte_object = bytes([int(byte, 2) for byte in bytes_list])
            out.append(struct.unpack('!f', byte_object)[0])
        return tuple(out)

    def encoded(self) -> Tuple[str, str]:
        x_bytes = struct.pack('!f', self.x)
        y_bytes = struct.pack('!f', self.y)
        x_binary = ''.join(format(byte, '08b') for byte in x_bytes)
        y_binary = ''.join(format(byte, '08b') for byte in y_bytes)
        return x_binary, y_binary


class GeneticAlgorithm:
    def __init__(self, GeneClass: Type[Gene], genes_amount: int, mutation_p: int,
                 bounds: Tuple[float, float], func: str, crossover_points: int, generations: int):
        self.genes: List[GeneClass] = self._make_genes(GeneClass, genes_amount, mutation_p, bounds, func)
        self.crossover_points: int = crossover_points
        self.generations: int = generations
        self.genes_amount = genes_amount
        self.iterations: list[list[GeneClass]] = []

    def _make_genes(self, GeneClass, genes_amount, mutation_p, bounds, func) -> List[Gene]:
        genes = []
        for _ in range(genes_amount):
            gene = GeneClass(bounds, mutation_p, func)
            genes.append(gene)
        return genes

    def solve(self) -> Tuple[float, float]:
        for _ in range(self.generations):
            crossovered_genes = self.crossover_population(self.genes)
            mutated_genes = self.mutate_population(self.genes)
            self.genes += crossovered_genes + mutated_genes
            self.selection()
            self.iterations.append(self.genes.copy())
        best_gene = max(self.genes, key=float)
        return best_gene.decoded()

    def selection(self) -> None:
        new_genes = []
        for i in range(0, len(self.genes), int(len(self.genes) / self.genes_amount)):
            new_genes.append(min(self.genes[i:int(len(self.genes) / self.genes_amount)], key=float))
        new_genes += self.genes[len(new_genes) - self.genes_amount:]
        self.genes = new_genes

    def crossover_population(self, genes_list: list[Gene]) -> list[Gene]:
        new_genes = []
        fitness_values = np.array([float(gene) for gene in genes_list], dtype=float)
        weights = fitness_values / np.sum(fitness_values)
        for _ in range(len(genes_list) // 2):
            parent1, parent2 = self.select_parents(genes_list, weights)
            child1, child2 = self.crossover(parent1, parent2)
            new_genes.extend([child1, child2])
        return new_genes

    def mutate_population(self, genes_list: list[Gene]) -> list[Gene]:
        for gene in genes_list:
            gene.mutate()
        return genes_list

    def select_parents(self, genes_list, weights) -> Tuple[Gene, Gene]:
        ind_p1, ind_p2 = np.random.choice(self.genes_amount, size=2, p=weights)
        return genes_list[ind_p1], genes_list[ind_p2]

    def crossover(self, parent1: Gene, parent2: Gene) -> Tuple[Gene, Gene]:
        crossover_points = sorted(random.sample(range(len(parent1.encoded())), self.crossover_points))
        for i in range(1, len(crossover_points), 2):
            start = crossover_points[i - 1]
            end = crossover_points[i]
            parent1[start:end], parent2[start:end] = parent2[start:end], parent1[start:end]

        return parent1, parent2
