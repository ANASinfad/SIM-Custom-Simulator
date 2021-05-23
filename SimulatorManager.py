from Elevator import Elevator
from InputModule import InputModule
from Pis import Pis
from TimeManager import TimeManager
from simulationEvents.EventsManager import EventsManager


class SimulatorManager:
    def __init__(self):
        self.eventsManager = EventsManager()
        self.timeManager = TimeManager()
        self.inputModule = InputModule()
        self.inputModule.showParameters()

        self.elevators = []
        self.floors = []
        for i in range(0, self.inputModule.numberOfLevels):
            self.floors.append(Pis(i + 1))

    def initElevators(self):
        self.elevators.append(Elevator(self.inputModule.MTF1))
        self.elevators.append(Elevator(self.inputModule.MTF2))
        self.elevators.append(Elevator(self.inputModule.MTF3))

    # self.elevators[2].state = ElevatorState.OUT_OF_SERVICE
    def addEvent(self, newEvent):
        self.eventsManager.addEvent(newEvent)

    def simulationNotFinished(self):
        return self.timeManager.getCurrentTimeInMillis() < self.timeManager.maxTime

    def getNextEvent(self):
        return self.eventsManager.getNextEvent()


