# valueIterationAgents.py
# -----------------------
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


# valueIterationAgents.py
# -----------------------
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


import mdp, util

from learningAgents import ValueEstimationAgent
import collections

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0
        self.runValueIteration()

    def runValueIteration(self):
        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        for i in range(self.iterations):
            val = self.values.copy()
            for state in self.mdp.getStates():
                actions = self.mdp.getPossibleActions(state)
                if len(actions) > 0:
                    max = self.computeQValueFromValues(state,actions[0])
                    for action in actions:
                        q = self.computeQValueFromValues(state, action)
                        if max <= q:
                            max = q
                            val[state] = q
            self.values = val

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]

    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        q = 0
        for state_, prob in self.mdp.getTransitionStatesAndProbs(state, action):
            reward = self.mdp.getReward(state, action, state_) + (self.discount*self.values[state_])
            q += prob * reward
        return q

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        if self.mdp.isTerminal(state):
            return None
        actions = self.mdp.getPossibleActions(state)
        final_Q = self.computeQValueFromValues(state, actions[0])
        final_action = actions[0]
        for action in actions:
            if final_Q < self.computeQValueFromValues(state, action):
                final_Q = self.computeQValueFromValues(state, action)
                final_action = action
        return final_action

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)

class AsynchronousValueIterationAgent(ValueIterationAgent):
    """
        * Please read learningAgents.py before reading this.*

        An AsynchronousValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs cyclic value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 1000):
        """
          Your cyclic value iteration agent should take an mdp on
          construction, run the indicated number of iterations,
          and then act according to the resulting policy. Each iteration
          updates the value of only one state, which cycles through
          the states list. If the chosen state is terminal, nothing
          happens in that iteration.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state)
              mdp.isTerminal(state)
        """
        ValueIterationAgent.__init__(self, mdp, discount, iterations)

    def runValueIteration(self):
        "*** YOUR CODE HERE ***"
        for i in range(self.iterations):
            val = self.values.copy()
            states = self.mdp.getStates()
            state = states[i%len(states)]
            actions = self.mdp.getPossibleActions(state)
            if len(actions) > 0:
                max = self.computeQValueFromValues(state,actions[0])
                for action in actions:
                    q = self.computeQValueFromValues(state, action)
                    if max <= q:
                        max = q
                        val[state] = q
            self.values = val


class PrioritizedSweepingValueIterationAgent(AsynchronousValueIterationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A PrioritizedSweepingValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs prioritized sweeping value iteration
        for a given number of iterations using the supplied parameters.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100, theta = 1e-5):
        """
          Your prioritized sweeping value iteration agent should take an mdp on
          construction, run the indicated number of iterations,
          and then act according to the resulting policy.
        """
        self.theta = theta
        ValueIterationAgent.__init__(self, mdp, discount, iterations)

    def runValueIteration(self):
        "*** YOUR CODE HERE ***"
        Pqueue = util.PriorityQueue()
        pred = {}

        for state in self.mdp.getStates():
            predSet = set()
            for predState in self.mdp.getStates():
                for action in self.mdp.getPossibleActions(predState):
                    for state_, prob in self.mdp.getTransitionStatesAndProbs(predState, action):
                        if state_ == state:
                            predSet.add(predState)
            pred[state] = predSet

            self.updateQueue(state,Pqueue)


        for i in range(self.iterations):
            if not Pqueue.isEmpty():
                s = Pqueue.pop()
                actions = self.mdp.getPossibleActions(s)


                if not self.mdp.isTerminal(s):
                    highQ = self.computeQValueFromValues(s,actions[0])
                    for action in actions:
                        q = self.computeQValueFromValues(s,action)
                        if q>=highQ:
                            highQ = q
                    self.values[s] = highQ

                for p in pred[s]:
                    self.updateQueue(p,Pqueue)


    def updateQueue(self, state, Pqueue):
        """ Updates Priority Queue of non-terminal state"""
        if not self.mdp.isTerminal(state):
            actions = self.mdp.getPossibleActions(state)
            final_Q = self.computeQValueFromValues(state, actions[0])
            for action in actions:
                if final_Q < self.computeQValueFromValues(state, action):
                    final_Q = self.computeQValueFromValues(state, action)
            diff = abs(self.values[state] - final_Q)
            Pqueue.update(state, -diff)
