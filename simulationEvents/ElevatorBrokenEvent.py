from numpy import random

from Elevator import *
from SimulatorManager import SimulatorManager
from simulationEvents.ElevatorFixEvent import ElevatorFixEvent
from simulationEvents.ElevatorIdleEvent import ElevatorIdleEvent
from simulationEvents.Event import Event
from simulationEvents.EventsManager import EventStatus


class ElevatorBrokenEvent(Event):
    def __init__(self, simulatorManager: SimulatorManager, entity, time):
        super().__init__(simulatorManager, entity, ElevatorState.ENTITY_TRANSFER, time)

    def treatEvent(self):
        if self.entity.state == ElevatorState.ENTITY_TRANSFER:
            self.entity.setElevatorState(ElevatorState.BROKEN)
            entityFixingTime = int(round(random.exponential(60 * 1000)))
            print(self.entity.name, "broken at at ", self.time)

            if self.simulatorManager.elevators[2].state == ElevatorState.OUT_OF_SERVICE:
                self.simulatorManager.elevators[2].setElevatorState(ElevatorState.IDLE)
                print(self.simulatorManager.elevators[2].name, " is now available at ", self.time)

            newEvent = ElevatorFixEvent(self.simulatorManager, self.entity, entityFixingTime + self.time)
            self.simulatorManager.eventsManager.addEvent(newEvent)
            return EventStatus.TREATED
        return EventStatus.PENDING