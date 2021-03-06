from population import Population
import numpy as np
from matplotlib import pyplot as plt
from multiprocessing import Process, Array


def execute_algorithm(pop, pop_history):
    counter = 0
    while min(pop.cost_matrix) > required_cost and counter < max_iterations:
        pop.calculate_cost_for_population()
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
statistical_day = np.random.random_integers(499, size=100)
required_cost = sum(statistical_day) / 1000
coins_to_save = [2, 5, 20, 100]
expected_quantity_of_coins = [50, 25, 20, 10]
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


if __name__ == '__main__':

    for m in mutations:
        for cf in cross_functions:
            for mf in mutate_functions:
                populations.append(Population(amount_of_species, statistical_day, coins_to_save, cf, mf, m, expected_quantity_of_coins))
                print("Creating new population")
                populations[-1].calculate_changes_for_specimens(available_coins)
                if not m:
                    break

    populations_history = list()
    jobs = list()
    [populations_history.append(Array('d', [0 for _ in range(max_iterations)])) for i in range(6)]
    [jobs.append(Process(target=execute_algorithm, args=(populations[i], populations_history[i]))) for i in range(6)]
    [j.start() for j in jobs]
    [j.join() for j in jobs]

    plt.figure()
    [plt.plot(range(len(populations_history[i])), populations_history[i], label=lab) for i, lab in zip(range(6), labels)]
    plt.axis((0, max_iterations, required_cost, 1200))
    plt.legend()
    plt.show()


