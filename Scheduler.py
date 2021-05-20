from InputModule import InputModule
from Elevator import *


class Scheduler:

    # Inicialització de la classe scheduler
    def __init__(self):
        self.eventList = []
        self.run()


        #self.source = Source()
        #self.Server = Server()
        #self.Queue = Queue()
        #self.Server2 = Server()

        #self.source.crearConnexio(server)
        #self.Server.crearConnexio(server2, queue)
        
        #self.simulationStart=Event(self,'SIMULATION_START', 0,null))
        #self.eventList.append(simulationStart)

    def run(self):
        #configurar el model per consola, arxiu de text...
        self.inputModule = InputModule()
        #mostrar la configuració
        self.inputModule.showParameters()
        self.elevators = []

        self.configurarModel()

        #self.currentTime=0
        #bucle de simulació (condició fi simulació llista buida)
        eventIterator = 0
        while eventIterator <= len(self.eventList):
            #obtenim l'esdeveniment a tractar
            eventATractar = self.eventList[eventIterator]
            transition = eventATractar.entity.treatEvent(eventATractar)
            if isinstance(eventATractar.entity, Elevator):
                self.nextElevatorEvent(eventATractar.entity, transition)
            #recuperem event simulacio
         #   event=self.eventList.donamEsdeveniment
            #actualitzem el rellotge de simulacio
          #  self.currentTime=event.time
            # deleguem l'acció a realitzar de l'esdeveniment a l'objecte que l'ha generat
            # també podríem delegar l'acció a un altre objecte
           # event.objecte.tractarEsdeveniment(event)
        
        #recollida d'estadístics
        #self.recollirEstadistics()

    def afegirEsdeveniment(self,event):
        #inserir esdeveniment de forma ordenada
        self.eventList.inserirEvent(event)

    # comunicar a tots els objectes que cal preparar-se
    def tractarEsdeveniment(self,event):
        if (event.tipus=="SIMULATION_START"):
            print("preparant esdeveniment!")

    def nextElevatorEvent(self, entity: Elevator, transition):

        if  transition == TransitionsEnum.BREAK:
            entity.setElevatorState(ElevatorState.BROKEN)
            self.afegirEsdeveniment(Event(entity,ElevatorState.BROKEN, 0))
            if entity != self.elevators[2]:
                self.elevators[2].setElevatorState(ElevatorState.IDLE)
                self.afegirEsdeveniment(Event(self.elevators[2],ElevatorState.IDLE, 0))

        elif transition == TransitionsEnum.CALL:
            entity.setElevatorState(ElevatorState.MOVING)
            self.afegirEsdeveniment(Event(entity,ElevatorState.MOVING, 0))

        elif transition == TransitionsEnum.REACH_DESTINATION:
            entity.setElevatorState(ElevatorState.ENTITY_TRANSFER)
            self.afegirEsdeveniment(Event(entity,ElevatorState.ENTITY_TRANSFER, 0))

        elif transition == TransitionsEnum.DOORS_CLOSED:
            if (entity != self.elevators[2] or self.elevators[0].state == ElevatorState.BROKEN or self.elevators[1].state != ElevatorState.BROKEN):
                entity.setElevatorState(ElevatorState.IDLE)
                self.afegirEsdeveniment(Event(entity,ElevatorState.IDLE, 0))
            else:
                entity.setElevatorState(ElevatorState.OUT_OF_SERVICE)
                self.afegirEsdeveniment(Event(entity,ElevatorState.OUT_OF_SERVICE, 0))

        elif transition == TransitionsEnum.FIX:
            entity.setElevatorState(ElevatorState.IDLE)
            self.afegirEsdeveniment(Event(entity,ElevatorState.OUT_OF_SERVICE, 0))


    def configurarmodel(self):
        #Inicialitzem els ascensors amb el seu estat inicial
        self.elevators.append(Elevator(self.inputModule.MTF1))
        self.elevators.append(Elevator(self.inputModule.MTF2))
        self.elevators.append(Elevator(self.inputModule.MTF3))
        self.elevators[2].state = ElevatorState.OUT_OF_SERVICE
        self.scaleTime = self.inputModule.timeScale
        #rellotge de simulacio a 0
        currentTime = 0

if __name__ == "__main__":
    scheduler = Scheduler()
    scheduler.run()
