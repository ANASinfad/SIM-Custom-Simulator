import enum

from SimulatorManager import SimulatorManager


class Event:
    # creació d'un nou esdeveniment
    def __init__(self, simulatorManager: SimulatorManager, entity, eventType: enum, time):
        # objecte que processarà l'esdeveniment
        self.entity = entity
        # type event
        self.eventType = eventType
        # instant en que succeirà l'esdeveniment
        self.time = time
        self.simulatorManager = simulatorManager

    # Deleguem el tractament a l'esdeveniment subclasse
    def treatEvent(self):
        pass
