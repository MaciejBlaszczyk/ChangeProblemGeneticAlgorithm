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
