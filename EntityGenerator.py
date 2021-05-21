import random

from numpy import random

from Event import *
from Person import *
from Pis import *


class EntityGenerator:
    CONST_SPWAN_TIME = 60

    def __init__(self, numberOfLevels: int):
        self.entitiesGenerated = 0
        self.numberOfLevels = numberOfLevels

    def generateEntity(self, currentTime):
        nextArrival = int(round(random.exponential(10*1000)))
        level = random.randint(0, self.numberOfLevels - 1)
        newEvent = Event(Pis(5), TransitionsEnum.NEW_ARRIVAL, nextArrival + currentTime)
        print("next event in: ", nextArrival/1000, "seconds, in the level ", level)

        return newEvent
