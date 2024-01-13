"""
    Genetic Algorithm - Mutation phase.

    This module performs the mutation phase of a Genetic Algorithm using single-point mutation.

    Parameters:
    - population_matrix: Matrix representing the population's binary-encoded chromosomes.
    - mutation_rate: The mutation rate for the genetic algorithm.
    - strings: Number of strings in each chromosome.
    - gene: Number of genes/bytes in each string.

    Returns:
    - new_population_matrix: A 2D array representing the population of chromosomes after the mutation phase.
"""

import numpy as np

def mutation(population_matrix, mutation_rate, strings, gene):
    population_size = len(population_matrix)

    # Initialize a new matrix to store the children
    new_population_matrix = np.zeros_like(population_matrix)

    # Perform mutation for each chromosome
    for i in range(population_size // 2):

        # Select two random indices for mutation pair
        parent_indices = np.random.choice(population_size, size=2, replace=False)

        print("parent_indices: ", parent_indices)

        # Get the chromosomes for mutation
        parent1 = population_matrix[parent_indices[0]]
        parent2 = population_matrix[parent_indices[1]]

        new_population_matrix[i * 2] = parent1
        new_population_matrix[i * 2 + 1] = parent2

        # Check if mutation should be performed based on the mutation rate
        if np.random.rand() < mutation_rate:
            print("Mutation performed")
            # Select a random mutation point
            mutation_point = np.random.randint(1, gene)
            print("mutation_point: ", mutation_point)

            # Get the index of the mutation point for each string
            mutate_point = gene - mutation_point

            # Perform mutation for each string
            for j in range(strings):
                # Perform mutation for the current string
                new_population_matrix[i * 2, mutate_point] = parent2[mutate_point]
                new_population_matrix[i * 2 + 1, mutate_point] = parent1[mutate_point]

                mutate_point += gene

        else:
            # If mutation is not performed, then the parents are copied into the new population
            print("Mutation not performed")

    return new_population_matrix
