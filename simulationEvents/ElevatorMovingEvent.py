from numpy import random

from Elevator import Elevator, ElevatorState
from SimulatorManager import SimulatorManager
from TimeManager import SimulationTime
from simulationEvents.ElevatorEntityTransferEvent import ElevatorEntityTransferEvent
from simulationEvents.Event import Event
from simulationEvents.EventsManager import EventStatus


class ElevatorMovingEvent(Event):
    def __init__(self, simulatorManager: SimulatorManager, entity, time: SimulationTime, levelDestination):
        super().__init__(simulatorManager, entity, ElevatorState.MOVING, time)
        self.levelDestination = levelDestination

    def treatEvent(self):
        #cast the entity to elevator
        if (self.entity.state == ElevatorState.IDLE):
            self.entity.setElevatorState(ElevatorState.MOVING, self.time)

            levelsToMove = abs(self.entity.currentLevel - self.levelDestination)
            secondsToMove = abs(levelsToMove * self.simulatorManager.elevatorMovingTime)
            minutesToMove = int(secondsToMove / 60)
            secondsToMove = secondsToMove % 60

            # once the elevator starts moving, we consider it will reach the level destination
            self.entity.setCurrentLevel(self.levelDestination)
            self.simulatorManager.addEvent(ElevatorEntityTransferEvent(
                self.simulatorManager, self.entity, self.simulatorManager.timeManager.addTime(
                    self.time, secondsToMove, minutesToMove, 0, 0, 0, 0)))
            print(self.entity.name, "starts moving at ", self.time.getDateAsString(), " for ", secondsToMove, " seconds to", self.levelDestination)
            return EventStatus.TREATED
        return EventStatus.PENDING