from Elevator import Elevator, ElevatorState
from EntityGenerator import EntityGenerator
from InputModule import InputModule
from Pis import PisState
from SimulatorManager import SimulatorManager
from simulationEvents.Event import Event


class Scheduler:

    # Inicialització de la classe scheduler
    def __init__(self):
        print("init")
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
        self.configurarmodel()

        # para generar una entidad(persona) // hay que enviar la señal de simulation_start
        generatorEvent = self.entityGenerator.generateEntity(self.simulatorManager.timeManager.getCurrentTimeInMillis())

        self.afegirEsdeveniment(generatorEvent)

        while self.simulatorManager.timeManager.getCurrentTimeInMillis() < self.simulatorManager.timeManager.maxTime:
            treatedEvents = []
            for event in self.simulatorManager.eventsManager.eventList:
                if event.time <= self.simulatorManager.timeManager.getCurrentTimeInMillis():
                    self.tractarEsdeveniment(event)
                    treatedEvents.append(event)

                if self.simulatorManager.timeManager.getCurrentTimeInMillis() < self.simulatorManager.timeManager.maxTime:
                    break


            # all the events treated are removed from the list
            for event in treatedEvents:
                self.eliminarEsdeveniment(event)

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
        self.simulatorManager.eventsManager.afegirEsdeveniment(event)

    def eliminarEsdeveniment(self, event):
        # eliminar esdeveniment seleccionat
        self.simulatorManager.eventsManager.eliminarEsdeveniment(event)

    # comunicar a tots els objectes que cal preparar-se
    def tractarEsdeveniment(self, event: Event):
        if (event.time < self.simulatorManager.timeManager.maxTime):
        # si encara no s'acaba la simulació, l'esdeveniment es processa

            if (event.type == "SIMULATION_START"):
                print("preparant esdeveniment!")

            if (event.type == PisState.NOT_EMPTY):
                newEvent = self.entityGenerator.generateEntity(self.simulatorManager.timeManager.getCurrentTimeInMillis())
                self.afegirEsdeveniment(newEvent)
                print("Arriba un pipiolo a l'ascensor")
            else:
                event.treatEvent()


    def configurarmodel(self):
        # Inicialitzem els ascensors amb el seu estat inicial

        self.scaleTime = self.inputModule.timeScale

        numberOfLevels = self.inputModule.numberOfLevels
        elevatorMovingTime = self.inputModule.ascensorTransportTime
        self.simulatorManager = SimulatorManager(numberOfLevels, elevatorMovingTime)
        self.entityGenerator = EntityGenerator(self.simulatorManager, numberOfLevels)

        self.simulatorManager.elevators.append(Elevator(self.inputModule.MTF1))
        self.simulatorManager.elevators.append(Elevator(self.inputModule.MTF2))
        self.simulatorManager.elevators.append(Elevator(self.inputModule.MTF3))
        self.simulatorManager.elevators[2].state = ElevatorState.OUT_OF_SERVICE

        # rellotge de simulacio a 0
        currentTime = 0


if __name__ == "__main__":
    scheduler = Scheduler()
    scheduler.run()
