import datetime


class SimulationTime:
    def __init__(self):
        self.currentSeconds = 0
        self.currentMinute = 0
        self.currentHours = 0
        self.currentDays = 0
        self.currentMonths= 0
        self.currentYears = 0

    def __init__(self, time: datetime.datetime):
        # initial time variables
        self.currentSeconds = time.second
        self.currentMinute = time.minute
        self.currentHours = time.hour
        self.currentDays = time.day
        self.currentMonths = time.month
        self.currentYears = time.year

    def getString(self):

        return str(self.currentMonths) + " " + str(self.currentDays) + "th" + str(self.currentHours) + ":" + str(self.currentMinute) + ":" + str(self.currentSeconds)

    def addTime(self, s, minutes, h, d, m, y):
        # s >= 0 and < 60
        # min >= 0 and < 60
        # h >= 0 and < 24
        # d >= 0 and < 30
        # y >= 0
        self.currentSeconds += s
        self.currentMinute += int(self.currentSeconds/60) + minutes
        self.currentSeconds = self.currentSeconds % 60
        self.currentHours += int(self.currentMinute/60) + h
        self.currentMinute = self.currentMinute % 60
        self.currentDays += int(self.currentHours/24) + d
        self.currentHours = self.currentHours % 24
        self.currentMonths += int(self.currentDays/30) + m
        self.currentDays = self.currentDays % 30
        self.currentYears += int(self.currentMonths/12) + y
        self.currentMonths = self.currentMonths % 12
        return self



class TimeManager:
    def __init__(self):
        self.maxTime = self.addTime(self.getCurrentTime(), 0, 0, 2, 0, 0, 0)
        self.instantSimulation = 0

    def getCurrentTime(self):
        currentTime = SimulationTime(datetime.datetime.now())
        return currentTime

    def addTime(self, time: SimulationTime, s, minutes, h, d, m, y):
        # s >= 0 and < 60
        # min >= 0 and < 60
        # h >= 0 and < 24
        # d >= 0 and < 30
        # y >= 0
        newDateTime = datetime.datetime(int(time.currentYears), int(time.currentMonths), int(time.currentDays),
                                        int(time.currentHours), int(time.currentMinute), int(time.currentSeconds))
        return SimulationTime(newDateTime).addTime(s, minutes, h, d, m, y)


    def eventIsInTime(self, eventTime: SimulationTime):
        if self.instantSimulation:
            return 1
        currentTime = self.getCurrentTime()
        return self.isTimeLowerThanTime(eventTime, currentTime)

    def setInstantSimulation(self, instantSimulation):
        self.instantSimulation = instantSimulation

    def isOutOfTime(self, time: SimulationTime):
        return self.isTimeLowerThanTime(self.maxTime, time)

    def isTimeLowerThanTime(self, time1: SimulationTime, time2: SimulationTime):
        if time1.currentYears < time2.currentYears:
             return 1
        if time1.currentYears > time2.currentYears:
            return 0

        if time1.currentMonths < time2.currentMonths:
             return 1
        if time1.currentMonths > time2.currentMonths:
             return 0

        if time1.currentDays < time2.currentDays:
             return 1
        if time1.currentDays > time2.currentDays:
             return 0

        if time1.currentHours < time2.currentHours:
             return 1
        if time1.currentHours > time2.currentHours:
             return 0

        if time1.currentMinute < time2.currentMinute:
             return 1
        if time1.currentMinute > time2.currentMinute:
             return 0

        if time1.currentSeconds < time2.currentSeconds:
             return 1
        return 0