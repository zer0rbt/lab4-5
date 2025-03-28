# Importing libraries and modules
import random
import struct
from copy import deepcopy
from typing import TypedDict
import numpy as np
import matplotlib.pyplot as plt

# Definition of TypedDict for the particle structure
class Particle(TypedDict):
    x1: float
    x2: float
    pbest_x1: float
    pbest_x2: float

# Initializing particles with random values within specified bounds
def initialize_particles(bounds, amount):
    """
    Initialize particles with random values.

    Parameters:
    - bounds: Range of values for initialization (list, [min, max]).
    - amount: Number of particles.

    Returns:
    - List of particles in TypedDict format.
    """
    particles = []
    for _ in range(amount):
        particles.append(Particle(
            x1=random.uniform(bounds[0], bounds[1]),
            x2=random.uniform(bounds[0], bounds[1]),
            pbest_x1=random.uniform(0, 1),
            pbest_x2=random.uniform(0, 1)
        ))
    return particles

# Definition of the objective function
def func(f, x1, x2):
    """
    Compute the value of the objective function.

    Parameters:
    - f: String with the mathematical expression of the objective function.
    - x1, x2: Variable values.

    Returns:
    - Value of the objective function for the given variables.
    """
    return eval(f)

# Implementation of the PSO-based optimization algorithm
def algorithm(particles, generations, f, bounds):
    """
    Implementation of the PSO-based optimization algorithm.

    Parameters:
    - particles: Initial population of particles.
    - generations: Number of generations (iterations) of the algorithm.
    - f: String with the mathematical expression of the objective function.
    - bounds: Range of values for initialization (list, [min, max]).

    Returns:
    - Evolution history of the population at each generation.
    """
    history = [deepcopy(sorted(particles, key=lambda x: func(f, x['x1'], x['x2'])))]
    for _ in range(generations):
        gbest = (history[-1][0]['x1'], history[-1][0]['x2'])
        for particle in particles:
            f_was = func(f, particle['x1'], particle['x2'])
            particle['x1'] = np.random.normal((gbest[0] + particle['pbest_x1']) / 2,
                                              abs(gbest[0] - particle['pbest_x1']))
            particle['x2'] = np.random.normal((gbest[1] + particle['pbest_x2']) / 2,
                                              abs(gbest[1] - particle['pbest_x2']))
            f_now = func(f, particle['x1'], particle['x2'])
            if f_now < f_was:
                particle['pbest_x1'] = particle['x1']
                particle['pbest_x2'] = particle['x2']
        particles = sorted(particles, key=lambda x: func(f, x['x1'], x['x2']))
        history.append(deepcopy(particles))
    return history