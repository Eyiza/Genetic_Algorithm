from phases.generate_initial import generateInitialPopulation
from phases.evaluation import evalation
from phases.selection import selection
from phases.crossover import crossover
from phases.mutation import mutation

def main():
    # Parameters
    fitness_function = "(4 * x1**2) + (2 * x1 * x2) + (x2 * x3) - (3 * x3**2)" 
    boundary_range = [(0,4), (2,3), (1,6)] # The boundaries of each string
    num_generations = 100 # Number of generations
    population_size = 100 # Number of chromosomes in the population
    strings = 3 # Number of strings in each chromosome
    gene = 5 # Number of genes/bytes in each string
    chromesome_length = strings * gene # Number of genes/bytes in each chromosome

    # Initial Generation i.e gen = 0 
    print("Initial Generation")
    population_matrix, mutation_rate, crossover_rate = generateInitialPopulation(population_size, chromesome_length)
    fitness = evalation(population_matrix, population_size, strings, gene, fitness_function, boundary_range)
    best_index, new_population_matrix = selection(fitness, population_matrix)


    best_solution = population_matrix[best_index] # Best solution found so far
    best_fitness = fitness[best_index] # Fitness of the best solution found so far

    for gen in range(1, num_generations + 1):
        print("Generation: ", gen)

        population_matrix = new_population_matrix

        # Crossover
        population_matrix = crossover(population_matrix, crossover_rate, strings, gene)

        # Mutation
        population_matrix = mutation(population_matrix, mutation_rate, strings, gene)
        
        # Evaluation
        fitness = evalation(population_matrix, population_size, strings, gene, fitness_function, boundary_range)

        # Selection
        best_index, new_population_matrix = selection(fitness, population_matrix)

        # Update best solution if a better solution is found
        if fitness[best_index] > best_fitness:
            best_solution = population_matrix[best_index]
            best_fitness = fitness[best_index]


    print("best_solution: ", best_solution)
    print("best_fitness: ", best_fitness)

if __name__ == "__main__":
    main()