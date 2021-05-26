from numpy import random

from Elevator import *
from SimulatorManager import SimulatorManager
from TimeManager import SimulationTime
from simulationEvents.ElevatorFixEvent import ElevatorFixEvent
from simulationEvents.ElevatorIdleEvent import ElevatorIdleEvent
from simulationEvents.Event import Event
from simulationEvents.EventsManager import EventStatus


class ElevatorBrokenEvent(Event):
    def __init__(self, simulatorManager: SimulatorManager, entity, time: SimulationTime):
        super().__init__(simulatorManager, entity, ElevatorState.BROKEN, time)

    def treatEvent(self):
        if self.entity.state == ElevatorState.ENTITY_TRANSFER:
            self.entity.setElevatorState(ElevatorState.BROKEN)
            entityFixingMinutes = int(round(random.exponential(60)))
            entityFixingHours = int(entityFixingMinutes / 60)
            entityFixingMinutes = entityFixingMinutes % 60
            #minutes
            print(self.entity.name, "broken at at ",  self.time.getString(),
                  "with", self.entity.currentCycles, "cycles")

            if self.simulatorManager.elevators[2].state == ElevatorState.OUT_OF_SERVICE:
                self.simulatorManager.elevators[2].setElevatorState(ElevatorState.IDLE)
                print(self.simulatorManager.elevators[2].name, " is now available at ", self.time.getString())

            newEvent = ElevatorFixEvent(self.simulatorManager, self.entity, self.simulatorManager.timeManager.addTime(
                self.time, 0, entityFixingMinutes, entityFixingHours, 0, 0, 0))
            self.simulatorManager.addEvent(newEvent)
            return EventStatus.TREATED
        return EventStatus.PENDING