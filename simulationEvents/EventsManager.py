import enum


class EventStatus(enum.Enum):
    PENDING = 0
    TREATED = 1

class EventsManager:
    def __init__(self):
        self.eventList = []
        self.eventIterator = 0

    def addEvent(self, event):
        # inserir esdeveniment de forma ordenada
        if len(self.eventList) == 0:
            self.eventList.append(event)
            return
        i = 0
        j = -1
        while i < len(self.eventList) and j == -1:
            if self.eventList[i].time > event.time:
                j = i
            else:
                i += 1
        self.eventList.insert(j, event)

    def deleteEvent(self, event):
        # inserir esdeveniment de forma ordenada
        self.eventList.remove(event)

    def getFirstEvent(self):
        self.eventIterator = 0
        if len(self.eventList) > 0:
            return self.eventList[0]
        return None

    def getNextEvent(self):
        self.eventIterator += 1
        if len(self.eventList) > self.eventIterator:
            return self.eventList[self.eventIterator]
        return None

    def getLastEvent(self):
        if len(self.eventList) > 0:
            return self.eventList[-1]
        else:
            return None