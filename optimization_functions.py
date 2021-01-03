# -*- coding: utf-8 -*-

"""Ce fichier rassemble les algorithmes d'optimisation que nous utilisons pour répondre au problème
   Certaines fonctions nous ont été données par Mme Bernardetta"""

import pyomo.environ as pe
from pyomo.opt import SolverFactory
from pyomo.opt import SolverStatus, TerminationCondition

import matplotlib.pyplot as plt
from cercle import Cercle
from display_circle import display_circles

from sphere import Sphere
from display_sphere import display_spheres


import os, sys, random


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
def init_points(model, init_values, is3D):
        (matrice,r) = init_values
        model.r = r
        i=1
        for point in matrice:
            model.x[i] = point.x
            model.y[i] = point.y
            if (is3D):
                print("test")
                model.z[i] = point.z
            i=i+1
                

def from_pyomo_model_to_class(model, is3D):
    """
    Convert pyomo model points to instance of Cercle class in order to work easily with it
    """
    matrice = []
    for i in range(1,len(model.x)+1):
        if (is3D) :
            matrice.append(Sphere(model.x[i].value, model.y[i].value, model.z[i].value, model.r.value))
        else :
            matrice.append(Cercle(model.x[i].value, model.y[i].value, model.r.value))
    return matrice, model.r.value

def perturbate_points(model, is3D):
    delta = 0.3
    for i in range (1,model.n +1) :
        model.x[i] = pe.value(model.x[i]) + random.uniform(-delta, delta)
        model.y[i] = pe.value(model.y[i]) + random.uniform(-delta, delta)
        if (is3D):
            model.z[i] = pe.value(model.z[i]) + random.uniform(-delta, delta)

def monotonic_basin_hopping(mymodel, iter_max, init_values, localsolver, labels, logfile = None, epsilon = 10**-4, is3D = False):

    algo_name = "MBH:"
    bestpoint = {}
    best_obj = sys.float_info.max
    nb_iter = 0
    #count the number of optimization task
    counter = 0
    init_points(mymodel, init_values, is3D)

    while nb_iter < iter_max+1 :

        perturbate_points(mymodel, is3D)
        localsolver.solve(mymodel, load_solutions=True)
        obj = mymodel.obj()

        print(algo_name + " Iteration ", nb_iter, " current value ", obj, end = '', file = logfile)
        if obj < best_obj - epsilon:
            counter +=1
            best_obj = obj
            print(" *" , file = logfile)
            printPointFromModel(mymodel, logfile)
            StorePoint(mymodel, bestpoint, labels)
            matrice, r = from_pyomo_model_to_class(mymodel, is3D)
            if not is3D :
                display_circles(matrice, r)
            else:
                display_spheres(matrice, r)
            #plt.title("Iteration number :{}".format(str(counter)))
            nb_iter = 0

        else:
            print(file = logfile)
            nb_iter = nb_iter + 1



    print(algo_name +" Best record found  {0:8.4f}".format(best_obj))
    LoadPoint(mymodel, bestpoint)
    printPointFromModel(mymodel)

    plt.show()
    return True
