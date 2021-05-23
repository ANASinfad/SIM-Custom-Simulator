from numpy import random

from Elevator import Elevator, ElevatorState
from SimulatorManager import SimulatorManager
from simulationEvents.ElevatorEntityTransferEvent import ElevatorEntityTransferEvent
from simulationEvents.Event import Event


class ElevatorMovingEvent(Event):
    def __init__(self, simulationManager: SimulatorManager, entity, time, levelDestination):
        super().__init__(simulationManager, entity, ElevatorState.MOVING, time)
        self.levelDestination = levelDestination

    def treatEvent(self):
        #cast the entity to elevator
        elevator = Elevator(self.entity)
        elevator.setElevatorState(ElevatorState.MOVING)
        levelDestination = random.randint(0, self.simulationManager.numberOfLevels - 1)
        if elevator == self.simulationManager.elevators[0]:
            if levelDestination % 2 == 1:
                if levelDestination != self.simulationManager.numberOfLevels:
                    levelDestination -= 1
                else:
                    levelDestination += 1
        elif elevator == self.simulationManager.elevators[1]:
            if levelDestination % 2 == 0:
                if levelDestination == self.simulationManager.numberOfLevels:
                    levelDestination -= 1
                else:
                    levelDestination += 1

        levelsToMove = abs(elevator.currentLevel - levelDestination)
        timeToMove = levelsToMove * self.simulationManager.elevatorMovingTime * 1000
        self.simulationManager.eventsManager.addEvent(ElevatorEntityTransferEvent(self.simulationManager, self.entity, self.simulationManager.timeManager.getCurrentTimeInMillis() + timeToMove))
        print("elevator starts moving at ", self.simulationManager.timeManager.getCurrentTimeInMillis(), " for ", timeToMove, " ms")