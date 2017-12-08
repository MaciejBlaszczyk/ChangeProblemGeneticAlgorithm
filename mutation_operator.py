from genotype import Genotype
import numpy as np

def mutation_mc(specimen):
    row = 6
    col = 18
    tmp = Genotype()
    mut = np.random.choice(col)
    for i in range(row):
        specimen.genotype_matrix[i][mut] = tmp.genotype_matrix[i][mut]

