from hypatia.backend.constraints.Constraint import Constraint
from hypatia.utility.constants import (
    ModelMode,
    TopologyType
)
from hypatia.utility.utility import annual_activity
from hypatia.utility.utility import create_technology_columns
from hypatia.utility.utility import stack
import pandas as pd
import cvxpy as cp
import numpy as np

"""
Defines the upper and lower limit for the annual production of the technologies
within each region
"""
class TechnologyUseShareRegional(Constraint):
    def _check(self):
        assert self.variables.technology_use != None, "technology_prod cannot be None"                    
    
    def rules(self):
        rules = []
                    
        # for reg in self.model_data.settings.regions:
            
        #     for key in self.model_data.settings.technologies[reg].keys():
                
        #         if key != "Conversion_plus":
        #             continue
        #         total_carrier_ratio_in_share = {}
        #         for indx, tech in enumerate(self.model_data.settings.technologies[reg][key]):
                    
        #             total_carrier_ratio_in_share_tech = np.zeros(len(self.model_data.settings.years) * len(self.model_data.settings.time_steps),)
        #             # print(tech)
                    
                    
        #             for carr in self.model_data.settings.regional_settings[reg]["Carrier_input"].loc[self.model_data.settings.regional_settings[reg]["Carrier_input"]["Technology"]== tech]["Carrier_in"].values:
        #                 # print(carr)
        #                 total_carrier_ratio_in_share_tech += self.variables.carrier_ratio_in[reg][key][tech][carr]
                        
        #                 rules.append(
        #                     self.variables.carrier_ratio_in[reg][key][tech][carr] 
        #                     - self.model_data.regional_parameters[reg]["min_carrier_ratio_in"][
        #                         (tech, carr)
        #                     ].values >= 0
        #                     )
                        
        #             total_carrier_ratio_in_share[tech] = total_carrier_ratio_in_share_tech    
        #             # print(total_carrier_ratio_in_share[tech])
                        
        #             rules.append(
        #                 total_carrier_ratio_in_share[tech] 
        #                 - np.ones(len(self.model_data.settings.years) * len(self.model_data.settings.time_steps),) == 0 
        #                 )

        return rules

    
    
    
