from enumeracions import *

class PisState(enum.Enum):
    NOT_EMPTY = 0
    EMPTY = 1

class Pis:

    def __init__(self, numero):
        self.numero = 0
        self.personas = []
        self.state = PisState.EMPTY

    def setPisState(self, state: PisState):
        self.state = state