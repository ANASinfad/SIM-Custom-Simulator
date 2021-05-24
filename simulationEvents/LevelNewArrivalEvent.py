from Elevator import TransitionsEnum
from Person import Person
from Pis import Pis
from SimulatorManager import SimulatorManager
from simulationEvents.ElevatorCallEvent import ElevatorCallEvent
from simulationEvents.Event import Event
from simulationEvents.EventsManager import EventStatus


class LevelNewArrivalEvent(Event):
    def __init__(self, simulatorManager: SimulatorManager, entity, time, levelDestination, newArrivedEntity):
        super().__init__(simulatorManager, entity, TransitionsEnum.NEW_ARRIVAL, time)
        self.levelDestination = levelDestination
        self.person = newArrivedEntity

    def treatEvent(self):
        self.entity.people.append(self.person)
        if len( self.entity.people) == 1:
            self.simulatorManager.eventsManager.addEvent(ElevatorCallEvent(self.simulatorManager, self.entity, self.time, self.levelDestination))
            print(len(self.entity.people), "people in the level", self.levelDestination,  "at", self.time)
        return EventStatus.TREATED