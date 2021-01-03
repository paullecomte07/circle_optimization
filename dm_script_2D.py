# -*- coding: utf-8 -*-

""" Ce script cherche à maximiser le rayon de n cercles enfermés dans un carré unitaire"""

import import_ipynb
from optimization_functions import *

from display_circle import init_circles, display_circles, init_circles_random
from my_model import CirclePacking


from pyomo.core.base.block import generate_cuid_names
import time

# Nombre de cercles contenus dans le carré
n = 5

# Modélisation du problème avec pyomo
mymodel = CirclePacking(n)

# Nombre max d'itérations
max_iter = n*10

# Appel d'un local solver
localsolver = create_solver('knitro')

# On génère un premier ensemble de centres et un rayon pour commencer l'optimisation
#init_values = init_circles(n)
init_values = init_circles_random(n)

labels = generate_cuid_names(mymodel)

# Création d'un fichier qui contiendra les logs
logfile = open("myLog.txt", 'w')
"""
# Execution de la méthode d'optimisation MBH avec mesure du temps d'execution
tech_time = time.process_time()
FoundSolution = monotonic_basin_hopping(mymodel, max_iter, init_values , localsolver, labels, logfile)
mbh_time = time.process_time()

print("\n--------------\nLoading... ", tech_time, "s")
print("MBH ", mbh_time - tech_time, "s")
"""


init_values = init_circles_random(n)

# Execution de la méthode d'optimisation Multistart avec mesure du temps d'execution
tech_time = time.process_time()
FoundSolution = multistart(mymodel, max_iter, init_values , localsolver, labels, logfile)
mbh_time = time.process_time()

print("\n--------------\nLoading... ", tech_time, "s")
print("MBH ", mbh_time - tech_time, "s")
