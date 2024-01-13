# Genetic_Algorithm

## Description
The genetic algorithm is a method for solving both constrained and unconstrained optimization problems that is based on natural selection, the process that drives biological evolution. The genetic algorithm repeatedly modifies a population of individual solutions. At each step, the genetic algorithm selects individuals at random from the current population to be parents and uses them to produce the children for the next generation. Over successive generations, the population "evolves" toward an optimal solution. You can apply the genetic algorithm to solve a variety of optimization problems that are not well suited for standard optimization algorithms, including problems in which the objective function is discontinuous, nondifferentiable, stochastic, or highly nonlinear. 


## Installation

1. **Virtual Environment** - This keeps your dependencies for each project separate and organized. 
Initialize and activate a virtual environment using:
```bash
python -m venv env
source env/bin/activate
```

Note - In Windows, the `env` does not have a `bin` directory. Therefore, you'd use the analogous command shown below:
```bash
env/Scripts/activate
```

2. **PIP Dependencies** - Once the virtual environment is setup and running, install the required dependencies by running:
```bash
pip install -r requirements.txt
```
All required packages are included in the requirements file. 


## Usage
To change the parameters of the genetic algorithm, open the `main.py` file and edit the following lines of code:
```python
# Genetic Algorithm Parameters
fitness_function # Objective function
boundary_range # The boundaries of each string
num_generations # Number of generations
population_size # Number of chromosomes in the population
strings # Number of strings in each chromosome
gene = 5 # Number of genes/bytes in each string
```

To run the genetic algorithm, execute the following command in the terminal:
```bash
python main.py
```

## Output
After running the genetic algorithm, a plot image named `best_fitness_plot.png` will be created in the current working directory. This image illustrates the improvement of the best fitness over generations. <br>
The best fitness and solution will also be printed to the terminal.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## References
- [Introduction to Genetic Algorithms](https://towardsdatascience.com/introduction-to-genetic-algorithms-including-example-code-e396e98d8bf3)
- [Genetic Algorithm Implementation in Python](https://towardsdatascience.com/genetic-algorithm-implementation-in-python-5ab67bb124a6)
- [Genetic Algorithm and its practicality in Machine Learning](https://towardsdatascience.com/genetic-algorithm-6aefd897f1ac)


## Author
Precious Michael