from population import Population
import numpy as np
from matplotlib import pyplot as plt
from multiprocessing import Process, Array


def execute_algorithm(pop, pop_history):
    counter = 0
    while min(pop.cost_matrix) > required_cost and counter < 200:
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
available_coins = [1, 2, 5, 10, 20, 50]
statistical_day = np.random.random_integers(99, size=100)
required_cost = sum(statistical_day) / 100
coins_to_save = [2]
expected_quantity_of_coins = [0]
max_iterations = 200

cross_functions = [Population.cross_by_choosing_the_best_values, Population.cross_mc]
mutate_functions = [Population.mutate_by_replacing_usage_of_important_coin_with_other_coins, Population.mutate_randomly]
mutations = [True, False]
labels = ["Intelligent Crossing + Intelligent Mutating",
          "Intelligent Crossing + Randomly Mutating",
          "Random Crossing + Intelligent Mutating",
          "Random Crossing + Random Mutating",
          "Intelligent Crossing + No Mutating",
          "Random Crossing + No Mutating"]
populations = []

for m in mutations:
    for cf in cross_functions:
        for mf in mutate_functions:
            populations.append(Population(amount_of_species, statistical_day, coins_to_save, cf, mf, m))
            populations[-1].calculate_changes_for_specimens(available_coins)
            if not m:
                break


if __name__ == '__main__':
    populations_history = list()
    jobs = list()
    [populations_history.append(Array('d', [0 for _ in range(max_iterations)])) for i in range(6)]
    [jobs.append(Process(target=execute_algorithm, args=(populations[i], populations_history[i]))) for i in range(6)]
    [j.start() for j in jobs]
    [j.join() for j in jobs]

    plt.figure()
    [plt.plot(range(len(populations_history[i])), populations_history[i], label=lab) for i, lab in zip(range(6), labels)]
    plt.axis((0, max_iterations, required_cost, 450))
    plt.legend()
    plt.show()


