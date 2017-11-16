from population import Population

amount_of_species = 100
available_values = [1, 2, 5]
statistical_day = [8, 5, 1, 5, 5,2,3,4,2,3,4,5,6,7,8,9,7,6,8,5,6,4,3,2,5,4,6,7,8,5,4,6,7,3,1,2,6,8,3,4,5,8, 5, 1, 5, 5,2,3,4,2,3,4,5,6,7,8,9,7,6,8,5,6,4,3,2,5,4,6,7,8,5,4,6,7,3,1,2,6,8,3,4,5,8, 5, 1, 5, 5,2,3,4,2,3,4,5,6,7,8,9,7,6,8,5,6,4,3,2,5,4,6,7,8,5,4,6,7,3,1,2,6,8,3,4,5]
coin_to_save = 2

population = Population(amount_of_species, statistical_day)
population.calculate_changes_for_genotypes(available_values)
population.rank()
population.calculate_cost_for_sorted_population(coin_to_save)

for i in range(10):
    population.cross(coin_to_save, amount_of_species)
    population.calculate_cost(coin_to_save)
    population.rank()
    population.calculate_cost_for_sorted_population(coin_to_save)
    print("Iteration ", i)
    print(min(population.cost_matrix))

#population.show_sorted_population_and_cost()





