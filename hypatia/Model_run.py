#%%
# # -*- coding: utf-8 -*-
"""
KENYA MODEL
@author: Gianluca Pellecchia
"""

from hypatia import Model
import os
from hypatia import italy2020_merge_results

#%% 
# Operation parameters creation

# load sets
model = Model(path="sets_operation", mode="Operation")

# # create parameteres
# model.create_data_excels(
#     path ='parameters_operation',
#     force_rewrite=True
# )

#%% 
# Operation

# read parameters data
model.read_input_data("parameters_operation")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results" + r"\result_operation", force_rewrite=True, postprocessing_module="it2020")

#%% 
# Planning parameters creation

# load sets
model = Model(path="sets_planning", mode="Planning")

# # create parameteres
# model.create_data_excels(
#     path ='parameters_planning_new',
#     force_rewrite=True
# )

#%% 
# Planning

# read parameters data
model.read_input_data("parameters_planning")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results" + r"\result_planning", force_rewrite=True, postprocessing_module="it2020")
# model.to_csv(path="results_Kenya"+ r"\result_planning, force_rewrite=True, postprocessing_module="it2020")

#%% 
# Planning parameters creation 1h

# load sets
model = Model(path="sets_planning_1h", mode="Planning")

# # create parameteres
# model.create_data_excels(
#     path ='parameters_planning',
#     force_rewrite=True
# )

#%% 
# Planning

# read parameters data
model.read_input_data("parameters_planning_1h")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results" + r"\result_planning_1h", force_rewrite=True, postprocessing_module="it2020")
# model.to_csv(path="results_Kenya"+ r"\result_planning, force_rewrite=True, postprocessing_module="it2020")
#%%
# Merge result csv for different scenarios
italy2020_merge_results(
    scenarios={
        "operation": "results" + "/result_operation/",
        "planning": "results" + "/result_planning/",
        "planning_1h": "results" + "/result_planning_1h/",
    },
    path="results_Kenya" + "/merged_results",
    force_rewrite=True
)