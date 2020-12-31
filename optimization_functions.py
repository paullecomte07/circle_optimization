# -*- coding: utf-8 -*-

"""Ce fichier rassemble les algorithmes d'optimisation que nous utilisons pour répondre au problème
   Certaines fonctions nous ont été données par Mme Bernardetta"""

import pyomo.environ as pe
from pyomo.opt import SolverFactory
from pyomo.opt import SolverStatus, TerminationCondition
import os, sys

sys.path.insert(0,os.path.abspath(os.path.join(os.path.abspath(''),'../utilities')))

from optmodel_utilities import *

def create_solver(solver_name = 'cplex'):
    solver_path = get_solver_path(solver_name)
    return  SolverFactory(solver_name, executable=str(solver_path), solver_io = 'nl')


def check_if_optimal(results):
    ok = (results.solver.status == pe.SolverStatus.ok)
    optimal = (results.solver.termination_condition
               == pe.TerminationCondition.optimal)
    return  (ok and optimal)

def random_point(model, gen_multi):
    for i in model.N:
        model.x[i] = gen_multi.uniform(model.lb, model.ub)
        
def multistart(mymodel, iter, gen_multi, localsolver, labels,
               logfile = None, epsilon = 10**-4):

    algo_name = "Multi:"
    bestpoint = {}
    best_obj = sys.float_info.max
    nb_solution = 0
    feasible = False

    for it in range(1,iter+1):
        random_point(mymodel, gen_multi)
        results = localsolver.solve(mymodel, load_solutions=True)
        if check_if_optimal(results):
            nb_solution += 1
            obj = mymodel.obj()
            feasible = True
            print(algo_name + " Iteration ", it, " current value ", obj, end = '', file = logfile)
            if obj  < best_obj - epsilon: 
                best_obj = obj
                print(" *" , file = logfile)
                printPointFromModel(mymodel, logfile)
                StorePoint(mymodel, bestpoint, labels)
            else:
                print(file = logfile)
        else:
            print(algo_name+" Iteration ", it, "No feasible solution", file = logfile)

    if feasible == True:
        print(algo_name + " Best record found  {0:8.4f}".format(best_obj))
        LoadPoint(mymodel, bestpoint)
        printPointFromModel(mymodel)
    else:
        print(algo_name + " No feasible solution found by local solver")
        
    print(algo_name + " Total number of feasible solutions ", nb_solution)

    return feasible



""" Nous utilisons ces cercles comme point de départ pour l'instant"""
def init_points(model, init_circles):
    (matrice,r) = init_circles
    model.r = r
    i=0
    for point in matrice:
        model.x[i] = point.x
        model.y[i] = point.y
        i=i+1

def monotonic_basin_hopping(mymodel, iter, init_values, localsolver, labels, logfile = None, epsilon = 10**-4):
    
    algo_name = "MBH:"
    bestpoint = {}
    best_obj = sys.float_info.max
    it = 0
    init_points(mymodel, init_values)
    
    while it < iter+1 :
        #best_obj = Locally_generate(obj)
        #best_obj = L(best_obj)
        localsolver.solve(mymodel, load_solutions=True)
        obj = mymodel.obj()
        
        print(algo_name + " Iteration ", it, " current value ", obj, end = '', file = logfile)
        if obj < best_obj - epsilon:
            best_obj = obj
            print(" *" , file = logfile)
            printPointFromModel(mymodel, logfile)
            StorePoint(mymodel, bestpoint, labels)
            it = 0
        else:
            print(file = logfile)
            it = it + 1
            
    print(algo_name +" Best record found  {0:8.4f}".format(best_obj))
    LoadPoint(mymodel, bestpoint)
    printPointFromModel(mymodel)
            
    return True
 