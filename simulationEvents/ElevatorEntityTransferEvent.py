from numpy import random

from Elevator import *
from SimulatorManager import SimulatorManager
from TimeManager import SimulationTime
from simulationEvents.ElevatorBrokenEvent import ElevatorBrokenEvent
from simulationEvents.ElevatorIdleEvent import ElevatorIdleEvent
from simulationEvents.Event import Event
from simulationEvents.EventsManager import EventStatus


class ElevatorEntityTransferEvent(Event):
    def __init__(self, simulatorManager: SimulatorManager, entity, time: SimulationTime):
        super().__init__(simulatorManager, entity, ElevatorState.ENTITY_TRANSFER, time)

    def treatEvent(self):
        #seconds
        if self.entity.state == ElevatorState.MOVING:

            entityTransferTime = int(round(random.exponential(3)))
            eventTime = self.simulatorManager.timeManager.addTime(
                                                 self.time, entityTransferTime, 0, 0, 0, 0, 0)

            self.entity.setElevatorState(ElevatorState.ENTITY_TRANSFER, self.time)
            # release elevator entities and pick new ones
            self.entity.releaseEntities()
            self.entity.pickEntities(self.simulatorManager.floors[self.entity.getCurrentLevel()])
            self.entity.cycleCompleted()
            # does the elevator break?
            notBreak = random.randint(0, self.entity.cyclesToBreak - 1)
            if notBreak:
                newEvent = ElevatorIdleEvent(self.simulatorManager, self.entity, eventTime)
            else:
                newEvent = ElevatorBrokenEvent(self.simulatorManager, self.entity, eventTime)

            self.simulatorManager.addEvent(newEvent)

            print(self.entity.name, "entity transfer at ", self.time.getDateAsString())
            return EventStatus.TREATED
        return EventStatus.PENDING