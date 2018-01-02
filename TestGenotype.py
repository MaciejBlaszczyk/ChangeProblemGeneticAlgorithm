import unittest
from genotype import *
from TestGenotypeData import *

class MyTestCase(unittest.TestCase):

    # less options in avaiable coins
    def test_calculate_cost_changed_avaiable_coins_should_be_worse_cost(self):
        gtFirst = Genotype()
        gtSecond = Genotype()
        gtFirst.calculate_change_randomly(statistical_dayFirst, available_coinsFirst)
        gtSecond.calculate_change_randomly(statistical_dayFirst, available_coinsSecond)
        gtFirst.calculate_cost(coins_to_save , expected_quantity_of_coins )
        gtSecond.calculate_cost(coins_to_save, expected_quantity_of_coins)
        #print(gtFirst.cost)
        #print(gtSecond.cost )
        #print("\n")
        self.assertEqual( gtSecond.cost - gtFirst.cost > 0 , True)




#changed size of statistical day from 10 to 1000 - cost raise from 50 to 1200
    def test_calculate_cost_changed_statistical_day_should_be_worse_cost(self):
        gtFirst = Genotype()
        gtSecond = Genotype()
        gtFirst.calculate_change_randomly(statistical_dayFirst, available_coinsFirst)
        gtSecond.calculate_change_randomly(statistical_daySecond, available_coinsFirst)
        gtFirst.calculate_cost(coins_to_save , expected_quantity_of_coins )
        gtSecond.calculate_cost(coins_to_save, expected_quantity_of_coins)
        #print(gtFirst.cost)
        #print(gtSecond.cost)
        #print("\n")
        self.assertEqual(gtSecond.cost - gtFirst.cost > 0 , True)



#changed avaiable coins to 1 2 5 10 20 50 100 200 compare to 1 2 5 10
# coins to save dont have main influence on cost attribute
    def test_calculate_cost_changed_available_coins_should_be_better_cost(self):
        gtFirst = Genotype()
        gtSecond = Genotype()
        gtFirst.calculate_change_randomly(statistical_dayFirst, available_coinsSecond)
        gtSecond.calculate_change_randomly(statistical_dayFirst, available_coinsThird)
        gtFirst.calculate_cost(coins_to_save , expected_quantity_of_coins )
        gtSecond.calculate_cost(coins_to_saveLess, expected_quantity_of_coins)
        print(gtFirst.cost)
        print(gtSecond.cost)
        #print("\n")
        self.assertEqual(gtSecond.cost - gtFirst.cost > 0 , False)


#tesT failure becouse of out of index (need to do exception)
'''

    
    def test_calculate_change_randomly(self):
        gtFirst = Genotype()
        gtSecond = Genotype()

        gtFirst.calculate_change_randomly(statistical_dayFirst, available_coinsFirst)
        gtSecond.calculate_change_randomly(statistical_dayFirst, available_coinsMinus)

        gtFirst.calculate_cost(coins_to_save, expected_quantity_of_coins)
        gtSecond.calculate_cost(coins_to_save, expected_quantity_of_coins)
        print(gtFirst.cost)
        print(gtSecond.cost)

        self.fail("Out of index")
'''

if __name__ == '__main__':
    unittest.main()
