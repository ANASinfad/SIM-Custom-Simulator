
from TimeManager import TimeManager
from simulationEvents.EventsManager import EventsManager


class SimulatorManager:
    def __init__(self, numberOfLevels: int, elevatorMovingTime: int):
        self.timeManager = TimeManager()
        self.eventsManager = EventsManager()
        self.numberOfLevels = numberOfLevels
        self.elevatorMovingTime = elevatorMovingTime
        self.elevators = []

