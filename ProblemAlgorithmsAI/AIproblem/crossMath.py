from AIproblem import *
from copy import deepcopy
from opDictionary import ops

class crossMath(AIproblem):
	def __init__(self, initialProblem, size, createCopy = True, evalFn=None, goal=None  ):
		self.initialProblem 	= initialProblem
		self.rows 				= initialProblem.rows
		self.cols 				= initialProblem.cols
		self.rowLength 			= len(self.rows)
		self.createCopy			= createCopy
		self.allPossibleActions = [ i for i in range(1,initialProblem.size+1) ]

		# Create an empty state of zeros
		emtpyRow = []
		for i in range(self.rowLength):
			emtpyRow.append(0)
		initialState = []
		for i in range(self.rowLength):
			initialState.append(deepcopy(emtpyRow))
		
		AIproblem.__init__(self, initialState, initialProblem.size)

	def getActions( self, state ) :
		if (state == None):
			return []

		usedActions = flatten(state)
		possibleActions = pruneActions(self.allPossibleActions, usedActions)
		[row, col] = findFirstZero(state, self.rowLength)
		if ( -1 == row) :
			#-1 indicates that there are no more blank spaces,
			# so there are no more remaining actions
			return []
		
		return possibleActions

	def applyAction ( self, state, action ) :
		# Modifies the state and then verifies if a completed row or column is still valid
		if not action :
			return
		else :
			# I am keeping the old newState so that we can easily apply other algorithms 
			if self.createCopy:
				newState = deepcopy(state)
			else:
				# newState just points to state
				newState = state
						
			[row, col] = findFirstZero(newState, self.rowLength)
			if ( -1 == row) :
				#-1 indicates that there are no more blank spaces,
				# so there are no more remaining actions
				return
			
			newState[row][col] = action
			
			# If the row is complete, validate it
			if ((col + 1) == self.rowLength):
				if (self.checkRow(newState[row], self.rows[row]) == False):
					return

			# If the column is complete, validate it
			if ((row + 1) == self.rowLength):
				flipped = list(zip(*newState))
				if (self.checkRow(flipped[col], self.cols[col]) == False):
					return
			
			return newState
		
	def undoLastAction(self, state):
		
		[row, col] = findFirstZero(state, self.rowLength)
		if ( -1 == row) :
			#-1 indicates that there are no more blank spaces,
			# so remove the last space
			state[self.rowLength - 1][self.rowLength - 1] = 0
			return state
		if (col > 0):
			state[row][col - 1] = 0
		else:
			state[row - 1][self.rowLength - 1] = 0
		
		return state

	def evaluation( self, state ):
		if not self.evalFn :
			return 0
		else :
			state.evaluate( state.evalFn )

	def isGoal ( self, state ):
		if (state == None):
			return False
		
		# Look for unfilled squares
		# If all cells have not yet been filled, not done yet
		[row, col] = findFirstZero(state, self.rowLength)
		if (-1 != row):
			return False
		
		# Check the row math
		if (self.checkRows(state, self.rows) == False):
			return False
			
		# Check the column math
		flipped = list(zip(*state))
		if (self.checkRows(flipped, self.cols) == False):
			return False
		return state
	
	def checkRows(self, state, puzzleRows):
		for r in range(len(state)):
			stateRow = state[r]
			puzzleRow = puzzleRows[r]
			if (self.checkRow(stateRow, puzzleRow) == False):
				return False
		return True

	def checkRow(self, stateRow, puzzleRow):
		operatorRow = puzzleRow[0]
		desiredAnswer = puzzleRow[1]
		rowLength = len(stateRow)
		total = stateRow[0]
		for i in range(rowLength - 1):
			total = ops[operatorRow[i]](total, stateRow[i+1])
		if total != desiredAnswer:
			return False
		return True
	
def printCrossMath(rows, cols, state):
	length = len(state)
	width = 5
	for i in range(length):
		boardrow = ''
		for j in range(length):
			boardrow += str(state[i][j]).rjust(width)
			if (j + 1 < length):
				boardrow += rows[i][0][j].rjust(2)
			else:
				boardrow += '='.rjust(2)
				boardrow += str(rows[i][1]).rjust(width)
		print(boardrow)

		boardrow = ''
		for j in range(length):
			if (i + 1 < length):
				boardrow += cols[j][0][i].rjust(width)
				boardrow += '  '
			else:
				boardrow += str('=').rjust(width)
				boardrow += '  '
		print(boardrow)
	
	boardrow = ''
	for j in range(length):
		boardrow += str(cols[j][1]).rjust(width)
		boardrow += '  '
	print(boardrow)

# This flattens a singly nested list
def flatten( Alist ):
	z = []
	for el in Alist:
		z.extend(el)
	return z

def findFirstZero(state, size) :
	for row in range(size) :
		for col in range(size) :
			if ( 0 == state[row][col] ) :
				# We found a zero, return its location
				return [row, col]

	# We did not find a zero
	return [-1, -1]

def pruneActions(possibleActions, pruneList):
	return list(set(possibleActions).difference(set(pruneList)))
