import random

from numpy import random

from Elevator import TransitionsEnum, ElevatorState
from Pis import *
from SimulatorManager import SimulatorManager
from simulationEvents.ElevatorMovingEvent import ElevatorMovingEvent
from simulationEvents.Event import Event


class EntityGenerator:
    CONST_SPWAN_TIME = 60

    def __init__(self, simulationManager: SimulatorManager, numberOfLevels: int):
        self.entitiesGenerated = 0
        self.numberOfLevels = numberOfLevels
        self.simulationManager = simulationManager

    def generateEntity(self, currentTime):
        nextArrival = int(round(random.exponential(5*1000)))
        level = random.randint(0, self.numberOfLevels - 1)
        print("entity Generated at ", currentTime)
        newEvent = Event(self.simulationManager, Pis(level), PisState.NOT_EMPTY, nextArrival + currentTime)
        if level % 2 == 0:
            if self.simulationManager.elevators[0].state == ElevatorState.IDLE:
                self.simulationManager.eventsManager.afegirEsdeveniment(ElevatorMovingEvent(self.simulationManager, self.simulationManager.elevators[0], currentTime, level))
        else:
            if self.simulationManager.elevators[1].state == ElevatorState.IDLE:
                self.simulationManager.eventsManager.afegirEsdeveniment(ElevatorMovingEvent(self.simulationManager, self.simulationManager.elevators[1], currentTime, level))

        return newEvent
