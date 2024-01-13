"""
    Genetic Algorithm - Crossover phase.

    This module performs the crossover phase of a Genetic Algorithm using single-point crossover.

    Parameters:
    - population_matrix: Matrix representing the population's binary-encoded chromosomes.
    - crossover_rate: The crossover rate for the genetic algorithm.
    - strings: Number of strings in each chromosome.
    - gene: Number of genes/bytes in each string.

    Returns:
    - new_population_matrix: A 2D array representing the population of chromosomes after the crossover phase.

"""

import numpy as np

def crossover(population_matrix, crossover_rate, strings, gene ):
    population_size = len(population_matrix)

    # Initialize a new matrix to store the children
    new_population_matrix = np.zeros_like(population_matrix)

    # Perform crossover for pairs of selected chromosomes
    for i in range(population_size // 2): 
        # Select two random indices for crossover pair
        parent_indices = np.random.choice(population_size, size=2, replace=False)

        print("parent_indices: ", parent_indices)

        # Get the chromosomes for crossover
        parent1 = population_matrix[parent_indices[0]]
        parent2 = population_matrix[parent_indices[1]]

        # Check if crossover should be performed based on the crossover rate
        if np.random.rand() < crossover_rate:
            print("Crossover performed")
            # Select a random crossover point
            crossover_point = np.random.randint(1, gene)
            print("crossover_point: ", crossover_point)

            # Get the index of the crossover point for each string
            cross_point = gene - crossover_point

            # Perform crossover for each string
            for j in range(strings):
                # Get the start and end indices for the current string
                start_index = j * gene
                end_index = start_index + gene
                
                # Perform crossover for the current string
                new_population_matrix[i * 2, start_index:end_index] = np.concatenate((parent1[start_index:cross_point], parent2[cross_point:end_index]))
                new_population_matrix[i * 2 + 1, start_index:end_index] = np.concatenate((parent2[start_index:cross_point], parent1[cross_point:end_index]))

                cross_point += gene
        
        else: 
            # If crossover is not performed, then the parents are copied into the new population
            print("Crossover not performed")
            new_population_matrix[i * 2] = parent1
            new_population_matrix[i * 2 + 1] = parent2


    # Check if the number of chromosomes is odd
    if population_size % 2 != 0:
        print("Odd number of chromosomes")
        # Select a random index for the last chromosome
        last_index = np.random.randint(0, population_size)
        print("last_index: ", last_index)
        # Copy the last chromosome into the new population
        new_population_matrix[- 1] = population_matrix[last_index]

    return new_population_matrix
