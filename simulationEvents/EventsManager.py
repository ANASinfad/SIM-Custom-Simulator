import time

from enumeracions import *


class EventsManager:
    def __init__(self):
        self.eventList = []

    def afegirEsdeveniment(self, event):
        # inserir esdeveniment de forma ordenada
        self.eventList.append(event)

    def eliminarEsdeveniment(self, event):
        # inserir esdeveniment de forma ordenada
        self.eventList.remove(event)