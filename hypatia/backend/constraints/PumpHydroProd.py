from hypatia.backend.constraints.Constraint import Constraint
from hypatia.utility.constants import (
    ModelMode,
    TopologyType
)
from hypatia.utility.utility import get_regions_with_storage

import pandas as pd
import cvxpy as cp
import numpy as np

"""
Fix the production from Pumped hydro pp to zero when the Pumped hydro storage is absorbing electricity 
"""
class PumpHydroProd(Constraint):
    def _check(self):
        assert hasattr(self.variables, 'totalcapacity'), "totalcapacity must be defined"
        assert self.variables.technology_use != None, "technology_use must not be None"
        assert self.variables.technology_prod != None, "technology_prod must not be None"
        
    def rules(self):
        timeslice_fraction = self.model_data.settings.timeslice_fraction
        if not isinstance(timeslice_fraction, int):
            timeslice_fraction.shape = (len(self.model_data.settings.time_steps), 1)

        rules = []
        for reg in get_regions_with_storage(self.model_data.settings):

            if 'Pump_hydro_Storage' in self.model_data.settings.technologies[reg]['Storage']:
                
                for indx, year in enumerate(self.model_data.settings.years):
            
                    if self.variables.technology_use[reg]["Storage"]['Pump_hydro_ST'][
                            indx * len(self.model_data.settings.time_steps) : (indx + 1)
                            * len(self.model_data.settings.time_steps),:] >= 0:
                    
                        rules.append(                                
                             self.variables.technology_prod[reg]["Supply"]['Pump_hydro_PP'][
                                indx
                                * len(self.model_data.settings.time_steps) : (indx + 1)
                                * len(self.model_data.settings.time_steps),
                                :,
                                ]
                            == 0
                        )
        return rules