import random

from numpy import random

from Event import *
from Person import *


class EntityGenerator:
    CONST_SPWAN_TIME = 60

    def __init__(self):
        self.entitiesGenerated = 0

    def generateEntity(self):
        nextArrival = random.exponential(30)
        newEvent = Event(Person(), TransitionsEnum.NEW_ARRIVAL, nextArrival)
        return newEvent
