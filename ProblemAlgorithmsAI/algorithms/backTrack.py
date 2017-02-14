# The intent with these search functions is to create a generic framework that can
# be applied to any problem. It should be configured so that you can use both this search and the
# Node class without modification, provided you write problem specific code in the Problem class
from node import *

def BackTrackSearch(problem, testResult = None):
	if (testResult):
		testResult.maxNodes = 1
		testResult.finish("Fail")
	return BackTrack( problem, problem.initial, testResult )
	
def BackTrack(problem, state, testResult):
	if problem.isGoal(state):
		return state
	for action in problem.getActions(state):
		# Contraints are check in apply action
		newState = problem.applyAction( state, action )
		if (testResult):
			testResult.incTotalIterations()
			if (testResult.pastTimeLimit()):
				testResult.finish("TimeExpired")
				return None
		if newState:
			result = BackTrack(problem, state, testResult)
			if result:
				testResult.finish("Success")
				return result
		problem.undoLastAction(state)
