import numpy as np

available_coinsFirst  = [1, 2, 5, 10, 20, 50]
available_coinsSecond  = [1, 2, 5, 10]
available_coinsThird = [1, 2, 5, 10, 20, 50, 100, 200]
available_coinsMinus = [1, 2, 5, -10]

statistical_dayFirst = np.random.random_integers(499, size=10)
statistical_daySecond = np.random.random_integers(499, size=100)


coins_to_save = [2, 5, 20, 100]
coins_to_saveLess = [2, 5, 10, 50]

expected_quantity_of_coins = [50, 25, 20, 10]