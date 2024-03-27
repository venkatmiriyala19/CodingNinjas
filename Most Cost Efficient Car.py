from os import *
from sys import *
from collections import *
from math import *

'''
    --------------------------- Car class for reference ---------------------------

    class Car:
        def __init__(self,priceOfCar,maintenanceCostPerMonth,numberOfkilemeterCarRunInOneLiter,pricePerLiter,numberOfKilometerCarRunInaMonth):
            self.priceOfCar=priceOfCar
            self.maintenanceCostPerMonth=maintenanceCostPerMonth
            self.numberOfkilemeterCarRunInOneLiter=numberOfkilemeterCarRunInOneLiter
            self.pricePerLiter=pricePerLiter
            self.numberOfKilometerCarRunInaMonth=numberOfKilometerCarRunInaMonth
'''

def mostCostEfficientCar(petrolCar, dieselCar):
    A=petrolCar.priceOfCar+petrolCar.maintenanceCostPerMonth*6+petrolCar.pricePerLiter/petrolCar.numberOfkilemeterCarRunInOneLiter*petrolCar.numberOfKilometerCarRunInaMonth*6
    B=dieselCar.priceOfCar+dieselCar.maintenanceCostPerMonth*6+dieselCar.pricePerLiter/dieselCar.numberOfkilemeterCarRunInOneLiter*dieselCar.numberOfKilometerCarRunInaMonth*6
    if A>B:
        return 1
    if A==B:
        return -1
    return 0
    # Write your code here.
    pass
