class EventsManager:
    def __init__(self):
        self.eventList = []

    def addEvent(self, event):
        # inserir esdeveniment de forma ordenada
        if len(self.eventList) == 0:
            self.eventList.append(event)
            pass
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

    def getNextEvent(self):
        if len(self.eventList) > 0:
            return self.eventList[0]
        return None
