from pyomo.environ import *
infinity = float('inf')

model = AbstractModel()

# Factories
model.I = Set()
# Pollutants
model.J = Set()

# ci - Cost to clean water
model.c    = Param(model.I, within=PositiveReals)

# rij - Amount of  Lanthilo and Smilo in the two things
model.r    = Param(model.I, model.J, within=NonNegativeReals)

# Lower and upper bound on processed waste
model.Nmin = Param(model.I, within=NonNegativeReals, default=0.0)

# Sj - Minimum required additives
model.S = Param(model.J)

# Ni - Number of Units of each product
model.N = Var(model.I, within=NonNegativeIntegers)

# Minimize the cost to reduce pollutants
def cost_rule(model):
    return sum(model.c[i]*model.N[i] for i in model.I)
model.cost = Objective(rule=cost_rule)

# Satisfy the state's requeriments on pollutant reduction
def pollutant_rule(model, j):
    return sum(model.r[i,j]*model.N[i] for i in model.I) >= model.S[j]
model.pollutant = Constraint(model.J, rule=pollutant_rule)

# Limit the volume of the decision variables
def waste_rule_min(model, i):
    return model.N[i] >= model.Nmin[i]
model.waste = Constraint(model.I, rule=waste_rule_min)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~ HW4Q3.dat file ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# param:  I:               c :=
#   "F_A"                8.0
#   "F_B"                10.0;

# param:  J:               S :=
#   "P_1"                150.0
#   "P_2"                100.0 ;   

# param r:
#                "P_1"   "P_2" :=
#   "F_A"         8.0     3.0
#   "F_B"         4.0     9.0 ;


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ OUTPUT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ==========================================================
# Solution Summary
# ==========================================================
# No solutions reported by solver.
# [    0.15] Applying Pyomo postprocessing actions
# [    0.15] Pyomo Finished

# (C:\Users\adisi\Anaconda2) C:\Users\adisi\Documents\NCSU\Courses\Fall 2017\Energy Modeling\HomeWork4>pyomo solve --solver=gurobi --summary HW4Q3.py HW4Q3.dat
# [    0.00] Setting up Pyomo environment
# [    0.00] Applying Pyomo preprocessing actions
# [    0.00] Creating model
# [    0.07] Applying solver
# [    0.33] Processing results
#     Number of solutions: 1
#     Solution Information
#       Gap: 0.0
#       Status: optimal
#       Function Value: 188.0
#     Solver results file: results.yml

# ==========================================================
# Solution Summary
# ==========================================================

# Model unknown

#   Variables:
#     N : Size=2, Index=I
#         Key : Lower : Value : Upper : Fixed : Stale : Domain
#         F_A :     0 :  16.0 :  None : False : False : NonNegativeIntegers
#         F_B :     0 :   6.0 :  None : False : False : NonNegativeIntegers

#   Objectives:
#     cost : Size=1, Index=None, Active=True
#         Key  : Active : Value
#         None :   True : 188.0

#   Constraints:
#     pollutant : Size=2
#         Key : Lower : Body  : Upper
#         P_1 : 150.0 : 152.0 :  None
#         P_2 : 100.0 : 102.0 :  None
#     waste : Size=2
#         Key : Lower : Body : Upper
#         F_A :   0.0 : 16.0 :  None
#         F_B :   0.0 :  6.0 :  None

# [    0.44] Applying Pyomo postprocessing actions
# [    0.44] Pyomo Finished
