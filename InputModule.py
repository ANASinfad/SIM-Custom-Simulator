from TimeManager import SimulationTime

CONST_DEFAULT_TRANSPORT_TIME = 5
CONST_DEFAULT_MTF1 = 100
CONST_DEFAULT_MTF2 = 200
CONST_DEFAULT_MTF3 = 300
CONST_DEFAULT_NUMBER_LEVELS = 10
CONST_DEFAULT_ARRIVAL_TIME = 20


# this class holds the input information of the user
class InputModule:

    def __init__(self):
        respuesta = YesNoQuestion('¿Desea definir el tiempo que tarda en moverse el ascensor de un piso a otro?')
        if respuesta == "si":
            self.ascensorTransportTime = int(input('indique el tiempo en segundos: '))
        else:
            print('se establecerá un tiempo de transporte por defecto')
            self.ascensorTransportTime = CONST_DEFAULT_TRANSPORT_TIME

        respuesta = YesNoQuestion('¿Desea definir el maximo número de usos de cada ascensor?')
        if respuesta == "si":
            self.MTF1 = int(input('indique el numero de usos del primer ascensor: '))
            self.MTF2 = int(input('indique el numero de usos del segundo ascensor: '))
            self.MTF3 = int(input('indique el numero de usos del tercer ascensor: '))
        else:
            print('los tiempos se asignarán por defecto')
            self.MTF1 = CONST_DEFAULT_MTF1
            self.MTF2 = CONST_DEFAULT_MTF2
            self.MTF3 = CONST_DEFAULT_MTF3

        respuesta = YesNoQuestion('¿Desea definir el numero de pisos?')
        if respuesta == "si":
            self.numberOfLevels = int(input('indique el numero de pisos: '))
        else:
            print('el numero de pisos se asignará por defecto')
            self.numberOfLevels = CONST_DEFAULT_NUMBER_LEVELS

        respuesta = YesNoQuestion('¿Desea definir el tiempo medio de llegadas de personas?')
        if respuesta == "si":
            self.timeBetweenArrivals = int(input('indique el numero de segundos entre llegadas: '))
        else:
            print('el numero de pisos se asignará por defecto')
            self.timeBetweenArrivals = CONST_DEFAULT_ARRIVAL_TIME

        respuesta = YesNoQuestion('¿Desea simular en tiempo real?')
        if respuesta == "si":
            self.instantSimulation = 0
        else:
            self.instantSimulation = 1

        respuesta = YesNoQuestion('¿Desea seleccionar un tiempo de simulación? Por defecto el tiempo será un dia')
        if respuesta == "si":
            months = int(input('indique el numero de meses de simulación (a continuación podrá escojer tiempos menores): '))
            days = int(input('indique el numero de dias de simulación (a continuación podrá escojer tiempos menores): '))
            hours = int(input('indique el numero de horas de simulación (a continuación podrá escojer tiempos menores): '))
            minutes = int(input('indique el numero de minutos de simulación: '))
            self.simulationTime = SimulationTime()
            self.simulationTime.setTimeByParameters(0, minutes, hours, days, months, 0)

        else:
            print('el tiempo de simulación se asignará por defecto')
            self.simulationTime = SimulationTime()
            self.simulationTime.setTimeByParameters(0, 0, 0, 1, 0, 0)

        print()

    def showParameters(self):
        print('----------------------------------------------------------------')
        print('-------------Simulador a mida - Simulació Ascensors-------------')
        print('----------------------------------------------------------------')
        print()

        print(f'Tiempo de transporte de los ascensores (por piso): {self.ascensorTransportTime} segundos')
        print()
        print('Los ascensores fallaran despues de los siguientes usos:')
        print(f' - Ascensor 1: {self.MTF1} usos')
        print(f' - Ascensor 2: {self.MTF2} usos')
        print(f' - Ascensor 3: {self.MTF3} usos')
        print()
        print(f'El numero de pisos es: {self.numberOfLevels} pisos')

        print('----------------------------------------------------------------')
        print('----------------------------------------------------------------')


def YesNoQuestion(question):
    print(question)
    answer = input()
    while answer != "si" and answer != "no":
        print("Escriba si o no")
        answer = input()
    return answer
