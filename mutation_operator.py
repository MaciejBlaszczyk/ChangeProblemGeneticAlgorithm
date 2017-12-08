from genotype import Genotype
import numpy as np

def mutation_mc(specimen_a,specimen_b):
    row = 6
    col = 18
    mut = np.random.choice(col)
    for i in range(row):
        specimen_a.genotype_matrix[i][mut] = specimen_b.genotype_matrix[i][mut]

