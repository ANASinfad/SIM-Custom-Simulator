from Elevator import ElevatorState
from EntityGenerator import EntityGenerator
from Floor import *
from SimulatorManager import SimulatorManager
from StatisticsManager import StatisticsManager
from simulationEvents.Event import Event
from simulationEvents.EventsManager import EventStatus
from simulationEvents.LevelNewArrivalEvent import LevelNewArrivalEvent


class Scheduler:

    # Inicialització de la classe scheduler
    def __init__(self):
        self.simulatorManager = SimulatorManager()
        self.statisticsManager = StatisticsManager(self.simulatorManager)
        self.entityGenerator = EntityGenerator(self.simulatorManager)
        self.simulatorManager.initElevators()

    def run(self):

        # Definim el primer esdeveniment d'arribada de persona, cada cop que
        # es tracti un esdeveniment d'arribada, es planificarà una nova arribada
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
        print("")

        # recollida d'estadístics
        self.statisticsManager.showStatistics()

    def afegirEsdeveniment(self, event):
        # inserir esdeveniment de forma ordenada
        self.simulatorManager.eventsManager.addEvent(event)

    def deleteEvent(self, event):
        # eliminar esdeveniment seleccionat
        self.simulatorManager.eventsManager.deleteEvent(event)



if __name__ == "__main__":
    scheduler = Scheduler()
    scheduler.run()
