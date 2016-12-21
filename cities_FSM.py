#!/usr/bin/env python

#Calculate optimal route from Arad to Bucharest

#STATES
#Arad, Sibiu, Fagaras, Rimnicu_Vilcea, Pitesti, Bucharest

#TRANSITIONS
#Arad_Sibiu, Sibiu_Fagaras, Sibiu_RV, Fagars_Bucharest, RV_Pitesti, Pitesti_Bucharest


#Each State
#Goal state (boolean)
#City name
#Dist from Bucharest
#Neighboring cities

#Each Transition
#Number of miles traveled



########################
#STATES
########################
class City(object):
	def __init__(self,goal,name,dist_to_goal,neighbors):
		self.goal = goal
		self.name = name
		self.dist_to_goal = dist_to_goal
		self.neighbors = neighbors

	def print_stats(self):
		print("You are in " + self.name + ". You are " + str(self.dist_to_goal) + " miles from Bucharest.")

	def getName(self):
		return self.name

	def getGoal(self):
		return self.goal


########################
#TRANSITIONS
########################
class Transition(object):
	def __init__(self,start,end,dist_traveled):
		self.start = start
		self.end = end
		self.dist_traveled = dist_traveled

########################
#FSM
########################
class SimpleFSM(object):
	def __init__(self):
		self.states = {}
		self.transitions = {}
		self.curState = None
		self.trans = None

	def setState(self, stateName):
		self.curState = self.states[stateName]

	def setTrans(self, transName):
		self.trans = self.transitions[transName]

	def find_state_closest_to_goal(self):
		target_state = self.curState.neighbors[0]
		for state in self.curState.neighbors:
			if self.states[state].dist_to_goal < self.states[target_state].dist_to_goal:
				target_state = state
		return target_state

	def Execute(self):
		if (self.trans):
			self.setState(self.trans.end.getName())
			self.trans = None
		self.curState.print_stats()


class Traveler(object):
	def __init__(self):
		self.FSM = SimpleFSM()

	def set_destination(self):
		self.FSM.setTrans(self.FSM.curState.getName()+"_"+self.FSM.find_state_closest_to_goal())

	def travel(self):
		self.FSM.Execute()


if __name__ == "__main__":
	print("Initiating...")
	salesman = Traveler()

	Arad = City(False,"Arad",366,["Sibiu"])
	Sibiu = City(False,"Sibiu",253,["Fagaras", "RimnicuVilcea"])
	Fagaras = City(False,"Fagaras",176,["Sibiu", "Bucharest"])
	RimnicuVilcea = City(False,"RimnicuVilcea",193,["Sibiu", "Pitesti"])
	Pitesti = City(False,"Pitesti",100,["RimnicuVilcea", "Bucharest"])
	Bucharest = City(True,"Bucharest",0,["Fagaras", "Pitesti"])

	Arad_Sibiu = Transition(Arad,Sibiu,140)
	Sibiu_Fagaras = Transition(Sibiu,Fagaras,99)
	Sibiu_RimnicuVilcea = Transition(Sibiu,RimnicuVilcea,80)
	Fagaras_Bucharest = Transition(Fagaras,Bucharest,211)
	RimnicuVilcea_Pitesti = Transition(RimnicuVilcea,Pitesti,97)
	Pitesti_Bucharest = Transition(Pitesti,Bucharest,101)

	salesman.FSM.states["Arad"] = Arad
	salesman.FSM.states["Sibiu"] = Sibiu
	salesman.FSM.states["Fagaras"] = Fagaras
	salesman.FSM.states["RimnicuVilcea"] = RimnicuVilcea
	salesman.FSM.states["Pitesti"] = Pitesti
	salesman.FSM.states["Bucharest"] = Bucharest

	salesman.FSM.transitions["Arad_Sibiu"] = Arad_Sibiu
	salesman.FSM.transitions["Sibiu_Fagaras"] = Sibiu_Fagaras
	salesman.FSM.transitions["Sibiu_RV"] = Sibiu_RimnicuVilcea
	salesman.FSM.transitions["Fagaras_Bucharest"] = Fagaras_Bucharest
	salesman.FSM.transitions["RimnicuVilcea_Pitesti"] = RimnicuVilcea_Pitesti
	salesman.FSM.transitions["Pitesti_Bucharest"] = Pitesti_Bucharest

	salesman.FSM.setState("Arad")


	cities_visited = []
	while (not salesman.FSM.curState.getName() == "Bucharest"):
		cities_visited.append(salesman.FSM.curState.getName())
		salesman.set_destination()
		salesman.travel()

	print("You've arrived in Bucharest")
	for city in cities_visited:
		print(city)
