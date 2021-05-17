from enumeracions import *
from EventsEnum import *
from AscensorEvent import *

class Ascensor:

    # creació d'un nou Ascensor
    def __init__(self, cyclesToBreak, ascensorEvent: EventsEnum):
        # cicles que durarà l'ascensor abans d'espatllar-se'
        self.cyclesToBreak = object;
        # valor per defecte dels cicles de l'ascensor
        self.currentCycles = 0;
        # estat per defecte de l'ascensor
        self.ascensorEvent = ascensorEvent;

    def setAscensorState(self, ascensorEvent: EventsEnum):
        self.ascensorEvent = ascensorEvent;

    def tractarEsdeveniment(self, event: AscensorEvent):

        if (event.tipus == EventsEnum.MOVING):
            self.startMoving()

        if (event.tipus == 'END_SERVICE'):
            self.processarFiServei(event)

    def crearConnexio(self, server2, queue):
        self.queue = queue
        self.server = server2

    def recullEntitat(self, time, entitat):
        self.entitatsTractades = entitat
        self.programarFinalServei(time, entitat)



    def simulationStart(self, event):
        self.state = enumeracions.idle
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
        self.entitatsTractades = self.entitatsTractades + 1
        # Mirar si es pot transferir a on per toqui
        if (server.estat == enumeracions.idle):
            # transferir entitat (es pot fer amb un esdeveniment immediat o invocant a un métode de l'element)
            server.recullEntitat(event.time, event.entitat)
        else:
            if (queue.estat == enumeracions.idle):
                queue.recullEntitat(event.time, event.entitat)
            ...
        self.estat = enumeracions.idle

    ...

