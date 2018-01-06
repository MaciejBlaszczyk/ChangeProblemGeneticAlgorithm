from population import Population
import numpy as np
from matplotlib import pyplot as plt
from multiprocessing import Process, Array


def execute_algorithm(pop, pop_history):
    counter = 0
    while min(pop.cost_matrix) > required_cost and counter < max_iterations:
        pop.calculate_cost_for_population(coins_to_save, expected_quantity_of_coins)
        pop.rank()
        pop.calculate_cost_matrix_for_sorted_population()
        pop.cross_and_choose_new_population_randomly_from_crossed_specimens(amount_of_species)
        if pop.mutation:
            pop.mutate(available_coins)

        print("Iteration ", counter)
        print(min(pop.cost_matrix))
        pop_history[counter] = min(pop.cost_matrix)
        counter += 1


amount_of_species = 100
available_coins = [1, 2, 5, 10, 20, 50, 100, 200]
statistical_day = np.random.random_integers(499, size=10)
required_cost = sum(statistical_day) / 1000
coins_to_save = [2, 5, 20, 100]
expected_quantity_of_coins = [50, 25, 20, 10]
max_iterations = 20
initial_number_of_coins = [60, 1000, 1000, 1000, 1000, 500, 500, 500]


pop = Population(amount_of_species, statistical_day, coins_to_save, Population.cross_by_choosing_the_best_values, Population.mutate_randomly, True,initial_number_of_coins,expected_quantity_of_coins)
pop.calculate_changes_for_specimens( available_coins)
pop.first_good(initial_number_of_coins, expected_quantity_of_coins, coins_to_save)
for i in range(max_iterations):
    pop.calculate_cost_for_population(coins_to_save, expected_quantity_of_coins,initial_number_of_coins)
    pop.rank()
    pop.calculate_cost_matrix_for_sorted_population()
    pop.cross_and_choose_new_population_randomly_from_crossed_specimens(amount_of_species)
    if pop.mutation:
        pop.mutate(available_coins)
    pop.is_good(initial_number_of_coins, expected_quantity_of_coins, coins_to_save)
    print("Iteration ", i)
    print(min(pop.cost_matrix))


if pop.good ==1:
    print("\nNajlepszy osobnik spełniajacy wymagania\n\n")
    print(pop.best_possible_specimen.genotype_matrix)
    print("best:", pop.best_possible_specimen.cost)
else:
    print("Nie powstał osobnik spełniajacy wymagania")
