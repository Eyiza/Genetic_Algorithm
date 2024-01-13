"""
    Genetic Algorithm: Generate Initial Population
    
    This module provides a function to generate the initial population of chromosomes for a genetic algorithm.

    Function:
    generate_initial_population(population_size, chromosome_length)

    Parameters:
    - population_size (int): The number of individuals in the population.
    - chromosome_length (int): The length of each chromosome in the population.

    Returns:
    - population_matrix (numpy.ndarray): A 2D array representing the initial population of chromosomes.
    - mutation_rate (float): The mutation rate for the genetic algorithm.
    - crossover_rate (float): The crossover rate for the genetic algorithm.
"""

import numpy as np

def generateInitialPopulation(population_size, chromesome_length):
    # Generate mutation and crossover rates
    crossover_rate = np.random.rand()
    mutation_rate = np.random.uniform(0, 0.5) # Mutation rate is usually set to a low value


    # Generate a population of random binary numbers
    population = np.random.randint(0, 2, size=(population_size, chromesome_length))    

    return population, mutation_rate, crossover_rate

