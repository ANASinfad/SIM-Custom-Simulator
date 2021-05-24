from numpy import random

from Elevator import Elevator, ElevatorState
from SimulatorManager import SimulatorManager
from simulationEvents.ElevatorEntityTransferEvent import ElevatorEntityTransferEvent
from simulationEvents.Event import Event
from simulationEvents.EventsManager import EventStatus


class ElevatorMovingEvent(Event):
    def __init__(self, simulatorManager: SimulatorManager, entity, time, levelDestination):
        super().__init__(simulatorManager, entity, ElevatorState.MOVING, time)
        self.levelDestination = levelDestination

    def treatEvent(self):
        #cast the entity to elevator
        if (self.entity.state == ElevatorState.IDLE):
            self.entity.setElevatorState(ElevatorState.MOVING)

            levelsToMove = abs(self.entity.currentLevel - self.levelDestination)
            timeToMove = levelsToMove * self.simulatorManager.elevatorMovingTime * 1000

            # once the elevator starts moving, we consider it will reach the level destination
            self.entity.setCurrentLevel(self.levelDestination)
            self.simulatorManager.eventsManager.addEvent(ElevatorEntityTransferEvent(self.simulatorManager, self.entity, self.time + timeToMove))
            print(self.entity.name, "starts moving at ", self.time, " for ", timeToMove, " ms to", self.levelDestination)
            return EventStatus.TREATED
        return EventStatus.PENDING