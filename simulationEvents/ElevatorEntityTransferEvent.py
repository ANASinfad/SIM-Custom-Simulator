from numpy import random

from Elevator import *
from SimulatorManager import SimulatorManager
from simulationEvents.ElevatorBrokenEvent import ElevatorBrokenEvent
from simulationEvents.ElevatorIdleEvent import ElevatorIdleEvent
from simulationEvents.Event import Event
from simulationEvents.EventsManager import EventStatus


class ElevatorEntityTransferEvent(Event):
    def __init__(self, simulatorManager: SimulatorManager, entity, time):
        super().__init__(simulatorManager, entity, ElevatorState.ENTITY_TRANSFER, time)

    def treatEvent(self):
        entityTransferTime = int(round(random.exponential(3 * 1000)))
        if self.entity.state == ElevatorState.MOVING:
            self.entity.setElevatorState(ElevatorState.ENTITY_TRANSFER)
            # release elevator entities and pick new ones
            self.entity.releaseEntities()
            self.entity.pickEntities(self.simulatorManager.floors[self.entity.getCurrentLevel()])
            # does the elevator break?
            notBreak = random.randint(0, self.entity.cyclesToBreak - 1)
            if notBreak:
                newEvent = ElevatorIdleEvent(self.simulatorManager, self.entity, entityTransferTime + self.time)
            else:
                newEvent = ElevatorBrokenEvent(self.simulatorManager, self.entity, entityTransferTime + self.time)

            self.simulatorManager.eventsManager.addEvent(newEvent)

            print(self.entity.name, "entity transfer at ", self.time)
            return EventStatus.TREATED
        return EventStatus.PENDING