# -*- coding: utf-8 -*-

import import_ipynb

from optimization_functions import *

from display_circle import init_circles

from my_model import CirclePacking

from pyomo.core.base.block import generate_cuid_names

n = 2 #number of circles

mymodel = CirclePacking(n)

Multi_n_iter = n*100

localsolver = create_solver('minos')

gen_multi = init_circles(n) # c'est l'idée mais le format renvoyé ne convient pas

#random_point dans multistart qu'on remplacera directement sans passer par gen_multi ?

labels = generate_cuid_names(mymodel)

logfile = open("myLog.txt", 'w')

tech_time = time.process_time()
FoundSolution = multistart(mymodel, Multi_n_iter, gen_multi, localsolver, labels, logfile)
multistart_time = time.process_time()

print("\n--------------\nLoading... ", tech_time)
print("Multistart ", multistart_time - tech_time)