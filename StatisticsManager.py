import plotly.graph_objects as go
import plotly.express as px
from Elevator import ElevatorState
from SimulatorManager import SimulatorManager
#matplotlib


class StatisticsManager:
    def __init__(self, simulatorManager: SimulatorManager):
        self.simulatorManager = simulatorManager

    def showStatistics(self):
        elevatorBrokenTimes = []
        elevatorNames = []
        for elevator in self.simulatorManager.elevators:
            elevatorNames.append(elevator.name)
            elevatorBrokenTimes.append(elevator.timesBroken)
            print (elevator.name, "states times:")
            elevatorStatesTime = []
            stateNames = []
            for state in ElevatorState:
                stateNames.append(state.getName())
                print (state, "", elevator.timeInState[state.getNum()].getTimeInHoursAndLower())
                elevatorStatesTime.append(elevator.timeInState[state.getNum()].getTimeInHoursDouble())
            self.createElevatorStatesChart(elevator.name, stateNames, elevatorStatesTime)
            print("times broken:", elevator.timesBroken)
            print("")
        print("")

        self.createElevatorBrokenTimesChart(elevatorNames, elevatorBrokenTimes)
        self.createMaxPeopleWaitingChart()

    def createElevatorStatesChart(self, elevatorName, stateNames, elevatorStatesTime):
        title = "State times in " + elevatorName
        fig = px.pie(values=elevatorStatesTime, names=stateNames, title=title)
        chartName = "figures/" + self.simulatorManager.timeManager.initialTime.getDateAsFileName() + "_" + elevatorName + "_states.html"
        fig.write_html(chartName)

    def createElevatorBrokenTimesChart(self, elevatorNames, elevatorBrokenTimes):
        params = {"y": elevatorBrokenTimes,
                  "name": "Times broken each elevator",
                  "showlegend": True,
                  "text": elevatorNames,
                  "ids": elevatorNames,
                  "hovertext": elevatorNames}
        fig = go.Figure(go.Bar(params))
        chartName = "figures/" + self.simulatorManager.timeManager.initialTime.getDateAsFileName() + "_ElevatorBrokenTimes.html"
        fig.write_html(chartName, True)

    def createMaxPeopleWaitingChart(self):
        maxPeopleWaitingInFloors = []
        floorNames = []
        for floor in self.simulatorManager.floors:
            print("floor", floor.level, "max people waiting:", floor.maxPeopleWaiting)
            floorName ="Floor " + str(floor.level)
            maxPeopleWaitingInFloors.append(floor.maxPeopleWaiting)
            floorNames.append(floorName)

        params = {"y": maxPeopleWaitingInFloors,
                  "name": "Max people waiting in each floor",
                  "showlegend": True,
                  "text": floorNames,
                  "ids": floorNames,
                  "hovertext": floorNames}
        fig = go.Figure(go.Bar(params))
        chartName = "figures/" + self.simulatorManager.timeManager.initialTime.getDateAsFileName() + "_maxPeopleWaiting.html"
        fig.write_html(chartName, True)
