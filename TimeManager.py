import time


class TimeManager:
    def __init__(self):
        self.initialRealTime = self.getRealTimeInMillis()
        self.currentTime = 0
        self.maxTime = 5*60*1000
        self.instantSimulation = 0

    def getRealTimeInMillis(self):
        return int(round(time.time() * 1000))

    def getCurrentTimeInMillis(self):
        return self.getRealTimeInMillis() - self.initialRealTime

    def eventIsInTime(self, eventTime):
        if self.instantSimulation:
            return 1
        return eventTime <= self.getCurrentTimeInMillis()

    def setInstantSimulation(self, instantSimulation):
        self.instantSimulation = instantSimulation