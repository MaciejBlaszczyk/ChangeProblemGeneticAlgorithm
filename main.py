from population import Population
from genotype import Genotype
import numpy as np


amount_of_species = 10
available_values = [1, 2, 5, 10, 20, 50]
statistical_day = np.random.random_integers(99, size=(10))
coin_to_save = [2,10]
quantity_of_coins = 2          #rozmiar coin_to_save
expected_quantity_of_coins=[1,2]       #oczekiwana ilosc wydanych nominalow ktore chcemy zachowac
best = Genotype()


population = Population(amount_of_species, statistical_day)
population.calculate_changes_for_specimens(available_values)
population.calculate_cost(coin_to_save, quantity_of_coins,expected_quantity_of_coins)
population.rank()
population.show_sorted_population_and_cost()
best.genotype_matrix = population.sorted_population[0].genotype_matrix
best.cost = population.sorted_population[0].cost

print(best.cost)

print("\n\n")



for i in range(5):
    population.cross()
    population.mutate_mc()
    population.calculate_cost(coin_to_save, quantity_of_coins,expected_quantity_of_coins)
    population.rank()
    population.calculate_cost_matrix_for_sorted_population()
    print("Iteration ", i)
    print(min(population.cost_matrix))
    if best.cost > population.sorted_population[0].cost:
        best.genotype_matrix = population.sorted_population[0].genotype_matrix
        best.cost = population.sorted_population[0].cost



print("\n\n")
print(("BEST:"))
print(best.genotype_matrix)
print("cost:",best.cost)










