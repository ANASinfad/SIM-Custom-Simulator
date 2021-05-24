import enum


class PisState(enum.Enum):
    NOT_EMPTY = 0
    EMPTY = 1


class Pis:

    def __init__(self, numero):
        self.numero = 0
        self.people = []
        self.state = PisState.EMPTY

    def setPisState(self, state: PisState):
        self.state = state

    def releaseEntities(self):
        self.people = []
