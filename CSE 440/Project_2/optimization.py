# optimization.py
# ---------------
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


import numpy as np
import itertools

import pacmanPlot
import graphicsUtils
import util

# You may add any helper functions you would like here:
# def somethingUseful():
#     return True


def findIntersections(constraints):
    """
    Given a list of linear inequality constraints, return a list all
    intersection points.

    Input: A list of constraints. Each constraint has the form:
        ((a1, a2, ..., aN), b)
        where the N-dimensional point (x1, x2, ..., xN) is feasible
        if a1*x1 + a2*x2 + ... + aN*xN <= b for all constraints.
    Output: A list of N-dimensional points. Each point has the form:
        (x1, x2, ..., xN).
        If none of the constraint boundaries intersect with each other, return [].

    An intersection point is an N-dimensional point that satisfies the
    strict equality of N of the input constraints.
    This method must return the intersection points for all possible
    combinations of N constraints.

    """
    "*** YOUR CODE HERE ***"
    A = []
    b = []
    A_ = []
    b_ = []
    result = []
    result_ = []
    N = 0
    N_ = 0
    for constraint in constraints:
        A.append(constraint[0])
        b.append(constraint[1])
        N = N+1
    print(A,b)
    if np.linalg.matrix_rank(A) >= 2:
        recursiveConstraintIntersect(result,N_,A_,b_,0,A,constraints)
    for val in result:
        result_.append(tuple(val))
    return list(result_)

def recursiveConstraintIntersect(result, N_,A_,b_,counter,A, constraints):
    if N_ >= len(A[0]) or counter > len(constraints):
        return
    i = 0
    for item in constraints[counter:]:
        N_ = N_ + 1
        i = i + 1
        A_.append(item[0])
        b_.append(item[1])
        recursiveConstraintIntersect(result,N_,A_,b_,counter+i,A,constraints)
        if np.linalg.matrix_rank(A_) == N_ and len(A_[0]) == N_:
            result.append(np.linalg.solve(A_, b_))
        A_.pop()
        b_.pop()
        N_ = N_ - 1

def findFeasibleIntersections(constraints):
    """
    Given a list of linear inequality constraints, return a list all
    feasible intersection points.

    Input: A list of constraints. Each constraint has the form:
        ((a1, a2, ..., aN), b).
        where the N-dimensional point (x1, x2, ..., xN) is feasible
        if a1*x1 + a2*x2 + ... + aN*xN <= b for all constraints.

    Output: A list of N-dimensional points. Each point has the form:
        (x1, x2, ..., xN).

        If none of the lines intersect with each other, return [].
        If none of the intersections are feasible, return [].

    You will want to take advantage of your findIntersections function.

    """
    "*** YOUR CODE HERE ***"
    result_ = []
    result_2 = []
    result = findIntersections(constraints)
    for posible in result:
        for constraint in constraints:
            if np.dot(constraint[0],posible) > constraint[1]:
                if posible not in result_:
                    result_.append(posible)
    for val in result:
        if val not in result_:
            result_2.append(val)
    return result_2

def solveLP(constraints, cost):
    """
    Given a list of linear inequality constraints and a cost vector,
    find a feasible point that minimizes the objective.

    Input: A list of constraints. Each constraint has the form:
        ((a1, a2, ..., aN), b).
        where the N-dimensional point (x1, x2, ..., xN) is feasible
        if a1*x1 + a2*x2 + ... + aN*xN <= b for all constraints.

        A tuple of cost coefficients: (c1, c2, ..., cN) where
        [c1, c2, ..., cN]^T is the cost vector that helps the
        objective function as cost^T*x.

    Output: A tuple of an N-dimensional optimal point and the 
        corresponding objective value at that point.
        One N-demensional point (x1, x2, ..., xN) which yields
        minimum value for the objective function.

        Return None if there is no feasible solution.
        You may assume that if a solution exists, it will be bounded,
        i.e. not infinity.

    You can take advantage of your findFeasibleIntersections function.

    """
    "*** YOUR CODE HERE ***"

    results = findFeasibleIntersections(constraints)
    solution = None
    if len(results) > 0:
        val = np.dot(results[0],cost)
    for result in results:
        current = np.dot(result,cost)
        if val >= current:
            val = current
            solution = (result,current)
    return solution

def wordProblemLP():
    """
    Formulate the work problem in the write-up as a linear program.
    Use your implementation of solveLP to find the optimal point and
    objective function.

    Output: A tuple of optimal point and the corresponding objective
        value at that point.
        Specifically return:
            ((sunscreen_amount, tantrum_amount), maximal_utility)

        Return None if there is no feasible solution.
        You may assume that if a solution exists, it will be bounded,
        i.e. not infinity.

    """
    "*** YOUR CODE HERE ***"
    constraints = [((-1,0),-20), ((0,-1),-15.5), ((2.5,2.5),100), ((0.5,0.25),50)]
    cost = (-7,-4)
    solution = solveLP(constraints, cost)
    result = [0,0]
    result[0] = solution[0]
    result[1] = -solution[1]
    return result

def solveIP(constraints, cost):
    """
    Given a list of linear inequality constraints and a cost vector,
    use the branch and bound algorithm to find a feasible point with
    interger values that minimizes the objective.

    Input: A list of constraints. Each constraint has the form:
        ((a1, a2, ..., aN), b).
        where the N-dimensional point (x1, x2, ..., xN) is feasible
        if a1*x1 + a2*x2 + ... + aN*xN <= b for all constraints.

        A tuple of cost coefficients: (c1, c2, ..., cN) where
        [c1, c2, ..., cN]^T is the cost vector that helps the
        objective function as cost^T*x.

    Output: A tuple of an N-dimensional optimal point and the 
        corresponding objective value at that point.
        One N-demensional point (x1, x2, ..., xN) which yields
        minimum value for the objective function.

        Return None if there is no feasible solution.
        You may assume that if a solution exists, it will be bounded,
        i.e. not infinity.

    You can take advantage of your solveLP function.

    """
    "*** YOUR CODE HERE ***"
    solution = solveLP(constraints, cost)
    solution_found = True
    counter = 0
    if solution is None:
        return None
    for val in solution[0]:
        if not integerCheck(val):
           solution_found = False
    if not solution_found:
        for val in solution[0]:
            counter = counter + 1
            if not integerCheck(val):
                ceil_constraints = makeConstriantCeil(counter, val, constraints)
                ceil_solution = solveIP(ceil_constraints, cost)
                floor_constraints = makeConstriantFloor(counter, val, constraints)
                floor_solution = solveIP(floor_constraints, cost)
                if ceil_solution is not None:
                    if floor_solution is not None:
                        if ceil_solution[1] < floor_solution[1]:
                            return ceil_solution
                        if ceil_solution[1] > floor_solution[1]:
                            return floor_solution
                    else:
                        return ceil_solution
                if floor_solution is not None:
                    return floor_solution
        return None

    else:
        return solution

def integerCheck(value):
    if (np.ceil(value) - value) < np.power(10.0, -12):
        return True
    if (value - np.floor(value)) < np.power(10.0, -12):
        return True
    return False

def makeConstriantCeil(counter, val, constraints):
    new_one = []
    new_two = []
    value = -np.ceil(val)
    temp_constraints = constraints.copy()
    sub_counter = counter
    for i in constraints[0][0]:
        sub_counter = sub_counter - 1
        if sub_counter is 0:
            new_one.append(-1)
            new_two.append(1)
        else:
            new_one.append(0)
            new_two.append(0)
    temp_constraints.append((tuple(new_one),value))
    temp_constraints.append((tuple(new_two),-value))
    return temp_constraints

def makeConstriantFloor(counter, val, constraints):
    new_one = []
    new_two = []
    value = np.floor(val)
    temp_constraints = constraints.copy()
    sub_counter = counter
    for i in constraints[0][0]:
        sub_counter = sub_counter - 1
        if sub_counter is 0:
            new_one.append(1)
            new_two.append(-1)
        else:
            new_one.append(0)
            new_two.append(0)
    temp_constraints.append((tuple(new_one), value))
    temp_constraints.append((tuple(new_two), -value))
    return temp_constraints

def wordProblemIP():
    """
    Formulate the work problem in the write-up as a linear program.
    Use your implementation of solveIP to find the optimal point and
    objective function.

    Output: A tuple of optimal point and the corresponding objective
        value at that point.
        Specifically return:
        ((f_DtoG, f_DtoS, f_EtoG, f_EtoS, f_UtoG, f_UtoS), minimal_cost)

        Return None if there is no feasible solution.
        You may assume that if a solution exists, it will be bounded,
        i.e. not infinity.

    """
    "*** YOUR CODE HERE ***"
    truck_limit = 30
    W = (1.2, 1.3, 1.1)
    C = (15, 30)
    T = [(12, 20), (4,5), (2,1)]

    return foodDistribution(truck_limit, W, C,T)

def foodDistribution(truck_limit, W, C, T):
    """
    Given M food providers and N communities, return the integer
    number of units that each provider should send to each community
    to satisfy the constraints and minimize transportation cost.

    Input:
        truck_limit: Scalar value representing the weight limit for each truck
        W: A tuple of M values representing the weight of food per unit for each 
            provider, (w1, w2, ..., wM)
        C: A tuple of N values representing the minimal amount of food units each
            community needs, (c1, c2, ..., cN)
        T: A list of M tuples, where each tuple has N values, representing the 
            transportation cost to move each unit of food from provider m to
            community n:
            [ (t1,1, t1,2, ..., t1,n, ..., t1N),
              (t2,1, t2,2, ..., t2,n, ..., t2N),
              ...
              (tm,1, tm,2, ..., tm,n, ..., tmN),
              ...
              (tM,1, tM,2, ..., tM,n, ..., tMN) ]

    Output: A length-2 tuple of the optimal food amounts and the corresponding objective
            value at that point: (optimial_food, minimal_cost)
            The optimal food amounts should be a single (M*N)-dimensional tuple
            ordered as follows:
            (f1,1, f1,2, ..., f1,n, ..., f1N,
             f2,1, f2,2, ..., f2,n, ..., f2N,
             ...
             fm,1, fm,2, ..., fm,n, ..., fmN,
             ...
             fM,1, fM,2, ..., fM,n, ..., fMN)

            Return None if there is no feasible solution.
            You may assume that if a solution exists, it will be bounded,
            i.e. not infinity.

    You can take advantage of your solveIP function.

    """
    M = len(W)
    N = len(C)
    constraints = []
    total_food_it = 0
    place = 0
    constraint = [0]*(M*N)
    cost = constraint.copy()
    weight_constraint = constraint.copy()
    food_constraints = constraint.copy()
    for i in range(M*N):
        pos_constraint = constraint.copy()
        pos_constraint[i] = -1
        constraints.append((tuple(pos_constraint), -0.0))
        if i % (M) == 0:
            if i != 0:
                constraints.append((tuple(food_constraints), -C[total_food_it]))
                #constraints.append((tuple(weight_constraint), truck_limit))
                total_food_it = total_food_it + 1
                place = place + 1
            food_constraints = constraint.copy()
            #weight_constraint = constraint.copy()
        weight_constraint[i] = W[i%M]
        food_constraints[i] = -1
        cost[i] = T[i%M][place]
        if i == ((M*N)-1):
            constraints.append((tuple(food_constraints), -C[total_food_it]))
    constraints.append((tuple(weight_constraint), truck_limit))
    return solveIP(constraints, cost)


if __name__ == "__main__":
    constraints = [((3, 2), 10),((1, -9), 8),((-3, 2), 40),((-3, -1), 20)]
    inter = findIntersections(constraints)
    print(inter)
    print()
    valid = findFeasibleIntersections(constraints)
    print(valid)
    print()
    print(solveLP(constraints, (3,5)))
    print()
    print(solveIP(constraints, (3,5)))
    print()
    print(wordProblemIP())
