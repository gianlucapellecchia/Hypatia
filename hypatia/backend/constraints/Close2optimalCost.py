from hypatia import Utilities_close2opt
from hypatia.backend.constraints.Constraint import Constraint
from hypatia.utility.utility import get_emission_types



import pandas as pd
import cvxpy as cp
import numpy as np

"""
Defines the additional constraint of cost relaxation, when the optimization mode is close2optimal
"""

class Close2optimalCost(Constraint):
    
    def rules(self):
        rules = []       
        rules.append(Utilities_close2opt.optimal_value * (1 + Utilities_close2opt.cost_relaxation) - cp.sum(self.variables.totalcost_allregions_act) >= 0)
        #print(np.shape(self.variables.totalcost_allregions_act))
        #print(self.variables.totalcost_allregions_act)
        #print(np.shape(cp.sum(self.variables.totalcost_allregions_act, axis = 0)))
        print('The optimal value used in the cost costraint is:', Utilities_close2opt.optimal_value)
        print('The cost relaxation used in the cost costraint is:', Utilities_close2opt.cost_relaxation )
        return rules

