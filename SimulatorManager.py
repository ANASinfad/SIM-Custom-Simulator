from Elevator import Elevator
from InputModule import InputModule
from Pis import Pis
from TimeManager import TimeManager
from simulationEvents.EventsManager import EventsManager


class SimulatorManager:
    def __init__(self):
        self.inputModule = InputModule()
        # Important to get the input before the time manager starts running
        self.eventsManager = EventsManager()
        self.timeManager = TimeManager()
        self.inputModule.showParameters()
        self.numberOfLevels = self.inputModule.numberOfLevels
        self.elevatorMovingTime = self.inputModule.ascensorTransportTime
        self.timeManager.setInstantSimulation(self.inputModule.instantSimulation)
        self.elevators = []
        self.floors = []
        for i in range(0, self.inputModule.numberOfLevels):
            self.floors.append(Pis(i + 1))

    def initElevators(self):
        self.elevators.append(Elevator("PairElevator", self.inputModule.MTF1))
        self.elevators.append(Elevator("OddElevator", self.inputModule.MTF2))
        self.elevators.append(Elevator("AuxElevator", self.inputModule.MTF3))

    # self.elevators[2].state = ElevatorState.OUT_OF_SERVICE
    def addEvent(self, newEvent):
        self.eventsManager.addEvent(newEvent)

    def simulationNotFinished(self):
        return self.timeManager.getCurrentTimeInMillis() < self.timeManager.maxTime

    def getNextEvent(self):
        return self.eventsManager.getNextEvent()

    def getFirstEvent(self):
        return self.eventsManager.getFirstEvent()

    def getLastEvent (self):
        return self.eventsManager.getLastEvent()

    def eventIsInTime (self, eventTime):
        return self.timeManager.eventIsInTime(eventTime)
