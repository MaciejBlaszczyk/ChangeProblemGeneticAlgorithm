from genotype import Genotype
import numpy as np


class Population:
    def __init__(self, quantity, statistical_day):
        self.quantity = quantity
        self.statistical_day = statistical_day
        self.population = [Genotype() for _ in range(quantity)]
        self.sorted_population = []
        self.cost_matrix = []
        self.rows_encoder = {1: 0,
                             2: 1,
                             5: 2}

    def calculate_changes_for_genotypes(self, available_values):
        for specimen in self.population:
            specimen.calculate_change_randomly(self.statistical_day, available_values)

    def show_sorted_population_and_cost(self):
        for specimen in self.sorted_population:
            print(specimen.genotype_matrix)
            print("cost:", specimen.cost)
            print("")

    def show_population_and_cost(self):
        for specimen in self.population:
            print(specimen.genotype_matrix)
            print("cost:", specimen.cost)
            print("")

    def calculate_cost(self, coin_to_save):
        for specimen in self.population:
            specimen.calculate_cost(coin_to_save)

    def calculate_cost_for_sorted_population(self, coin_to_save):
        self.cost_matrix = []
        for specimen in self.sorted_population:
            self.cost_matrix.append(specimen.calculate_cost(coin_to_save))

    def lowest_cost(self):
        return min(self.cost_matrix)

    def rank(self):
        self.sorted_population = sorted(self.population, key=lambda x: x.cost)

    def cross(self, coin_to_save, amount_of_species):
        self.population = [Genotype() for _ in range(round((amount_of_species / 4) * ((amount_of_species / 2) - 1)))]
        counter = 0
        for i in range(round(len(self.sorted_population) / 2)):
            for j in range(i + 1, round(len(self.sorted_population) / 2)):
                for k in range(9):
                    if self.sorted_population[i].genotype_matrix[self.rows_encoder[coin_to_save]][k] > self.sorted_population[j].genotype_matrix[self.rows_encoder[coin_to_save]][k]:
                        self.population[counter].genotype_matrix[self.rows_encoder[1]][k] = \
                            self.sorted_population[j].genotype_matrix[self.rows_encoder[1]][k]
                        self.population[counter].genotype_matrix[self.rows_encoder[2]][k] = \
                            self.sorted_population[j].genotype_matrix[self.rows_encoder[2]][k]
                        self.population[counter].genotype_matrix[self.rows_encoder[5]][k] = \
                            self.sorted_population[j].genotype_matrix[self.rows_encoder[5]][k]
                    else:
                        self.population[counter].genotype_matrix[self.rows_encoder[1]][k] = \
                            self.sorted_population[i].genotype_matrix[self.rows_encoder[1]][k]
                        self.population[counter].genotype_matrix[self.rows_encoder[2]][k] = \
                            self.sorted_population[i].genotype_matrix[self.rows_encoder[2]][k]
                        self.population[counter].genotype_matrix[self.rows_encoder[5]][k] = \
                            self.sorted_population[i].genotype_matrix[self.rows_encoder[5]][k]
                counter += 1
        np.random.shuffle(self.population)
        self.population = self.population[0:amount_of_species]


