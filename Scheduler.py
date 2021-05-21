from Elevator import *
from EntityGenerator import *
from InputModule import InputModule
from Pis import *
import time


class Scheduler:

    # Inicialització de la classe scheduler
    def __init__(self):
        self.eventList = []
        self.currentTime = self.getCurrentTimeInMillis()
        # by default the simulation time will be 1h
        self.maxTime = self.currentTime + 2*60*1000

        print("max time = ", self.maxTime)
        print("current time = ", self.currentTime)

        # self.source = Source()
        # self.Server = Server()
        # self.Queue = Queue()
        # self.Server2 = Server()

        # self.source.crearConnexio(server)
        # self.Server.crearConnexio(server2, queue)

        # self.simulationStart=Event(self,'SIMULATION_START', 0,null))
        # self.eventList.append(simulationStart)

    def run(self):
        # configurar el model per consola, arxiu de text...
        self.inputModule = InputModule()
        # mostrar la configuració
        self.inputModule.showParameters()
        self.elevators = []
        self.configurarmodel()

        # para generar una entidad(persona) // hay que enviar la señal de simulation_start
        generatorEvent = self.generator.generateEntity(self.currentTime)
        self.afegirEsdeveniment(generatorEvent)

        while self.currentTime < self.maxTime:
            treatedEvents = []
            for event in self.eventList:
                if (event.time <= self.currentTime):
                    self.tractarEsdeveniment(event)
                    treatedEvents.append(event)

                self.currentTime = self.getCurrentTimeInMillis()
                if self.currentTime < self.maxTime:
                    break


            # all the events treated are removed from the list
            for event in treatedEvents:
                self.eventList.remove(event)

            # Ahora hay que tratar el evento



        # self.currentTime=0
        # bucle de simulació (condició fi simulació llista buida)


        # obtenim l'esdeveniment a tractar
        #eventATractar = self.eventList[eventIterator]
        #transition = eventATractar.entity.treatEvent(eventATractar)
        #if isinstance(eventATractar.entity, Elevator):
        #    self.nextElevatorEvent(eventATractar.entity, transition)
        #elif isinstance(eventATractar.entity, Pis):
        #    self.nextPisEvent(eventATractar.entity, transition)

        # recuperem event simulacio
        #   event=self.eventList.donamEsdeveniment
        # actualitzem el rellotge de simulacio
        #  self.currentTime=event.time
        # deleguem l'acció a realitzar de l'esdeveniment a l'objecte que l'ha generat
        # també podríem delegar l'acció a un altre objecte
        # event.objecte.tractarEsdeveniment(event)

        # recollida d'estadístics
        # self.recollirEstadistics()

    def afegirEsdeveniment(self, event):
        # inserir esdeveniment de forma ordenada
        #self.eventList.inserirEvent(event)
        self.eventList.append(event)

    # comunicar a tots els objectes que cal preparar-se
    def tractarEsdeveniment(self, event: Event):
        if (event.time < self.maxTime):
        # si encara no s'acaba la simulació, l'esdeveniment es processa

            if (event.type == "SIMULATION_START"):
                print("preparant esdeveniment!")

            if (event.type == TransitionsEnum.NEW_ARRIVAL):
                newEvent = self.generator.generateEntity(self.currentTime)
                self.afegirEsdeveniment(newEvent)
                print("Arriba un pipiolo a l'ascensor")


    def nextElevatorEvent(self, entity: Elevator, transition):

        if transition == TransitionsEnum.BREAK:
            entity.setElevatorState(ElevatorState.BROKEN)
            self.afegirEsdeveniment(Event(entity, ElevatorState.BROKEN, 0))
            if entity != self.elevators[2]:
                self.elevators[2].setElevatorState(ElevatorState.IDLE)
                self.afegirEsdeveniment(Event(self.elevators[2], ElevatorState.IDLE, 0))

        elif transition == TransitionsEnum.CALL:
            entity.setElevatorState(ElevatorState.MOVING)
            self.afegirEsdeveniment(Event(entity, ElevatorState.MOVING, 0))

        elif transition == TransitionsEnum.REACH_DESTINATION:
            entity.setElevatorState(ElevatorState.ENTITY_TRANSFER)
            self.afegirEsdeveniment(Event(entity, ElevatorState.ENTITY_TRANSFER, 0))

        elif transition == TransitionsEnum.DOORS_CLOSED:
            if (entity != self.elevators[2] or self.elevators[0].state == ElevatorState.BROKEN or self.elevators[
                1].state != ElevatorState.BROKEN):
                entity.setElevatorState(ElevatorState.IDLE)
                self.afegirEsdeveniment(Event(entity, ElevatorState.IDLE, 0))
            else:
                entity.setElevatorState(ElevatorState.OUT_OF_SERVICE)
                self.afegirEsdeveniment(Event(entity, ElevatorState.OUT_OF_SERVICE, 0))

        elif transition == TransitionsEnum.FIX:
            entity.setElevatorState(ElevatorState.IDLE)
            self.afegirEsdeveniment(Event(entity, ElevatorState.OUT_OF_SERVICE, 0))

    def nextPisEvent(self, entity: Pis, transition):
        if transition == TransitionsEnum.NEW_ARRIVAL:
            entity.setPisState(PisState.NOT_EMPTY)
            self.afegirEsdeveniment(Event(entity, PisState.EMPTY, 0))
            if (entity.numero % 2 == 0):
                if (self.elevators[0].state != ElevatorState.BROKEN):
                    self.afegirEsdeveniment(Event(self.elevators[0], ElevatorState.MOVING, 0))
                else:
                    self.afegirEsdeveniment(Event(self.elevators[2], ElevatorState.MOVING, 0))
            if (entity.numero % 2 == 1):
                if (self.elevators[0].state != ElevatorState.BROKEN):
                    self.afegirEsdeveniment(Event(self.elevators[1], ElevatorState.MOVING, 0))
                else:
                    self.afegirEsdeveniment(Event(self.elevators[2], ElevatorState.MOVING, 0))


    def configurarmodel(self):
        # Inicialitzem els ascensors amb el seu estat inicial
        self.elevators.append(Elevator(self.inputModule.MTF1))
        self.elevators.append(Elevator(self.inputModule.MTF2))
        self.elevators.append(Elevator(self.inputModule.MTF3))
        self.elevators[2].state = ElevatorState.OUT_OF_SERVICE
        self.scaleTime = self.inputModule.timeScale

        self.generator = EntityGenerator(self.inputModule.numberOfLevels)
        # rellotge de simulacio a 0
        currentTime = 0

    def getCurrentTimeInMillis(self):
        return int(round(time.time() * 1000))

if __name__ == "__main__":
    scheduler = Scheduler()
    scheduler.run()
