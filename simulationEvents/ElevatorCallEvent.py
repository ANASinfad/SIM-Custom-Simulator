from Elevator import Elevator, ElevatorState, TransitionsEnum
from SimulatorManager import SimulatorManager
from simulationEvents.ElevatorMovingEvent import ElevatorMovingEvent
from simulationEvents.Event import Event
from simulationEvents.EventsManager import EventStatus


class ElevatorCallEvent(Event):
    def __init__(self, simulatorManager: SimulatorManager, entity, time, levelDestination):
        super().__init__(simulatorManager, entity, TransitionsEnum.CALL, time)
        self.levelDestination = levelDestination

    def treatEvent(self):
        if self.levelDestination % 2 == 0:
            if self.simulatorManager.elevators[0].state == ElevatorState.BROKEN:
                return self.checkIfIdleAndCreateEvent(self.simulatorManager.elevators[2])

            return self.checkIfIdleAndCreateEvent(self.simulatorManager.elevators[0])
        else:
            if self.simulatorManager.elevators[1].state == ElevatorState.BROKEN:
                return self.checkIfIdleAndCreateEvent(self.simulatorManager.elevators[2])

            return self.checkIfIdleAndCreateEvent(self.simulatorManager.elevators[1])

    def checkIfIdleAndCreateEvent(self, elevator: Elevator):
        if elevator.state == ElevatorState.IDLE:
            self.simulatorManager.eventsManager.addEvent(
                ElevatorMovingEvent(self.simulatorManager, elevator,
                                    self.simulatorManager.timeManager.getCurrentTimeInMillis(), self.levelDestination))
            return EventStatus.TREATED
        else:
            return EventStatus.PENDING