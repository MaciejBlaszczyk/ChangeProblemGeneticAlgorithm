import numpy as np


class Genotype:

    def __init__(self):
        self.number_of_ways_to_give_change = 18
        self.number_of_used_bankotes_and_coins = 6
        self.genotype_matrix = np.zeros((self.number_of_used_bankotes_and_coins, self.number_of_ways_to_give_change))
        self.cost = 0
        self.rows_encoder = {1: 0,
                        2: 1,
                        5: 2,
                        10: 3,
                        20: 4,
                        50: 5}
        self.cols_encoder = {1: 0,
                        2: 1,
                        3: 2,
                        4: 3,
                        5: 4,
                        6: 5,
                        7: 6,
                        8: 7,
                        9: 8,
                        10: 9,
                        20 : 10,
                        30: 11,
                        40: 12,
                        50: 13,
                        60: 14,
                        70: 15,
                        80: 16,
                        90: 17}

    def calculate_change_randomly(self, statistical_day, available_values):
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
                    generated_value = np.random.choice(available_values)
                    if temp + generated_value <= tens:
                        temp = temp + generated_value
                        self.genotype_matrix[self.rows_encoder[generated_value]][self.cols_encoder[tens]] += 1

            temp = 0
            while temp != unity:
                generated_value = np.random.choice(available_values[0:3])
                if temp + generated_value <= unity:
                    temp = temp + generated_value
                    self.genotype_matrix[self.rows_encoder[generated_value]][self.cols_encoder[unity]] += 1

    def calculate_cost(self, coin_to_save):
        self.cost = sum(self.genotype_matrix[self.rows_encoder[coin_to_save]])
        return self.cost



