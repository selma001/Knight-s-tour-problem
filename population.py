from knight import Knight
import random
from chromosome import Chromosome

class Population:
    def __init__(self, population_size):
        self.population_size = population_size
        self.generation = 1
        self.knights = [Knight() for _ in range(population_size)]

    def check_population(self):
        for knight in self.knights:
            knight.check_moves()

    def evaluate(self):
        best_knight = None
        max_fitness = float("-inf")

        for knight in self.knights:
            knight.evaluate_fitness()
            if knight.fitness > max_fitness:
                max_fitness = knight.fitness
                best_knight = knight

        return max_fitness, best_knight

    def tournament_selection(self, size=3):
        selected_parents = []

        for _ in range(size):
            sample = random.sample(self.knights, size)
            selected_parents.append(max(sample, key=lambda x: x.fitness))

        return selected_parents

    def create_new_generation(self):
        new_population = []

        while len(new_population) < self.population_size:
            parents = self.tournament_selection(2)

            parent1_chromosome = parents[0].chromosome
            parent2_chromosome = parents[1].chromosome

            offspring1_genes = parent1_chromosome.crossover(parent2_chromosome)
            offspring2_genes = parent2_chromosome.crossover(parent1_chromosome)

            offspring1 = Knight(Chromosome(offspring1_genes))
            offspring2 = Knight(Chromosome(offspring2_genes))

            offspring1.chromosome.mutation()
            offspring2.chromosome.mutation()

            new_population.extend([offspring1, offspring2])

        self.knights = new_population
        self.generation += 1