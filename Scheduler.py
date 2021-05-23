from EntityGenerator import EntityGenerator
from Pis import *
from SimulatorManager import SimulatorManager
from TimeManager import TimeManager
from simulationEvents.Event import Event


class Scheduler:

    # Inicialització de la classe scheduler
    def __init__(self):
        self.simulatorManager = SimulatorManager()
        self.treatedEvents = []

        self.entityGenerator = EntityGenerator(self.simulatorManager)
        self.simulatorManager.initElevators()

    def run(self):


        # para generar una entidad(persona) // hay que enviar la señal de simulation_start
        self.entityGenerator.generateEntity()

        while self.simulatorManager.simulationNotFinished():
            nextEvent = self.simulatorManager.getNextEvent()
            nextEvent.treatEvent()
            self.treatedEvents.append(nextEvent)
            self.deleteEvent(nextEvent)
            #for event in self.simulatorManager.eventsManager.eventList:
             #   if event.time <= self.simulatorManager.timeManager.getCurrentTimeInMillis():
              #      self.tractarEsdeveniment(event)
               #     self.treatedEvents.append(event)

               # if self.simulatorManager.timeManager.getCurrentTimeInMillis() < self.simulatorManager.timeManager.maxTime:
                #    break

            # all the events treated are removed from the list
            # for event in treatedEvents:
             #   self.deleteEvent(event)


        # self.currentTime=0
        # bucle de simulació (condició fi simulació llista buida)

        # obtenim l'esdeveniment a tractar
        # eventATractar = self.eventList[eventIterator]
        # transition = eventATractar.entity.treatEvent(eventATractar)
        # if isinstance(eventATractar.entity, Elevator):
        #    self.nextElevatorEvent(eventATractar.entity, transition)
        # elif isinstance(eventATractar.entity, Pis):
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
        self.simulatorManager.eventsManager.addEvent(event)

    def deleteEvent(self, event):
        # eliminar esdeveniment seleccionat
        self.simulatorManager.eventsManager.deleteEvent(event)

    # comunicar a tots els objectes que cal preparar-se
    def tractarEsdeveniment(self, event: Event):
        if (event.time < self.simulatorManager.timeManager.maxTime):
            # si encara no s'acaba la simulació, l'esdeveniment es processa

            if (event.type == "SIMULATION_START"):
                print("preparant esdeveniment!")

            if (event.type == PisState.NOT_EMPTY):
                newEvent = self.entityGenerator.generateEntity(
                    self.simulatorManager.timeManager.getCurrentTimeInMillis())
                self.afegirEsdeveniment(newEvent)
                print("Arriba un pipiolo a l'ascensor")
            else:
                event.treatEvent()


if __name__ == "__main__":
    scheduler = Scheduler()
    scheduler.run()
