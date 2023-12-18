"""
    Genetic Algorithm Fitness Evaluation

    This module evaluates the fitness of each chromosome in a population using a given binary-encoded genetic representation. 
    It decodes the chromosomes, maps them to decimal values within specified boundaries, and calculates fitness based on a user-defined fitness function.

    Parameters:
    - population_matrix: Matrix representing the population's binary-encoded chromosomes.
    - population_size: Number of chromosomes in the population.
    - strings: Number of strings in each chromosome.
    - gene: Number of genes/bytes in each string.
    - fitness_function: String representation of the fitness function in terms of x1, x2, x3.
    - boundary_range: List of tuples specifying the boundaries for each variable (x1, x2, x3).

    Returns:
    - fitness: Matrix containing the fitness value for each chromosome.
"""


import numpy as np

def binary_to_decimal(binary):
    binary_string = ''.join(map(str, binary)) # Convert each element in the binary list to a string and then join them together.
    decimal_value = int(binary_string, 2) # Convert the binary string to a decimal value
    return decimal_value


def evalation(population_matrix, population_size, strings, gene, fitness_function, boundary_range):
    # Decode each string in each chromosome
    decoded_population = np.zeros((population_size, strings), dtype=int) # Create a matrix to store the decoded population
    de_values = np.zeros((population_size, strings))


    for i in range(population_size): # For each chromosome
        start_index = 0 # The start index of the current string
        for j in range(strings): # For each string in the chromosome
            end_index = start_index + gene # The end index of the current string
            binary = population_matrix[i, start_index:end_index] # The binary representation of the current string. Note: i is the index of the current row you are interested in
            decoded_population[i, j] = binary_to_decimal(binary) # The decimal representation of the current string
            de_values[i, j] = boundary_range[j][0] + ( (decoded_population[i, j] * (boundary_range[j][1] - boundary_range[j][0])) ) / ((2 ** gene) - 1)
            start_index = end_index # Update the start index for the next string


    # Evaluate fitness of each chromosome using the fitness function
    fitness = np.zeros((population_size, 1)) # Create a matrix to store the fitness of each chromosome
    for i in range(population_size): 
        x1, x2, x3 = de_values[i]
        fitness[i] = eval(fitness_function)
        
    return fitness