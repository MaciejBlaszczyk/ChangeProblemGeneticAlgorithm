from population import Population
import numpy as np
from matplotlib import pyplot as plt


amount_of_species = 100
available_coins = [1, 2, 5, 10, 20, 50]
statistical_day = np.random.random_integers(99, size=100)
required_cost = sum(statistical_day) / 100
coins_to_save = [2, 5]
expected_quantity_of_coins = [30, 15]


population1 = Population(amount_of_species, statistical_day, coins_to_save, Population.cross_by_choosing_the_best_values)
population1.calculate_changes_for_specimens(available_coins)
population1_history = []
population2 = Population(amount_of_species, statistical_day, coins_to_save, Population.cross_mc)
population2.calculate_changes_for_specimens(available_coins)
population2_history = []


counter = 0
while min(population1.cost_matrix) > required_cost and counter < 200:
    population1.calculate_cost_for_population(coins_to_save, expected_quantity_of_coins)
    population1.rank()
    population1.calculate_cost_matrix_for_sorted_population()
    population1.cross_and_choose_new_population_randomly_from_crossed_specimens(amount_of_species)
    population1.mutate(available_coins)

    print("Iteration ", counter)
    print(min(population1.cost_matrix))
    population1_history.append(min(population1.cost_matrix))
    counter += 1


counter = 0
while min(population2.cost_matrix) > required_cost and counter < 200:
    population2.calculate_cost_for_population(coins_to_save, expected_quantity_of_coins)
    population2.rank()
    population2.calculate_cost_matrix_for_sorted_population()
    population2.cross_and_choose_new_population_randomly_from_crossed_specimens(amount_of_species)
    population2.mutate(available_coins)

    print("Iteration ", counter)
    print(min(population2.cost_matrix))
    population2_history.append(min(population2.cost_matrix))
    counter += 1

plt.figure()
plt.plot(range(len(population1_history)), population1_history, label='intelligent crossing')
plt.plot(range(len(population2_history)), population2_history, label='random crossing')
plt.axis((0, 200, required_cost, 400))
plt.legend()
plt.show()







