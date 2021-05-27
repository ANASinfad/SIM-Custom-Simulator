from numpy import random

from Elevator import *
from SimulatorManager import SimulatorManager
from simulationEvents.ElevatorIdleEvent import ElevatorIdleEvent
from simulationEvents.ElevatorOutOfServiceEvent import ElevatorOutOfServiceEvent
from simulationEvents.Event import Event
from simulationEvents.EventsManager import EventStatus


class ElevatorFixEvent(Event):
    def __init__(self, simulatorManager: SimulatorManager, entity, time):
        super().__init__(simulatorManager, entity, ElevatorState.ENTITY_TRANSFER, time)

    def treatEvent(self):
        if self.entity.state == ElevatorState.BROKEN:
            self.entity.setElevatorState(ElevatorState.IDLE, self.time)
            print(self.entity.name, "fixed at ", self.time.getDateAsString())
            if self.simulatorManager.elevators[0].state != ElevatorState.BROKEN and \
                    self.simulatorManager.elevators[1].state != ElevatorState.BROKEN:
                newEvent = ElevatorOutOfServiceEvent(self.simulatorManager, self.simulatorManager.elevators[2],
                                                     self.time)
                self.simulatorManager.addEvent(newEvent)

            return EventStatus.TREATED
        return EventStatus.PENDING