from Ascensor import Ascensor
from EventsEnum import *
from Event import Event


class Scheduler:

    # Inicialització de la classe scheduler
    def __init__(self):
        self.eventList = []
        self.entradaParametros()
        currentTime = 0

        #self.source = Source()
        #self.Server = Server()
        #self.Queue = Queue()
        #self.Server2 = Server()

        #self.source.crearConnexio(server)
        #self.Server.crearConnexio(server2, queue)
        
        #self.simulationStart=Event(self,'SIMULATION_START', 0,null))
        #self.eventList.append(simulationStart)

    def entradaParametros(self):
        respuesta = YesNoQuestion('¿Desea definir el tiempo que tarda en moverse el ascensor de un piso a otro?')
        if respuesta == "si":
            self.ascensorTransportTime = int(input('indique el tiempo en segundos: '))

        respuesta = YesNoQuestion('¿Desea definir el maximo número de usos de cada ascensor?')
        if respuesta == "si":
            self.MTF1 = int(input('indique el numero de usos del primer ascensor: '))
            self.MTF2 = int(input('indique el numero de usos del segundo ascensor: '))
            self.MTF3 = int(input('indique el numero de usos del tercer ascensor: '))

        respuesta = YesNoQuestion('¿Desea definir el numero de pisos?')
        if respuesta == "si":
            self.numberOfLevels = int(input('indique el numero de pisos: '))

        print('Esta es tu entrada:')
        print(self.ascensorTransportTime)
        print(self.numberOfLevels)
        print(self.MTF1)
        print(self.MTF2)
        print(self.MTF3)

    def run(self):
        print("running process...")
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

def YesNoQuestion(question):
    print(question)
    respuesta = input()
    while respuesta != "si" and respuesta != "no":
        print("Escriba si o no")
        respuesta = input()
    return respuesta

if __name__ == "__main__":
    scheduler = Scheduler()
    scheduler.run()
