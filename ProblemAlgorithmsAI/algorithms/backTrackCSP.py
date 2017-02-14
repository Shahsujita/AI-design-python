# The intent with these search functions is to create a generic framework that can
# be applied to any problem. It should be configured so that you can use both this search and the
# Node class without modification, provided you write problem specific code in the Problem class
from node import *

def BackTrackCSPSearch(problem, testResult = None):
	return BackTrackCSP( problem, problem.initial, testResult )

def BackTrackCSP(problem, state):
	if problem.isGoal(state):
		return state
	for action in problem.getActions(state):
		actionList = []
		# Contraints are check in apply action
		newState = problem.applyAction( state, action, actionList)
		# TODO runInference needs to be implented in the CSP, it will append to the actionList
		inferenceSuccss = problem.runInference(state, actionList)
		if inferenceSuccss:
			result = BackTrackCSP(problem, state)
			if result:
				return result
		for undoAction in actionList:
			state = problem.undoAction(state, undoAction)