import enum


class PisState(enum.Enum):
    NOT_EMPTY = 0
    EMPTY = 1


class Floor:

    def __init__(self, level):
        self.level = level
        self.people = []
        self.state = PisState.EMPTY
        self.maxPeopleWaiting = 0

    def setPisState(self, state: PisState):
        self.state = state

    def releaseEntities(self):
        self.people = []

    def addPerson(self, person):
        self.people.append(person)
        if len(self.people) > self.maxPeopleWaiting:
            self.maxPeopleWaiting = len(self.people)