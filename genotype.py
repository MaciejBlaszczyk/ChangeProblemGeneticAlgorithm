import numpy as np
from Encoders import *


class Genotype:

    def __init__(self):
        self.number_of_ways_to_give_change = 18
        self.number_of_used_bankotes_and_coins = 6
        self.genotype_matrix = np.zeros((self.number_of_used_bankotes_and_coins, self.number_of_ways_to_give_change))
        self.cost = 0

    def calculate_change_randomly(self, statistical_day, available_coins):
        for value_to_divide in statistical_day:
            unity, tens = 0, 0
            if value_to_divide > 9:
                unity = value_to_divide % 10
                tens = int(value_to_divide / 10) * 10
            else:
                unity = value_to_divide

            temp = 0
            if value_to_divide > 9:
                while temp != tens:
                    generated_value = np.random.choice(available_coins)
                    if temp + generated_value <= tens:
                        temp = temp + generated_value
                        self.genotype_matrix[rows_encoder[generated_value]][cols_encoder[tens]] += 1

            temp = 0
            while temp != unity:
                generated_value = np.random.choice(available_coins[0:3])
                if temp + generated_value <= unity:
                    temp = temp + generated_value
                    self.genotype_matrix[rows_encoder[generated_value]][cols_encoder[unity]] += 1

    def calculate_cost(self, coins_to_save, expected_quantity_of_coins):
        value_of_rows = np.zeros(len(coins_to_save))
        difference = np.zeros(len(coins_to_save))
        for i in range(len(coins_to_save)):
            value_of_rows[i] = sum(self.genotype_matrix[rows_encoder[coins_to_save[i]]])
            difference[i] = abs(value_of_rows[i] - expected_quantity_of_coins[i])
        self.cost = sum(difference)
        return self.cost
