from population import Population
import numpy as np
amount_of_species = 100
available_values = [1, 2, 5, 10, 20, 50]
statistical_day = np.random.random_integers(99, size=(100))
coin_to_save = 5

population = Population(amount_of_species, statistical_day)
population.calculate_changes_for_genotypes(available_values)
population.rank()
population.calculate_cost_for_sorted_population(coin_to_save)

population.show_sorted_population_and_cost()
print("\n\n")
for i in range(100):
    population.cross(coin_to_save, amount_of_species)
    population.mutate(coin_to_save, available_values)
    population.calculate_cost(coin_to_save)
    population.rank()
    population.calculate_cost_for_sorted_population(coin_to_save)
    print("Iteration ", i)
    print(min(population.cost_matrix))

population.show_sorted_population_and_cost()






