import time

from enumeracions import *


class TimeManager:
    def __init__(self):
        self.initialRealTime = self.getRealTimeInMillis()
        self.currentTime = 0
        self.maxTime = 2*60*1000

    def getRealTimeInMillis(self):
        return int(round(time.time() * 1000))

    def getCurrentTimeInMillis(self):
        return self.getRealTimeInMillis() - self.initialRealTime