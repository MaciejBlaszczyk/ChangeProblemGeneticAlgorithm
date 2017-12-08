from genotype import Genotype
import numpy as np
from cross_operator import cross_mc


class Population:
    def __init__(self, quantity, statistical_day):
        self.quantity = quantity
        self.statistical_day = statistical_day
        self.population = [Genotype() for _ in range(quantity)]
        self.sorted_population = []
        self.cost_matrix = []
        self.rows_encoder = {1: 0,
                             2: 1,
                             5: 2,
                             10: 3,
                             20: 4,
                             50: 5}

    def calculate_changes_for_specimens(self, available_values):
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

    def calculate_cost(self, coin_to_save, quantity_of_coins,expected_quantity_of_coins):
        for specimen in self.population:
            specimen.calculate_cost(coin_to_save, quantity_of_coins,expected_quantity_of_coins)

    def calculate_cost_matrix_for_sorted_population(self):
        self.cost_matrix = []
        for specimen in self.sorted_population:
            self.cost_matrix.append(specimen.cost)

    def rank(self):
        self.sorted_population = sorted(self.population, key=lambda x: x.cost)


    def cross(self, amount_of_species):
        young_population = Population(self.quantity,self.statistical_day)
        for i in range(amount_of_species):
            if (i%2) == 0:
                young_population.population[i] = cross_mc(self.population[i], self.population[i+1])
                young_population.population[i+1] = cross_mc(self.population[i+1], self.population[i])

        for i in range (amount_of_species):
            self.population[i].genotype_matrix = young_population.population[i].genotype_matrix






'''

    def cross(self, coin_to_save, amount_of_species):
        self.population = [Genotype() for _ in range(round((amount_of_species / 4) * ((amount_of_species / 2) - 1)))]
        counter = 0
        for i in range(round(len(self.sorted_population) / 2)):
            for j in range(i + 1, round(len(self.sorted_population) / 2)):
                for k in range(18):
                    if self.sorted_population[i].genotype_matrix[self.rows_encoder[coin_to_save]][k] > self.sorted_population[j].genotype_matrix[self.rows_encoder[coin_to_save]][k]:
                        for m in range(6):
                            self.population[counter].genotype_matrix[m][k] = self.sorted_population[j].genotype_matrix[m][k]
                    else:
                        for m in range(6):
                            self.population[counter].genotype_matrix[m][k] = self.sorted_population[i].genotype_matrix[m][k]
                counter += 1
        np.random.shuffle(self.population)
        self.population = self.population[0:amount_of_species]





#TODO
#when coin to save = 1, while loop never stops for example for value_to_exchange = 21 when we randomly take 4x5 and now we need just 1 (21-20=1)
    def mutate(self, coin_to_save, available_values):
        random_specimen = np.random.choice(self.population)
        random_col = np.random.choice(range(random_specimen.number_of_ways_to_give_change))
        amount_of_coins_which_are_supposed_to_be_saved = random_specimen.genotype_matrix[self.rows_encoder[coin_to_save]][random_col]
        value_to_exchange = amount_of_coins_which_are_supposed_to_be_saved * coin_to_save
        available_values_without_coin_to_save = list(available_values)
        available_values_without_coin_to_save.remove(coin_to_save)

        temp = 0
        while temp != value_to_exchange:
            generated_value = np.random.choice(available_values_without_coin_to_save)
            if temp + generated_value <= value_to_exchange:
                temp = temp + generated_value
                random_specimen.genotype_matrix[self.rows_encoder[generated_value]][random_col] += 1

        random_specimen.genotype_matrix[self.rows_encoder[coin_to_save]][random_col] = 0

'''

