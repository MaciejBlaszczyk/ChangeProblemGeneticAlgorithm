import numpy as np


class Genotype:

    def __init__(self):
        self.genotype_matrix = np.zeros((3, 9))
        self.cost = 0
        self.rows_encoder = {1: 0,
                        2: 1,
                        5: 2}
        self.cols_encoder = {1: 0,
                        2: 1,
                        3: 2,
                        4: 3,
                        5: 4,
                        6: 5,
                        7: 6,
                        8: 7,
                        9: 8}

    def calculate_change_randomly(self, statistical_day, available_values):
        for value_to_divide in statistical_day:
            temp = 0
            while temp != value_to_divide:
                generated_value = np.random.choice(available_values)
                if temp + generated_value <= value_to_divide:
                    temp = temp + generated_value
                    self.genotype_matrix[self.rows_encoder[generated_value]][self.cols_encoder[value_to_divide]] += 1

    def calculate_cost(self, coin_to_save):
        self.cost = sum(self.genotype_matrix[self.rows_encoder[coin_to_save]])
        return self.cost



