from numpy import random

from Elevator import *
from SimulatorManager import SimulatorManager
from simulationEvents.ElevatorIdleEvent import ElevatorIdleEvent
from simulationEvents.Event import Event


class ElevatorEntityTransferEvent(Event):
    def __init__(self, simulationManager: SimulatorManager, entity, time):
        super().__init__(simulationManager, entity, ElevatorState.ENTITY_TRANSFER, time)

    def treatEvent(self):
        entityTransferTime = int(round(random.exponential(3 * 1000)))
        newEvent = ElevatorIdleEvent(self.simulationManager, self.entity, entityTransferTime + self.simulationManager.timeManager.getCurrentTimeInMillis())
        self.simulationManager.eventsManager.addEvent(newEvent)
        print("entity transfer at ", self.simulationManager.timeManager.getCurrentTimeInMillis())