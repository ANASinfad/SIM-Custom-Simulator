import random

from numpy import random

from Person import Person
from SimulatorManager import SimulatorManager
from simulationEvents.LevelNewArrivalEvent import LevelNewArrivalEvent


class EntityGenerator:
    CONST_SPWAN_TIME = 60

    def __init__(self, simulatorManager: SimulatorManager):
        self.entitiesGenerated = 0
        self.numberOfLevels = len(simulatorManager.floors)
        self.simulatorManager = simulatorManager

    def generateEntity(self):
        nextArrival = int(round(random.exponential(2 * 60 * 1000)))
        level = random.randint(0, self.numberOfLevels - 1)

        newEvent = LevelNewArrivalEvent(self.simulatorManager, self.simulatorManager.floors[level],
                                        nextArrival + self.simulatorManager.timeManager.getCurrentTimeInMillis(), level, Person(self.entitiesGenerated))
        self.entitiesGenerated += 1

        self.simulatorManager.addEvent(newEvent)
