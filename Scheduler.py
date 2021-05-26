from EntityGenerator import EntityGenerator
from Pis import *
from SimulatorManager import SimulatorManager
from simulationEvents.Event import Event
from simulationEvents.EventsManager import EventStatus
from simulationEvents.LevelNewArrivalEvent import LevelNewArrivalEvent


class Scheduler:

    # Inicialització de la classe scheduler
    def __init__(self):
        self.simulatorManager = SimulatorManager()

        self.entityGenerator = EntityGenerator(self.simulatorManager)
        self.simulatorManager.initElevators()

    def run(self):


        # para generar una entidad(persona) // hay que enviar la señal de simulation_start
        self.entityGenerator.generateFirstEntity()

        while self.simulatorManager.simulationNotFinished():
            eventResult = EventStatus.PENDING
            nextEvent = self.simulatorManager.getFirstEvent()
            # if it's not the last element of the list and we cannot treat it,
            while nextEvent != None and (eventResult == EventStatus.PENDING or nextEvent == self.simulatorManager.getLastEvent()):
                if self.simulatorManager.eventIsInTime(nextEvent.time):
                    eventResult = nextEvent.treatEvent()
                    if eventResult == EventStatus.TREATED:
                        if isinstance(nextEvent, LevelNewArrivalEvent):
                            self.entityGenerator.generateEntity(nextEvent.time)
                        self.deleteEvent(nextEvent)
                nextEvent = self.simulatorManager.getNextEvent()
        print ("simulation finished")
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



if __name__ == "__main__":
    scheduler = Scheduler()
    scheduler.run()
