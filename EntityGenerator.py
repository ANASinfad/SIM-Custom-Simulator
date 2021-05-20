import random

from numpy import random
from Person import *
from Event import *


class EntityGenerator:
    CONST_SPAWN_PROBABILTY = 0.5
    CONST_SPWAN_TIME = 60

    def __init__(self):
        self.entitiesGenerated = 0

    def generateEntity(self, currentTime):
        self.entitiesGenerated = random.exponential() % 1
        if self.entitiesGenerated > self.CONST_SPAWN_PROBABILTY:
            print(self.entitiesGenerated)
            currentTime += self.CONST_SPAWN_PROBABILTY * self.CONST_SPWAN_TIME
            newEvent = Event(Person(), TransitionsEnum.NEW_ARRIVAL, currentTime)
            return newEvent
        return None
