import enum

import SimulatorManager


class Event:
    # creació d'un nou esdeveniment
    def __init__(self, simulationManager: SimulatorManager, entity, type: enum, time):
        # objecte que processarà l'esdeveniment
        self.entity = entity
        # type event
        self.type = type
        # instant en que succeirà l'esdeveniment
        self.time = time
        self.simulationManager = simulationManager

    # Deleguem el tractament a l'esdeveniment subclasse
    def treatEvent(self):
        pass
