from population import Population
from genotype import Genotype
import numpy as np

def cross_mc(specimen_a, specimen_b):
    specimen_c = Genotype()
    rows = 6
    col = 18
    for i in range (rows):
        for j in range (int(col/2)):
            specimen_c.genotype_matrix[i][j]=specimen_a.genotype_matrix[i][j]
    for i in range (rows):
        for j in range (int(col/2), col):
            specimen_c.genotype_matrix[i][j]=specimen_b.genotype_matrix[i][j]


    return specimen_c


amount_of_species = 10
available_values = [1, 2, 5, 10, 20, 50]
statistical_day = np.random.random_integers(99, size=(10))
coin_to_save = [2,5]
quantity_of_coins = 2          #rozmiar coin_to_save
expected_quantity_of_coins=[1,2]       #oczekiwana ilosc wydanych nominalow ktore chcemy zachowac

population = Population(amount_of_species, statistical_day)
population.calculate_changes_for_specimens(available_values)
population.rank()
population.calculate_cost(coin_to_save, quantity_of_coins,expected_quantity_of_coins)
population.show_sorted_population_and_cost()
print("\n\n")
spec = Genotype()

spec = cross_mc(population.population[0], population.population[1])
print (spec.genotype_matrix)

for i in range(10):
    population.cross(coin_to_save, amount_of_species)
    population.calculate_cost(coin_to_save, quantity_of_coins,expected_quantity_of_coins)
    population.rank()
    population.calculate_cost_matrix_for_sorted_population()
    print("Iteration ", i)
    print(min(population.cost_matrix))

population.show_sorted_population_and_cost()









