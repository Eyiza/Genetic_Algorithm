from phases.generate_initial import generateInitialPopulation
from phases.evaluation import evalation
from phases.selection import selection

def main():
    fitness_function = "(4 * x1**2) + (2 * x1 * x2) + (x2 * x3) - (3 * x3**2)" 
    boundary_range = [(0,4), (2,3), (1,6)] # The boundaries of each string
    num_generations = 100 # Number of generations
    population_size = 100 # Number of chromosomes in the population
    strings = 3 # Number of strings in each chromosome
    gene = 5 # Number of genes/bytes in each string
    chromesome_length = strings * gene # Number of genes/bytes in each chromosome
    
    population_matrix, mutation_rate, crossover_rate = generateInitialPopulation(population_size, chromesome_length)

    # Initial Generation
    fitness = evalation(population_matrix, population_size, strings, gene, fitness_function, boundary_range)
    # print("fitness: ", fitness)

    selected_chromosomes, best_index = selection(fitness)
    best_solution = population_matrix[best_index] # Best solution found so far
    best_fitness = fitness[best_index] # Fitness of the initial best solution found so far

    # print("best_solution: ", best_solution)
    # print("best_fitness: ", best_fitness)


    # while gen < num_generations:
    #     parents = evalation(population_matrix, population_size, strings, gene)
    #     gen += 1


if __name__ == "__main__":
    main()