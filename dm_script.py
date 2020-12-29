# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 16:48:56 2020

@author: caro9
"""

import import_ipynb

from optimization_functions import *

from display_circle import init_circles

from my_model import CirclePacking

from pyomo.core.base.block import generate_cuid_names

n = 2

mymodel = CirclePacking(n)

Multi_n_iter = n*100

localsolver = create_solver('minos')

gen_multi = init_circles(n) # c'est l'idée mais le format renvoyé ne convient pas

#random_point dans multistart qu'on remplacera directement sans passer par gen_multi ?