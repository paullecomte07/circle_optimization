# -*- coding: utf-8 -*-

"""Modélisation du problème avec pyomo
   Définition de la fonction à maximiser et des contraintes"""

import pyomo.environ as pe


def CirclePacking2D(size):
    
    model = pe.AbstractModel()
    model.n = pe.Param(within=pe.NonNegativeIntegers)
    
    model.I = pe.RangeSet(1,model.n)
    model.J = pe.RangeSet(1,model.n)
    
    model.x = pe.Var(model.I, bounds=(0,1))
    model.y = pe.Var(model.I, bounds=(0,1))
    model.r = pe.Var(domain=pe.NonNegativeReals, bounds=(0,1))
    
    # on a vu des méthodes permettant de déterminer le minimum
    # mais on cherche max r ce qui revient à chercher min -r
    model.obj = pe.Objective(expr = - model.r ) 
        
    def xyrconstraint_rule(m,i,j):
        # return the expression for the constraint for i and j if i != j
        if i!=j :
            return ((m.x[i] - m.x[j])**2 + (m.y[i] - m.y[j])**2) >= (2*m.r)**2
        else :
            return pe.Constraint.Skip
    
    model.xyrconstraint = pe.Constraint(model.I, model.J, rule = xyrconstraint_rule) 
    
    def xrconstraint_rule1(m,i):
        return m.r <= m.x[i]
        
    model.xrconstraint1 = pe.Constraint(model.I, rule = xrconstraint_rule1 )
    
    def xrconstraint_rule2(m,i):
        return m.x[i] <= 1-m.r
        
    model.xrconstraint2 = pe.Constraint(model.I, rule = xrconstraint_rule2 )
    
    
    def yrconstraint_rule1(m,i):
        return m.r <= m.y[i]
    
    model.yrconstraint1 = pe.Constraint(model.I, rule = yrconstraint_rule1)
    
    def yrconstraint_rule2(m,i):
        return m.y[i] <= 1-m.r
    
    model.yrconstraint2 = pe.Constraint(model.I, rule = yrconstraint_rule2)
    
    model.n = size
    
    return model.create_instance()

def CirclePacking3D(size):
    
    model = pe.AbstractModel()
    model.n = pe.Param(within=pe.NonNegativeIntegers)
    
    model.I = pe.RangeSet(1,model.n)
    model.J = pe.RangeSet(1,model.n)
    
    model.x = pe.Var(model.I, bounds=(0,1))
    model.y = pe.Var(model.I, bounds=(0,1))
    model.z = pe.Var(model.I, bounds=(0,1))
    model.r = pe.Var(domain=pe.NonNegativeReals, bounds=(0,1))
    
    # on a vu des méthodes permettant de déterminer le minimum
    # mais on cherche max r ce qui revient à chercher min -r
    model.obj = pe.Objective(expr = - model.r ) 
        
    def xyzrconstraint_rule(m,i,j):
        # return the expression for the constraint for i and j if i != j
        if i!=j :
            return ((m.x[i] - m.x[j])**2 + (m.y[i] - m.y[j])**2 + (m.z[i] - m.z[j])**2) >= (2*m.r)**2
        else :
            return pe.Constraint.Skip
    
    model.xyrconstraint = pe.Constraint(model.I, model.J, rule = xyzrconstraint_rule) 
    
    def xrconstraint_rule1(m,i):
        return m.r <= m.x[i]
        
    model.xrconstraint1 = pe.Constraint(model.I, rule = xrconstraint_rule1 )
    
    def xrconstraint_rule2(m,i):
        return m.x[i] <= 1-m.r
        
    model.xrconstraint2 = pe.Constraint(model.I, rule = xrconstraint_rule2 )
    
    
    def yrconstraint_rule1(m,i):
        return m.r <= m.y[i]
    
    model.yrconstraint1 = pe.Constraint(model.I, rule = yrconstraint_rule1)
    
    def yrconstraint_rule2(m,i):
        return m.y[i] <= 1-m.r
    
    model.yrconstraint2 = pe.Constraint(model.I, rule = yrconstraint_rule2)
    
    def zrconstraint_rule1(m,i):
        return m.r <= m.z[i]
    
    model.zrconstraint1 = pe.Constraint(model.I, rule = zrconstraint_rule1)
    
    def zrconstraint_rule2(m,i):
        return m.z[i] <= 1-m.r
    
    model.zrconstraint2 = pe.Constraint(model.I, rule = zrconstraint_rule2)
    
    model.n = size
    
    return model.create_instance()