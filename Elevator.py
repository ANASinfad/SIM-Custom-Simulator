import enum


from Event import *
from enumeracions import *


class ElevatorState(enum.Enum):
    IDLE = 0
    MOVING = 1
    ENTITY_TRANSFER = 2
    BROKEN = 3

    # This one only available for the 3rd elevator
    OUT_OF_SERVICE = 4


class TransitionsEnum(enum.Enum):
    REACH_DESTINATION = 0
    BREAK = 1
    FIX = 2
    DOORS_CLOSED = 3
    ONE_BROKEN = 4
    ALL_FIXED = 5


class Elevator:

    # Initialization of an elevator
    def __init__(self, cyclesToBreak):
        self.cyclesToBreak = cyclesToBreak
        self.currentCycles = 0
        self.state = ElevatorState.IDLE
        self.floor = 0

    def setElevatorState(self, ascensorEvent: ElevatorState):
        self.ascensorEvent = ascensorEvent;

    def treatEvent(self, event: Event):
        if event.type == TransitionsEnum.CALL:
            self.startMoving(event)

        elif event.type == TransitionsEnum.FINISH_SERVICE:
            self.startEntityTransfer(event)

        elif event.type == TransitionsEnum.BREAK:
            self.startBroken(event)

        elif event.type == TransitionsEnum.DOORS_CLOSED:
            self.startIdle(event)

        elif event.type == TransitionsEnum.ALL_FIXED:
            self.startOutOfService(event)
        elif event.type == TransitionsEnum.FIX:
            self.startFix(event)
        elif event.type == TransitionsEnum.ONE_BROKEN:
            self.startOneBroken(event)

    def createConnection(self, server2, queue):
        self.queue = queue
        self.server = server2

    def pickEntity(self, time, entitat):
        self.entitatsTractades = entitat
        self.programarFinalServei(time, entitat)

    def startMoving(self):
        self.state = ElevatorState.MOVING

    def startEntityTransfer(self):
        self.state = ElevatorState.ENTITY_TRANSFER
        self.entitatsTractades = 0

    def startBroken(self):
        self.state = ElevatorState.BROKEN
        self.entitatsTractades = 0

    def startIdle(self):
        self.state = ElevatorState.IDLE
        self.entitatsTractades = 0

    def startOutOfService(self, event):
        self.state = ElevatorState.OUT_OF_SERVICE
        self.entitatsTractades = 0

    def simulationStart(self, event):
        self.state = ElevatorState.idle
        self.entitatsTractades = 0

    def programarFinalServei(self, time, entitat):
        # que triguem a fer un servei (aleatorietat)
        tempsServei = 1  # _alguna_funcio ()
        # incrementem estadistics si s'escau
        self.entitatsTractades = self.entitatsTractades + 1
        self.state = enumeracions.busy
        # programació final servei
        return Event(self, 'END_SERVICE', time + tempsServei, entitat)

    def processarFiServei(self, event):
        # Registrar estadístics
        # self.entitatsTractades = self.entitatsTractades + 1
        # Mirar si es pot transferir a on per toqui
        # if (server.estat == enumeracions.idle):
        # transferir entitat (es pot fer amb un esdeveniment immediat o invocant a un métode de l'element)
        #   server.recullEntitat(event.time, event.entitat)
        # else:
        #    if (queue.estat == enumeracions.idle):
        #        queue.recullEntitat(event.time, event.entitat)

        self.estat = enumeracions.idle
