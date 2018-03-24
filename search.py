# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    startState = problem.getStartState()
    expandedStatesInfo = {}     # state:(fromState,fromDir)
    stack = util.Stack()
    "stack entry : (state,fromState,fromDir)"    
    stack.push((startState, "", ""))
    
    while True:
        try: expState,fromState,fromDir = stack.pop()
        except IndexError:
            print "No goal state found!!"
            raise
        print "expState : ", expState, fromState, fromDir

        if expState in expandedStatesInfo:
            print "already expanded : ", expState
            continue

        print "adding to expandedStatesInfo : ", expState
        expandedStatesInfo[expState] = (fromState,fromDir)

        if problem.isGoalState(expState):
            print "reached goal state : ", expState
            break

        # handle the fringes
        fringesInfo = problem.getSuccessors(expState)
        print "fringesInfo : ", fringesInfo
        for fringeState, fringeDir, fringeCostLocal in fringesInfo:
            print "fringeState : ", fringeState, fringeDir, fringeCostLocal
            stack.push((fringeState,expState,fringeDir))
        # print "stack : ", stack.list

    assert problem.isGoalState(expState)

    # backtrack the path
    path = []
    state = expState
    while state != startState:
        fromState, fromDir = expandedStatesInfo[state]
        print "adding to path : ", state, fromState, fromDir
        path.append(fromDir)
        state = fromState

    path.reverse()
    print "path : ", path
    return path

# def depthFirstSearch(problem):
#     """
#     Search the deepest nodes in the search tree first.

#     Your search algorithm needs to return a list of actions that reaches the
#     goal. Make sure to implement a graph search algorithm.

#     To get started, you might want to try some of these simple commands to
#     understand the search problem that is being passed in:

#     print "Start:", problem.getStartState()
#     print "Is the start a goal?", problem.isGoalState(problem.getStartState())
#     print "Start's successors:", problem.getSuccessors(problem.getStartState())
#     """
#     "*** YOUR CODE HERE ***"
#     print "Start:", problem.getStartState()
#     print "Is the start a goal?", problem.isGoalState(problem.getStartState())
#     print "Start's successors:", problem.getSuccessors(problem.getStartState())

#     startState = problem.getStartState()
#     currState = startState
#     precededBy = {}
#     stack = util.Stack()
#     coveredStates = set()
    
#     while not problem.isGoalState(currState):
#         print "currState : ", currState
#         coveredStates.add(currState)
#         successors = problem.getSuccessors(currState)
#         print "successors : ", successors
#         for successor,direction,cost in successors:
#             print "successor : ", successor
#             if successor not in coveredStates:
#                 precededBy[successor] = currState, direction
#                 stack.push(successor)
#         print "stack : ", stack.list
#         try:
#             currState = stack.pop()
#         except IndexError:
#             print "No goal state found!!"
#             raise

#     assert problem.isGoalState(currState)
#     print "goal state : ", currState
#     reversePath = []
#     while currState != startState:
#         currState,direction = precededBy[currState]
#         print currState, ":", direction
#         reversePath.append(direction)
#         print "reversePath: ", reversePath
#     # print "reversePath:", reversePath
#     reversePath.reverse()
#     return reversePath

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    startState = problem.getStartState()
    expandedStatesInfo = {}     # state:(fromState,fromDir)
    queue = util.Queue()
    "queue entry : (state,fromState,fromDir)"    
    queue.push((startState, "", ""))
    
    while True:
        try: expState,fromState,fromDir = queue.pop()
        except IndexError:
            print "No goal state found!!"
            raise
        print "expState : ", expState, fromState, fromDir

        if expState in expandedStatesInfo:
            print "already expanded : ", expState
            continue

        print "adding to expandedStatesInfo : ", expState
        expandedStatesInfo[expState] = (fromState,fromDir)

        if problem.isGoalState(expState):
            print "reached goal state : ", expState
            break

        # handle the fringes
        fringesInfo = problem.getSuccessors(expState)
        print "fringesInfo : ", fringesInfo
        for fringeState, fringeDir, fringeCostLocal in fringesInfo:
            print "fringeState : ", fringeState, fringeDir, fringeCostLocal
            queue.push((fringeState,expState,fringeDir))
        # print "queue : ", queue.list

    assert problem.isGoalState(expState)

    # backtrack the path
    path = []
    state = expState
    while state != startState:
        fromState, fromDir = expandedStatesInfo[state]
        print "adding to path : ", state, fromState, fromDir
        path.append(fromDir)
        state = fromState

    path.reverse()
    print "path : ", path
    return path

# def breadthFirstSearch(problem):
#     """Search the shallowest nodes in the search tree first."""
#     "*** YOUR CODE HERE ***"
#     print "Start:", problem.getStartState()
#     print "Is the start a goal?", problem.isGoalState(problem.getStartState())
#     print "Start's successors:", problem.getSuccessors(problem.getStartState())

#     startState = problem.getStartState()
#     currState = startState
#     precededBy = {}
#     queue = util.Queue()
#     coveredStates = set()
    
#     while not problem.isGoalState(currState):
#         print "currState : ", currState
#         if currState in coveredStates:
#             print "state already covered"
#             continue
#         coveredStates.add(currState)
#         successors = problem.getSuccessors(currState)
#         print "successors : ", successors
#         for successor,direction,cost in successors:
#             print "successor : ", successor
#             if successor not in coveredStates:
#                 print "successor not covered"
#                 precededBy[successor] = currState, direction
#                 queue.push(successor)
#             else: print "successor covered"
#         print "queue : ", queue.list
#         try:
#             currState = queue.pop()
#         except IndexError:
#             print "No goal state found!!"
#             raise

#     assert problem.isGoalState(currState)
#     print "goal state : ", currState
#     reversePath = []
#     while currState != startState:
#         currState,direction = precededBy[currState]
#         print currState, ":", direction
#         reversePath.append(direction)
#         print "reversePath: ", reversePath
#     # print "reversePath:", reversePath
#     reversePath.reverse()
#     return reversePath


# def uniformCostSearch(problem):
#     """Search the node of least total cost first."""
#     "*** YOUR CODE HERE ***"
#     startState = problem.getStartState()
#     currState = startState
#     precededBy = {}
#     priorityQueue = util.PriorityQueue()
#     coveredStates = set()
#     stateCosts = {}
#     stateCosts[startState] = 0
    
#     while not problem.isGoalState(currState):
#         print "currState : ", currState
#         coveredStates.add(currState)
#         successors = problem.getSuccessors(currState)
#         print "successors : ", successors
#         for successor,direction,cost in successors:
#             print "successor : ", successor
#             if successor not in coveredStates:
#                 precededBy[successor] = currState, direction
#                 totalCost = stateCosts[currState] + cost
#                 print "totalCost :", totalCost
#                 priorityQueue.push(successor, totalCost)
#                 stateCosts[successor] = totalCost
                
#         print "priorityQueue : ", priorityQueue.heap
#         try:
#             currState = priorityQueue.pop()
#         except IndexError:
#             print "No goal state found!!"
#             raise

#     assert problem.isGoalState(currState)
#     print "goal state : ", currState
#     reversePath = []
#     while currState != startState:
#         currState,direction = precededBy[currState]
#         print currState, ":", direction
#         reversePath.append(direction)
#         print "reversePath: ", reversePath
#     # print "reversePath:", reversePath
#     reversePath.reverse()
#     return reversePath

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    startState = problem.getStartState()
    expandedStatesInfo = {}     # state:(fromState,fromDir,costTillState)
    priorityQ = util.PriorityQueueWithFunction( lambda x: x[3] )
    "priorityQ entry : (state,fromState,fromDir,costTillState)"    
    priorityQ.push((startState, "", "", 0))
    
    while True:
        try: expState,fromState,fromDir,costTillExpState = priorityQ.pop()
        except IndexError:
            print "No goal state found!!"
            raise
        print "expState : ", expState, fromState, fromDir, costTillExpState

        if expState in expandedStatesInfo:
            print "already expanded : ", expState
            continue

        print "adding to expandedStatesInfo : ", expState
        expandedStatesInfo[expState] = (fromState,fromDir,costTillExpState)

        if problem.isGoalState(expState):
            print "reached goal state : ", expState
            break

        # handle the fringes
        fringesInfo = problem.getSuccessors(expState)
        print "fringesInfo : ", fringesInfo
        for fringeState, fringeDir, fringeCostLocal in fringesInfo:
            print "fringeState : ", fringeState, fringeDir, fringeCostLocal
            fringeCostTotal = costTillExpState + fringeCostLocal
            print "fringeCostTotal :", fringeCostTotal
            priorityQ.push((fringeState,expState,fringeDir,fringeCostTotal))
        # print "priorityQ : ", priorityQ.heap

    assert problem.isGoalState(expState)

    # back-track the path
    path = []
    state = expState
    while state != startState:
        fromState, fromDir, costTillState = expandedStatesInfo[state]
        print "adding to path : ", state, fromState, fromDir
        path.append(fromDir)
        state = fromState

    path.reverse()
    print "path : ", path
    return path


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    startState = problem.getStartState()
    expandedStatesInfo = {}     # state:(fromState,fromDir,costTillState)
    priorityQ = util.PriorityQueueWithFunction( lambda x: x[3] + x[4] )
    "priorityQ entry : (state,fromState,fromDir,costTillState,heuristic)"    
    priorityQ.push((startState, "", "", 0, heuristic(startState,problem)))
    
    while True:
        try: expState,fromState,fromDir,costTillExpState,h = priorityQ.pop()
        except IndexError:
            print "No goal state found!!"
            raise
        print "expState : ", expState, fromState, fromDir, costTillExpState, heuristic

        if expState in expandedStatesInfo:
            earlierFoundCost = expandedStatesInfo[expState][2]
            print "already expanded : ", expState, " : cost : ", earlierFoundCost
            if earlierFoundCost <= costTillExpState: continue

        print "adding to expandedStatesInfo : ", expState
        expandedStatesInfo[expState] = (fromState,fromDir,costTillExpState)

        if problem.isGoalState(expState):
            print "reached goal state : ", expState
            break

        # handle the fringes
        fringesInfo = problem.getSuccessors(expState)
        print "fringesInfo : ", fringesInfo
        for fringeState, fringeDir, fringeCostLocal in fringesInfo:
            print "fringeState : ", fringeState, fringeDir, fringeCostLocal
            fringeCostTotal = costTillExpState + fringeCostLocal
            print "fringeCostTotal:",fringeCostTotal,"=",costTillExpState,"+",fringeCostLocal
            priorityQ.push((fringeState,expState,fringeDir,fringeCostTotal,heuristic(fringeState,problem)))
        # print "priorityQ : ", priorityQ.heap

    assert problem.isGoalState(expState)

    # back-track the path
    path = []
    state = expState
    while state != startState:
        fromState, fromDir, costTillState = expandedStatesInfo[state]
        print "adding to path : ", state, fromState, fromDir
        path.append(fromDir)
        state = fromState

    path.reverse()
    print "path : ", path
    return path

# def aStarSearch(problem, heuristic=nullHeuristic):
#     """Search the node that has the lowest combined cost and heuristic first."""
#     "*** YOUR CODE HERE ***"
#     startState = problem.getStartState()
#     currState = startState
#     precededBy = {}
#     priorityQueue = util.PriorityQueue()
#     coveredStates = set()
#     stateCosts = {}
#     stateCosts[startState] = 0
    
#     while not problem.isGoalState(currState):
#         print "currState : ", currState
#         coveredStates.add(currState)
#         successors = problem.getSuccessors(currState)
#         print "successors : ", successors
#         for successor,direction,cost in successors:
#             print "successor : ", successor
#             if successor not in coveredStates:
#                 precededBy[successor] = currState, direction
#                 # totalCost = cost + heuristic(successor, problem)
#                 totalCost = stateCosts[currState] + cost + heuristic(successor, problem)
#                 print "totalCost :", totalCost
#                 priorityQueue.push(successor, totalCost)
#                 stateCosts[successor] = totalCost
                
#         print "priorityQueue : ", priorityQueue.heap
#         try:
#             currState = priorityQueue.pop()
#         except IndexError:
#             print "No goal state found!!"
#             raise

#     assert problem.isGoalState(currState)
#     print "goal state : ", currState
#     reversePath = []
#     while currState != startState:
#         currState,direction = precededBy[currState]
#         print currState, ":", direction
#         reversePath.append(direction)
#         print "reversePath: ", reversePath
#     # print "reversePath:", reversePath
#     reversePath.reverse()
#     return reversePath


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
