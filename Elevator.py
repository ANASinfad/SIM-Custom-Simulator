import datetime
import enum

from TimeManager import SimulationTime


class ElevatorState(enum.Enum):
    IDLE = 0
    MOVING = 1
    ENTITY_TRANSFER = 2
    BROKEN = 3

    # This one only available for the 3rd elevator
    OUT_OF_SERVICE = 4


class TransitionsEnum(enum.Enum):
    REACH_DESTINATION = 0
    BREAK = 1
    FIX = 2
    DOORS_CLOSED = 3
    ONE_BROKEN = 4
    ALL_FIXED = 5
    CALL = 6
    NEW_ARRIVAL = 7


class Elevator:

    # Initialization of an elevator
    def __init__(self, name, cyclesToBreak, initialTime: SimulationTime):
        self.name = name
        self.cyclesToBreak = cyclesToBreak
        self.currentCycles = 0
        self.state = ElevatorState.IDLE
        self.currentLevel = 0
        self.people = []
        self.timeInState = []
        self.initTimeInState()
        self.lastStateTime = initialTime
        self.timesBroken = 0

    def initTimeInState(self):
        for state in ElevatorState:
            self.timeInState.append(SimulationTime())

    def setElevatorState(self, state: ElevatorState, time: SimulationTime):
        # save state statistics
        newDateTime = datetime.datetime(int(time.currentYears), int(time.currentMonths), int(time.currentDays),
                                        int(time.currentHours), int(time.currentMinute), int(time.currentSeconds))

        stateTime = SimulationTime()
        stateTime.setTimeByDatetime(newDateTime)
        stateTime.addTime(-self.lastStateTime.currentSeconds,
                                                        -self.lastStateTime.currentMinute,
                                                        -self.lastStateTime.currentHours,
                                                        -self.lastStateTime.currentDays,
                                                        -self.lastStateTime.currentMonths,
                                                        -self.lastStateTime.currentYears)
        self.timeInState[self.state.value].addTime(stateTime.currentSeconds, stateTime.currentMinute,
                                             stateTime.currentHours, stateTime.currentDays,
                                             stateTime.currentMonths, -self.lastStateTime.currentYears)
        self.lastStateTime = time
        self.state = state;

    def createConnection(self, pis):
        self.pis = pis

    def pickEntities(self, entity):
        self.people = entity.people
        entity.releaseEntities()

    def releaseEntities(self):
        del self.people
        # should we remove the instances like this?
        self.people = []

    def setCurrentLevel(self, level):
        self.currentLevel = level

    def getCurrentLevel(self):
        return self.currentLevel

    def cycleCompleted(self):
        self.currentCycles += 1
