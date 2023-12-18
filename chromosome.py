import random

class Chromosome:
    def __init__(self, genes=None):
        if genes is None:
            self.genes = self.generate_random_genes()
        else:
            self.genes = genes

    def generate_random_genes(self):
        return [
            random.randint(1, 8) for _ in range(20)
        ]  

    def get_genes(self):
        return self.genes

    def crossover(self, partner):
        crossover_point = random.randint(0, min(len(self.genes), len(partner.genes)))
        new_genes = self.genes[:crossover_point] + partner.genes[crossover_point:]
        return new_genes

    def mutation(self):
        mutation_rate = 0.1
        for i in range(len(self.genes)):
            if random.random() < mutation_rate:
                self.genes[i] = random.randint(1, 8)