import enum


class Event:
    # creació d'un nou esdeveniment
    def __init__(self, entity, type: enum, time):
        # objecte que processarà l'esdeveniment
        self.entity = entity
        # type event
        self.type = type
        # instant en que succeirà l'esdeveniment
        self.time = time

    # Deleguem el tractament a l'esdeveniment subclasse
    def treatEvent(self):
        pass
