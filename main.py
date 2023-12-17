from phases.generate_initial import generateInitialPopulation
from phases.evaluation import evalation


def main():
    fitness_function = "(4 * x1**2) + (2 * x1 * x2) + (x2 * x3) - (3 * x3**2)" 
    boundary_range = [(0,4), (2,3), (1,6)] # The boundaries of each string
    num_generations = 100 # Number of generations
    population_size = 100 # Number of chromosomes in the population
    strings = 3 # Number of strings in each chromosome
    gene = 5 # Number of genes/bytes in each string
    chromesome_length = strings * gene # Number of genes/bytes in each chromosome

    best_solution = None # Best solution found so far
    best_fitness = 0 # Fitness of the best solution found so far
    
    gen = 0 # Generation number
    population_matrix, mutation_rate, crossover_rate = generateInitialPopulation(population_size, chromesome_length)

    parents = evalation(population_matrix, population_size, strings, gene, fitness_function, boundary_range)

    # while gen < num_generations:
    #     parents = evalation(population_matrix, population_size, strings, gene)
    #     gen += 1


if __name__ == "__main__":
    main()