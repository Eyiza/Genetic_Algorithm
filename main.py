from phases.generate_initial import generateInitialPopulation

def main():
    num_generations = 100 # Number of generations
    population_size = 100 # Number of chromosomes in the population
    strings = 3 # Number of strings in each chromosome
    gene = 5 # Number of genes/bytes in each string
    chromesome_length = strings * gene # Number of genes/bytes in each chromosome
    
    population_matrix, mutation_rate, crossover_rate = generateInitialPopulation(population_size, chromesome_length)

    print(population_matrix)


if __name__ == "__main__":
    main()