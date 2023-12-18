"""
    Genetic Algorithm - Selection Phase

    This module performs the selection phase of a Genetic Algorithm. 
    It selects chromosomes from the population for the crossover phase based on their fitness values, employing roulette wheel selection.

    Parameters:
    - fitness: List of fitness values corresponding to each chromosome in the population.

    Returns:
    - selected_chromosomes: List of selected chromosome indices for the crossover phase.
    - best_index: Index of the chromosome with the highest fitness in the population.
"""

import numpy as np
from collections import Counter

def selection(fitness):
    populaion_size = len(fitness)
    if min(fitness) < 0:
        fitness = fitness + abs(min(fitness))

        
    # Calculate the total fitness of the population
    cumulative_fitness = np.cumsum(fitness)
    total_fitness = np.sum(fitness)

    # Generate random numbers between 0 and 1
    random_numbers = np.random.random_sample(populaion_size)

    # Select the chromosomes that corresponds to the random number based on the cumulative fitness
    selected_chromosomes = []
    
    for number in random_numbers:
        random_number = number * total_fitness
        for i in range(1, populaion_size + 1):
            if random_number < cumulative_fitness[i]:
                selected_chromosomes.append(i)
                break

    # Get the index of chromosome with the best fitness
    best_index = np.argmax(fitness)

    # Count occurrences of each chromosome
    # chromosome_counts = Counter(selected_chromosomes) 
    # print("Chromosome counts:", chromosome_counts)

    return selected_chromosomes, best_index
