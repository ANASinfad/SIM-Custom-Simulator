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


    def simulationNotFinished(self):
        if self.timeManager.instantSimulation:
            #check if the first element of the list
            return not self.timeManager.isOutOfTime(self.eventsManager.getFirstEvent().time)
        return not self.timeManager.isOutOfTime(self.timeManager.getCurrentTime())

    def getNextEvent(self):
        return self.eventsManager.getNextEvent()

    def getFirstEvent(self):
        return self.eventsManager.getFirstEvent()

    def getLastEvent (self):
        return self.eventsManager.getLastEvent()

    def eventIsInTime (self, eventTime):
        return self.timeManager.eventIsInTime(eventTime)

    def addEvent(self, event):
        # inserir esdeveniment de forma ordenada
        if len(self.eventsManager.eventList) == 0:
            self.eventsManager.eventList.append(event)
            return
        i = 0
        j = -1
        while i < len(self.eventsManager.eventList) and j == -1:
            if self.timeManager.isTimeLowerThanTime(event.time, self.eventsManager.eventList[i].time):
                j = i
            else:
                i += 1
        self.eventsManager.eventList.insert(j, event)
