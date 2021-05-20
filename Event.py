from TransitionsEnum import *


class Event:
    # creació d'un nou esdeveniment
    def __init__(self, entity, type: TransitionsEnum, time):
        # objecte que processarà l'esdeveniment
        self.entity = entity
        # type event
        self.type = type
        # instant en que succeirà l'esdeveniment
        self.time = time

    # Podríem delegar l'esdeveniment a l'objecte des de l'event o des del scheduler
    def treatEvent(self):
        self.entity.treatEvent(self.type)
