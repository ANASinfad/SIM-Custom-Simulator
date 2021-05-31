import random

from numpy import random

from Person import Person
from SimulatorManager import SimulatorManager
from simulationEvents.LevelNewArrivalEvent import LevelNewArrivalEvent


class EntityGenerator:

    def __init__(self, simulatorManager: SimulatorManager):
        self.entitiesGenerated = 0
        self.numberOfLevels = len(simulatorManager.floors)
        self.simulatorManager = simulatorManager
        self.spawnTime = simulatorManager.inputModule.timeBetweenArrivals

    def generateFirstEntity(self):
        self.newArrivalEvent(self.simulatorManager.timeManager.getCurrentTime())

    def generateEntity(self, time):
        self.newArrivalEvent(time)

    def newArrivalEvent(self, time):
        nextArrival = int(abs(round(random.exponential(self.spawnTime))))
        level = random.randint(0, self.numberOfLevels)

        newEvent = LevelNewArrivalEvent(
            self.simulatorManager, self.simulatorManager.floors[level], self.simulatorManager.timeManager.addTime(
                        time, nextArrival, 0, 0, 0, 0, 0),
                        level, Person(self.entitiesGenerated))
        self.entitiesGenerated += 1

        self.simulatorManager.addEvent(newEvent)