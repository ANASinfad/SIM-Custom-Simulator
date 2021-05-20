from Elevator import Elevator
from EntityGenerator import *
from InputModule import InputModule


class Scheduler:

    # Inicialització de la classe scheduler
    def __init__(self):
        self.eventList = []
        self.inputModule = InputModule()
        self.inputModule.showParameters()
        self.elevators = []
        self.elevators.append(Elevator(self.inputModule.MTF1))
        self.elevators.append(Elevator(self.inputModule.MTF2))
        self.elevators.append(Elevator(self.inputModule.MTF3))
        self.generator = EntityGenerator()
        self.currentTime = 0

        #self.source = Source()
        #self.Server = Server()
        #self.Queue = Queue()
        #self.Server2 = Server()

        #self.source.crearConnexio(server)
        #self.Server.crearConnexio(server2, queue)
        
        #self.simulationStart=Event(self,'SIMULATION_START', 0,null))
        #self.eventList.append(simulationStart)

    def run(self):
        print("running process...")
        # miramos si el evento devuelto por el generador es nulo o no
        generatorEvent = self.generator.generateEntity(self.currentTime)
        if generatorEvent is not None:
            self.eventList.append(generatorEvent)
        #configurar el model per consola, arxiu de text...
        #self.configurarModel()

        #rellotge de simulacio a 0
        #self.currentTime=0
        #bucle de simulació (condició fi simulació llista buida)
        #while self.eventList:
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



if __name__ == "__main__":
    scheduler = Scheduler()
    scheduler.run()
