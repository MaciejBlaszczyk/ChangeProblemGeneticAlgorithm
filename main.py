from population import Population
import numpy as np
amount_of_species = 10
available_values = [1, 2, 5, 10, 20, 50]
statistical_day = np.random.random_integers(9, size=(10))
coin_to_save = 2

population = Population(amount_of_species, statistical_day)
population.calculate_changes_for_specimens(available_values)
population.rank()
population.calculate_cost(coin_to_save)
population.show_sorted_population_and_cost()
print("\n\n")

for i in range(10):
    population.cross(coin_to_save, amount_of_species)
    population.mutate(coin_to_save, available_values)
    population.calculate_cost(coin_to_save)
    population.rank()
    population.calculate_cost_matrix_for_sorted_population()
    print("Iteration ", i)
    print(min(population.cost_matrix))

population.show_sorted_population_and_cost()






