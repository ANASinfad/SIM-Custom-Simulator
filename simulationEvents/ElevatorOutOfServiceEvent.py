from numpy import random

from Elevator import *
from SimulatorManager import SimulatorManager
from simulationEvents.ElevatorIdleEvent import ElevatorIdleEvent
from simulationEvents.Event import Event
from simulationEvents.EventsManager import EventStatus


class ElevatorOutOfServiceEvent(Event):
    def __init__(self, simulatorManager: SimulatorManager, entity, time):
        super().__init__(simulatorManager, entity, ElevatorState.ENTITY_TRANSFER, time)

    def treatEvent(self):
        if self.entity.state == ElevatorState.IDLE:
            self.entity.setElevatorState(ElevatorState.OUT_OF_SERVICE)
            print(self.entity.name, "is out of service at", self.time)
            return EventStatus.TREATED
        return EventStatus.PENDING