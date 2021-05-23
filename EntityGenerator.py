import random

from numpy import random

from Elevator import ElevatorState
from Person import Person
from Pis import *
from SimulatorManager import SimulatorManager
from simulationEvents.ElevatorMovingEvent import ElevatorMovingEvent
from simulationEvents.Event import Event


class EntityGenerator:
    CONST_SPWAN_TIME = 60

    def __init__(self, simulationManager: SimulatorManager):
        self.entitiesGenerated = 0
        self.numberOfLevels = len(simulationManager.floors)
        self.simulationManager = simulationManager

    def generateEntity(self):
        nextArrival = int(round(random.exponential(5 * 1000)))
        level = random.randint(0, self.numberOfLevels - 1)
        print("entity generated," + str(self.simulationManager.timeManager.getCurrentTimeInMillis()))
        if level % 2 == 0:
            if self.simulationManager.elevators[0].state == ElevatorState.IDLE:
                newEvent = Event(Person(), self.simulationManager.elevators[0].getCallEvent(),
                                 nextArrival + self.simulationManager.timeManager.getCurrentTimeInMillis())
                self.simulationManager.addEvent(newEvent)
        else:
            if self.simulationManager.elevators[1].state == ElevatorState.IDLE:
                newEvent = Event(Person(), self.simulationManager.elevators[1].getCallEvent(),
                                 nextArrival + self.simulationManager.timeManager.getCurrentTimeInMillis())
                self.simulationManager.addEvent(newEvent)
