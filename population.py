from genotype import Genotype
import numpy as np
from encoders import *


class Population:
    def __init__(self, quantity, statistical_day, coins_to_save, cross_function, mutate_function, mutation, expected_quantity_of_coins):
        self.quantity = quantity
        self.statistical_day = statistical_day
        self.population = [Genotype() for _ in range(quantity)]
        self.sorted_population = []
        self.coins_to_save = coins_to_save
        self.cost_matrix = [10000]
        self.cross_function = cross_function
        self.mutation_function = mutate_function
        self.mutation = mutation
        self.expected_quantity_of_coins = expected_quantity_of_coins

    def calculate_changes_for_specimens(self, available_coins):
        print("Calculating changes")
        for specimen in self.population:
            specimen.calculate_change_randomly(self.statistical_day, available_coins)

    def show_sorted_population_and_cost(self):
        for specimen in self.sorted_population:
            print('\n'.join([''.join(['{:5}'.format(item) for item in row]) for row in specimen.genotype_matrix]))
            print("cost:", specimen.cost)
            print("")

    def show_population_and_cost(self):
        for specimen in self.population:
            print(specimen.genotype_matrix)
            print("cost:", specimen.cost)
            print("")

    def calculate_cost_for_population(self):
        for specimen in self.population:
            specimen.calculate_cost(self.coins_to_save, self.expected_quantity_of_coins)

    def calculate_cost_matrix_for_sorted_population(self):
        self.cost_matrix = []
        for specimen in self.sorted_population:
            self.cost_matrix.append(specimen.cost)

    def rank(self):
        self.sorted_population = sorted(self.population, key=lambda x: x.cost)

    def cross_and_choose_new_population_randomly_from_crossed_specimens(self, amount_of_species):
        coin_chosen_to_save = np.random.choice(self.coins_to_save)
        for i in range(round(len(self.sorted_population) / 2)):
            for j in range(i + 1, round(len(self.sorted_population) / 2)):
                self.population.append(self.cross_function(self.sorted_population[i], self.sorted_population[j], coin_chosen_to_save, self.expected_quantity_of_coins[self.coins_to_save.index(coin_chosen_to_save)]))

        np.random.shuffle(self.population)
        self.population = self.population[0:amount_of_species]

    def mutate(self, available_coins):
        self.mutation_function(self.population, available_coins, self.coins_to_save)

    @staticmethod
    def mutate_randomly(pop, available_coins, coins_to_save):
        specimen_a = np.random.choice(pop)
        specimen_b = np.random.choice(pop)
        mut = np.random.choice(22)
        for i in range(8):
            specimen_a.genotype_matrix[i][mut] = specimen_b.genotype_matrix[i][mut]

    #TODO
    # when coin to save = 1, while loop never stops.
    # For example for value_to_exchange = 21 when we randomly take 4x5 we need just 1 (21-20=1)
    @staticmethod
    def mutate_by_replacing_usage_of_important_coin_with_other_coins(pop, available_coins, coins_to_save):
        coin_chosen_to_save = np.random.choice(coins_to_save)
        random_specimen = np.random.choice(pop)
        random_col = np.random.choice(range(random_specimen.number_of_ways_to_give_change))
        amount_of_coins_which_are_supposed_to_be_saved = random_specimen.genotype_matrix[rows_encoder[coin_chosen_to_save]][random_col]
        value_to_exchange = amount_of_coins_which_are_supposed_to_be_saved * coin_chosen_to_save
        available_coins_without_coins_to_save = list(available_coins)
        available_coins_without_coins_to_save.remove(coin_chosen_to_save)

        temp = 0
        while temp != value_to_exchange:
            generated_value = np.random.choice(available_coins_without_coins_to_save)
            if temp + generated_value <= value_to_exchange:
                temp = temp + generated_value
                random_specimen.genotype_matrix[rows_encoder[generated_value]][random_col] += 1

        random_specimen.genotype_matrix[rows_encoder[coin_chosen_to_save]][random_col] = 0

    @staticmethod
    def cross_mc(specimen_a, specimen_b, coin_chosen_to_save, coin_quantity):
        specimen_c = Genotype()
        rows = 8
        col = 22
        for i in range(rows):
            for j in range(int(col / 2)):
                specimen_c.genotype_matrix[i][j] = specimen_a.genotype_matrix[i][j]
        for i in range(rows):
            for j in range(int(col / 2), col):
                specimen_c.genotype_matrix[i][j] = specimen_b.genotype_matrix[i][j]
        return specimen_c

    @staticmethod
    def cross_by_choosing_the_best_values(specimenA, specimenB, coin_chosen_to_save, coin_quantity):
        temp_specimen = Genotype()
        for k in range(22):
            if abs(specimenA.genotype_matrix[rows_encoder[coin_chosen_to_save]][k] - coin_quantity) > abs(specimenB.genotype_matrix[rows_encoder[coin_chosen_to_save]][k] - coin_quantity):
                for m in range(8):
                    temp_specimen.genotype_matrix[m][k] = specimenB.genotype_matrix[m][k]
            else:
                for m in range(8):
                    temp_specimen.genotype_matrix[m][k] = specimenA.genotype_matrix[m][k]
        return temp_specimen

