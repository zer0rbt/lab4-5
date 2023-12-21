import math
import random
from typing import Type, List, Tuple
import numpy as np
from copy import deepcopy


class Unit:
    def __init__(self, func, bounds, local_best_weight, global_best_weight):
        # Инициализация частицы в алгоритме оптимизации
        # func - оптимизируемая функция
        # bounds - границы области поиска
        # local_best_weight - вес влияния лучшей локальной позиции
        # global_best_weight - вес влияния лучшей глобальной позиции
        self.func = func
        self.bounds = bounds
        self.pos: list[float, float] = [random.uniform(self.bounds[0], self.bounds[1]),
                                        random.uniform(self.bounds[0], self.bounds[1])]
        self.u = [0, 0]
        self.phi1 = local_best_weight
        self.phi2 = global_best_weight
        self.local_best = self.pos.copy()
        self.velocity_formula = "v_t + phi1 * (p1 - x_t) + phi2 * (p2 - x_t)"
        self.position_formula = "chi * (v_t1) + chi * x_t + (1 - chi) * (phi1 * p1 + phi2 * p2) / (phi1 + phi2)"
        self.chi_formula = "2 * k / abs(2 - phi1 - phi2 - ((phi1 + phi2) * (phi1 + phi2 - 4)) ** 0.5)"

    def __float__(self):
        # Преобразование позиции частицы в число с использованием целевой функции
        x = self.pos[0]
        y = self.pos[1]
        x1 = x
        x2 = y
        return float(eval(self.func))

    def calculate_speed(self, phi1, phi2, v_t, x_t, p1, p2):
        # Расчет новой скорости частицы
        return eval(self.velocity_formula)

    def calculate_position(self, phi1, phi2, v_t1, x_t, p1, p2, chi):
        # Расчет новой позиции частицы
        return eval(self.position_formula)

    def calculate_chi(self, phi1, phi2):
        # Расчет параметра chi, контролирующего влияние лучших локальных и глобальных позиций
        k = random.uniform(0, 1)
        return k if phi1 + phi2 == 4 else eval(self.chi_formula)

    def turn(self, global_best):
        # Обновление скорости, позиции и лучшей локальной позиции частицы
        chi = self.calculate_chi(phi1=self.phi1, phi2=self.phi2)
        for i in range(len(self.pos)):
            self.u[i] = self.calculate_speed(phi1=self.phi1, phi2=self.phi2, p1=self.local_best[i], p2=global_best[i],
                                             v_t=self.u[i], x_t=self.pos[i])

            self.pos[i] = self.calculate_position(phi1=self.phi1, phi2=self.phi2, p1=self.local_best[i],
                                                  p2=global_best[i],
                                                  v_t1=self.u[i], x_t=self.pos[i], chi=chi)
            if self.pos[i] != max(min(self.pos[i], self.bounds[1]), self.bounds[0]):
                self.pos[i] = max(min(self.pos[i], self.bounds[1]), self.bounds[0])
                self.u[i] *= (-1/100)

        x, y = global_best
        x1, x2 = x, y
        if float(self) > eval(self.func):
            self.local_best = self.pos.copy()


class Swarm:
    def __init__(self, UnitClass: Type[Unit], units_amount: int, global_best_weight: int, local_best_weight: int,
                 bounds: Tuple[float, float], func: str, generations: int):
        # Инициализация роя частиц в алгоритме оптимизации
        # UnitClass - тип частицы в рое
        # units_amount - количество частиц в рое
        # global_best_weight - вес влияния лучшей глобальной позиции
        # local_best_weight - вес влияния лучшей локальной позиции
        # bounds - границы области поиска
        # func - оптимизируемая функция
        # generations - количество итераций алгоритма
        self.units: List[UnitClass] = self._make_units(UnitClass, units_amount, global_best_weight, local_best_weight,
                                                       bounds, func)
        self.generations: int = generations
        self.units_amount = units_amount
        self.iterations: list[list[UnitClass]] = []

    def _make_units(self, UnitClass, units_amount, global_best_weight, local_best_weight, bounds, func):
        # Создание частиц в рое
        units = []
        for _ in range(units_amount):
            unit = UnitClass(bounds=bounds, global_best_weight=global_best_weight, local_best_weight=local_best_weight,
                             func=func)
            units.append(unit)
        return units

    def solve(self, num_iterations):
        # Запуск алгоритма на указанное количество итераций
        self.iterations.append(deepcopy(self.units))
        for _ in range(num_iterations):
            for agent in self.units:
                agent.turn(self.get_global_best().pos)
            self.iterations.append(deepcopy(self.units))
        return self.get_global_best().pos

    def get_global_best(self):
        # Получение лучшей глобальной позиции в рое
        return min(self.units, key=float)
