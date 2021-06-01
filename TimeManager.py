import datetime
import math
import time


class SimulationTime:
    def __init__(self):
        self.currentSeconds = 0
        self.currentMinute = 0
        self.currentHours = 0
        self.currentDays = 0
        self.currentMonths = 0
        self.currentYears = 0

    def setTimeByDatetime(self, time: datetime.datetime):
        # initial time variables
        self.currentSeconds = time.second
        self.currentMinute = time.minute
        self.currentHours = time.hour
        self.currentDays = time.day
        self.currentMonths = time.month
        self.currentYears = time.year

    def setTimeByParameters(self, currentSeconds, currentMinute, currentHours, currentDays, currentMonths, currentYears):
        # initial time variables
        self.currentSeconds = currentSeconds
        self.currentMinute = currentMinute
        self.currentHours = currentHours
        self.currentDays = currentDays
        self.currentMonths = currentMonths
        self.currentYears = currentYears

    def getDateAsString(self):
        return str(self.currentDays) + "/" + str(self.currentMonths) + "/" + str(self.currentYears) + " " + str(self.currentHours) \
               + ":" + str(self.currentMinute) + ":" + str(self.currentSeconds)

    def getDateAsFileName(self):
        return str(self.currentDays) + "_" + str(self.currentMonths) + "_" + str(self.currentYears) + "__" + str(self.currentHours) \
               + "_" + str(self.currentMinute) + "_" + str(self.currentSeconds)

    def getTimeInHoursAndLower(self):
        months = self.currentMonths + self.currentYears * 12
        days = self.currentDays + months * 30
        hours = self.currentHours + days * 24
        return str(hours) + " hours, " + str(self.currentMinute) + " minutes and " + \
               str(self.currentSeconds) + " seconds"

    def getTimeInHoursDouble(self):
        months = self.currentMonths + self.currentYears * 12
        days = self.currentDays + months * 30
        hours = self.currentHours + days * 24
        return hours + self.currentMinute / 60 + self.currentSeconds / 3600

    def addTime(self, s, minutes, h, d, m, y):
        #post s >= 0 and < 60
        # min >= 0 and < 60
        # h >= 0 and < 24
        # d >= 1 and < 30
        #m >= 1 and <= 12
        # y >= 0
        self.currentSeconds += s
        self.currentMinute += math.floor(self.currentSeconds / 60) + minutes
        self.currentSeconds = self.currentSeconds % 60
        self.currentHours += math.floor(self.currentMinute / 60) + h
        self.currentMinute = self.currentMinute % 60
        self.currentDays += math.floor(self.currentHours / 24) + d
        self.currentHours = self.currentHours % 24
        self.currentMonths += math.floor((self.currentDays - 1) / 31) + m
        if self.currentDays == 32:
            self.currentDays = 1
        self.currentYears += math.floor((self.currentMonths - 1) / 12) + y
        if self.currentMonths == 13:
            self.currentMonths = 1

        return self

    def addTimeWithoutFormat(self, s, minutes, h, d, m, y):
        # s >= 0 and < 60
        # min >= 0 and < 60
        # h >= 0 and < 24
        # d >= 0 and < 30
        # y >= 0
        self.currentSeconds += s
        self.currentMinute += math.floor(self.currentSeconds / 60) + minutes
        self.currentSeconds = self.currentSeconds % 60
        self.currentHours += math.floor(self.currentMinute / 60) + h
        self.currentMinute = self.currentMinute % 60
        self.currentDays += math.floor(self.currentHours / 24) + d
        self.currentHours = self.currentHours % 24
        self.currentMonths += math.floor(self.currentDays / 31) + m
        self.currentDays = self.currentDays % 31
        self.currentYears += math.floor(self.currentMonths / 12) + y
        self.currentMonths = self.currentMonths % 12

        return self

    def isLowerThanTime(self,  time):
        if self.currentYears < time.currentYears:
            return 1
        if self.currentYears > time.currentYears:
            return 0

        if self.currentMonths < time.currentMonths:
            return 1
        if self.currentMonths > time.currentMonths:
            return 0

        if self.currentDays < time.currentDays:
            return 1
        if self.currentDays > time.currentDays:
            return 0

        if self.currentHours < time.currentHours:
            return 1
        if self.currentHours > time.currentHours:
            return 0

        if self.currentMinute < time.currentMinute:
            return 1
        if self.currentMinute > time.currentMinute:
            return 0

        if self.currentSeconds < time.currentSeconds:
            return 1
        return 0


class TimeManager:
    def __init__(self):
        self.initialTime = self.getCurrentTime()
        self.maxTime = self.getCurrentTime()
        self.instantSimulation = 0

    def getCurrentTime(self):
        currentTime = SimulationTime()
        currentTime.setTimeByDatetime(datetime.datetime.now())
        return currentTime

    def addTime(self, time: SimulationTime, s, minutes, h, d, m, y):
        # s >= 0 and < 60
        # min >= 0 and < 60
        # h >= 0 and < 24
        # d >= 0 and < 30
        # y >= 0

        result = SimulationTime()
        result.setTimeByParameters(time.currentSeconds, time.currentMinute, time.currentHours, time.currentDays,
                                   time.currentMonths, time.currentYears)
        return result.addTime(s, minutes, h, d, m, y)

    def addTimeWithoutFormat(self, time: SimulationTime, s, minutes, h, d, m, y):
        # s >= 0 and < 60
        # min >= 0 and < 60
        # h >= 0 and < 24
        # d >= 0 and < 30
        # y >= 0

        result = SimulationTime()
        result.setTimeByParameters(time.currentSeconds, time.currentMinute, time.currentHours, time.currentDays,
                                   time.currentMonths, time.currentYears)
        return result.addTimeWithoutFormat(s, minutes, h, d, m, y)

    def eventIsInTime(self, eventTime: SimulationTime):
        if self.instantSimulation:
            return 1
        currentTime = self.getCurrentTime()
        if self.isTimeLowerThanTime(currentTime, eventTime):
            timeToWait = self.addTimeWithoutFormat(eventTime, -currentTime.currentSeconds, -currentTime.currentMinute,
                                  -currentTime.currentHours, -currentTime.currentDays, -currentTime.currentMonths,
                                  -currentTime.currentYears)
            self.sleepTime(timeToWait)
        return 1

    def setInstantSimulation(self, instantSimulation):
        self.instantSimulation = instantSimulation

    def isOutOfTime(self, time: SimulationTime):
        return self.isTimeLowerThanTime(self.maxTime, time)

    def isTimeLowerThanTime(self, time1: SimulationTime, time2: SimulationTime):
        return time1.isLowerThanTime(time2)

    def setSimulationTime(self, timeToWait: SimulationTime):
        self.maxTime = self.addTime(self.initialTime, timeToWait.currentSeconds, timeToWait.currentMinute,
                                    timeToWait.currentHours, timeToWait.currentDays,
                                    timeToWait.currentMonths, timeToWait.currentYears)

    def sleepTime(self, simulationTime):
        time.sleep(simulationTime.currentSeconds + simulationTime.currentMinute*60 + simulationTime.currentHours * 3600)
        self.sleepDays(simulationTime.currentDays)
        self.sleepMonths(simulationTime.currentMonths)
        self.sleepYears(simulationTime.currentYears)

    def sleepYears(self, years):
        for day in range(years):
            self.sleepMonths(12)

    def sleepMonths(self, months):
        for day in range(months):
            self.sleepDays(30)

    def sleepDays(self, days):
        for day in range(days):
            time.sleep(24*3600)