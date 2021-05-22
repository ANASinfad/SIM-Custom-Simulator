
from Elevator import *
from SimulatorManager import SimulatorManager
from simulationEvents.Event import Event


class ElevatorIdleEvent(Event):
    def __init__(self, simulationManager: SimulatorManager, entity, time):
        super().__init__(simulationManager, entity, ElevatorState.IDLE, time)

    def treatEvent(self):
        elevator = Elevator(self.entity)
        elevator.setElevatorState(ElevatorState.IDLE)
        print ("elevator idle at ", self.simulationManager.timeManager.getCurrentTimeInMillis())