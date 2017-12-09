from population import Population
import numpy as np
from matplotlib import pyplot as plt
from multiprocessing import Process, Array


def execute_algorithm(pop, mutate_flag, pop_history):
    counter = 0
    while min(pop.cost_matrix) > required_cost and counter < 200:
        pop.calculate_cost_for_population(coins_to_save, expected_quantity_of_coins)
        pop.rank()
        pop.calculate_cost_matrix_for_sorted_population()
        pop.cross_and_choose_new_population_randomly_from_crossed_specimens(amount_of_species)
        if mutate_flag is True:
            pop.mutate(available_coins)

        print("Iteration ", counter)
        print(min(pop.cost_matrix))
        pop_history[counter] = min(pop.cost_matrix)
        counter += 1


amount_of_species = 100
available_coins = [1, 2, 5, 10, 20, 50]
statistical_day = np.random.random_integers(99, size=100)
required_cost = sum(statistical_day) / 100
coins_to_save = [2, 5]
expected_quantity_of_coins = [30, 15]


population1 = Population(amount_of_species, statistical_day, coins_to_save, Population.cross_by_choosing_the_best_values)
population1.calculate_changes_for_specimens(available_coins)
population2 = Population(amount_of_species, statistical_day, coins_to_save, Population.cross_mc)
population2.calculate_changes_for_specimens(available_coins)
population3 = Population(amount_of_species, statistical_day, coins_to_save, Population.cross_by_choosing_the_best_values)
population3.calculate_changes_for_specimens(available_coins)
population4 = Population(amount_of_species, statistical_day, coins_to_save, Population.cross_mc)
population4.calculate_changes_for_specimens(available_coins)


if __name__ == '__main__':
    population1_history = Array('d', [0 for _ in range(200)])
    population2_history = Array('d', [0 for _ in range(200)])
    population3_history = Array('d', [0 for _ in range(200)])
    population4_history = Array('d', [0 for _ in range(200)])
    jobs = list()
    jobs.append(Process(target=execute_algorithm, args=(population1, True, population1_history)))
    jobs.append(Process(target=execute_algorithm, args=(population2, True, population2_history)))
    jobs.append(Process(target=execute_algorithm, args=(population3, False, population3_history)))
    jobs.append(Process(target=execute_algorithm, args=(population4, False, population4_history)))
    [j.start() for j in jobs]
    [j.join() for j in jobs]

    plt.figure()
    plt.plot(range(len(population1_history)), population1_history, label='intelligent crossing + mutating')
    plt.plot(range(len(population2_history)), population2_history, label='random crossing + mutating')
    plt.plot(range(len(population3_history)), population3_history, label='intelligent crossing')
    plt.plot(range(len(population4_history)), population4_history, label='random crossing')
    plt.axis((0, 200, required_cost, 400))
    plt.legend()
    plt.show()


