
from Elevator import *
from SimulatorManager import SimulatorManager
from simulationEvents.Event import Event
from simulationEvents.EventsManager import EventStatus


class ElevatorIdleEvent(Event):
    def __init__(self, simulatorManager: SimulatorManager, entity, time):
        super().__init__(simulatorManager, entity, ElevatorState.IDLE, time)

    def treatEvent(self):
        if self.entity.state == ElevatorState.ENTITY_TRANSFER:
            self.entity.setElevatorState(ElevatorState.IDLE)
            print (self.entity.name, "idle at ", self.time)
            return EventStatus.TREATED
        return EventStatus.PENDING