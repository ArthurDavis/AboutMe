# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    o_list=util.Stack() #create open list in stack form, new entries added to front
    o_list.push((problem.getStartState(), [])) #push the first state/node to open list

    c_list=[] #initialize closed list
    c_list.append(problem.getStartState())

    while not o_list.isEmpty(): #and not problem.isGoalState(current_node):
        node, actions = o_list.pop() #pop the location and actions of next node from open
        if problem.isGoalState(node):
            return actions
        for succ_node, nsew, cost in problem.getSuccessors(node): 
            if not succ_node in c_list: #checks that successor is not on closed list
                o_list.push((succ_node, actions+[nsew])) #push the next node with information of how to get there
                c_list.append(node)
    return []

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    o_list=util.Queue() #create open list in queue form, new entries added to end
    o_list.push((problem.getStartState(), [])) #push the first node to open list w empty actions to get there

    c_list=[] #initialize closed list
    c_list.append(problem.getStartState())

    while not o_list.isEmpty():
        node, actions = o_list.pop() #pop the location and actions of next node from open
        if problem.isGoalState(node): #checks to see if that node is the goal state
            return actions
        for succ_node, nsew, cost in problem.getSuccessors(node): 
            if not succ_node in c_list: #checks that successor is not on closed list
                o_list.push((succ_node, actions+[nsew])) #push the next node with information of how to get there
                c_list.append(succ_node)
    return []

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    o_list = util.PriorityQueue()
    o_list.push((problem.getStartState(),[],0), 0)

    c_list = []

    while not o_list.isEmpty():
        node, actions, cost = o_list.pop() #pop location, actions and cost of next node from open
        if problem.isGoalState(node): #checks to see if that node is the goal state
            return actions

        if not node in c_list: #if the node is unexplored
            c_list.append(node) #mark as explored
            for succ_node, nsew, succ_cost in problem.getSuccessors(node): #push successors to open list
                o_list.push((succ_node, actions+[nsew], cost + succ_cost), cost + succ_cost)
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    o_list = util.PriorityQueue()
    o_list.push((problem.getStartState(),[],0), 0)

    c_list = []

    while not o_list.isEmpty():
        node, actions, cost = o_list.pop() #pop location, actions and cost of next node from open
        if problem.isGoalState(node): #pop location, actions and cost of next node from open
            return actions

        if not node in c_list: #if the node is unexplored
            c_list.append(node) #mark as explored
            for succ_node, nsew, succ_cost in problem.getSuccessors(node): #push successors to open list
                o_list.push((succ_node, actions+[nsew], cost + succ_cost), heuristic(succ_node, problem) + cost + succ_cost)
    return []
   

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
