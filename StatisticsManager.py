import plotly.graph_objects as go
from Elevator import ElevatorState
from SimulatorManager import SimulatorManager


class StatisticsManager:
    def __init__(self, simulatorManager: SimulatorManager):
        self.simulatorManager = simulatorManager

    def showStatistics(self):
        for elevator in self.simulatorManager.elevators:
            print (elevator.name, "states times:")
            for state in ElevatorState:
                print (state, "", elevator.timeInState[state.value].getTimeInHoursAndLower())
            print("times broken:", elevator.timesBroken)
        print("")

        maxPeopleWaitingInFloors = []
        for floor in self.simulatorManager.floors:
            print("floor", floor.level, "max people waiting:", floor.maxPeopleWaiting)
            floorName ="floor " + str(floor.level)
            maxPeopleWaitingInFloors.append(floor.maxPeopleWaiting)

        params = {"y": maxPeopleWaitingInFloors}
        fig = go.Figure(go.Bar(params))
        fig.write_html('figures/first_figure.html', True)
