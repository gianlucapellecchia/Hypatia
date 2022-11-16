#%%
# # -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 10:15:56 2022
@author: Gianluca Pellecchia
"""

from hypatia import Model
import os
from hypatia import italy2020_merge_results


#%% 
# Basecase

# load sets
model = Model(path="sets_Carlo", mode="Planning")

# # create parameteres
# model.create_data_excels(
#     path ='parameters_Carlo1',
#     force_rewrite=True
# )

# read parameters data
model.read_input_data("parameters_Carlo1")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_Carlo", force_rewrite=True, postprocessing_module="it2020")
#%% 
# Low share of H2

# load sets
model = Model(path="sets_planning_v1", mode="Planning")

# # create parameteres
# model.create_data_excels(
#     path ='parameters_planning_prova',
#     force_rewrite=True
# )

# read parameters data
model.read_input_data("parameters_planning_LS")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_LS", force_rewrite=True, postprocessing_module="it2020")

#%% 
# Low share of H2 + Carbon Tax 20 

# load sets
model = Model(path="sets_planning_v1", mode="Planning")

# # create parameteres
# model.create_data_excels(
#     path ='parameters_planning_prova',
#     force_rewrite=True
# )

# read parameters data
model.read_input_data("parameters_planning_LS - CT20")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_LS_CT20", force_rewrite=True, postprocessing_module="it2020")

#%% 
# Low share of H2 + Carbon tax 60

# load sets
model = Model(path="sets_planning_v1", mode="Planning")

# # create parameteres
# model.create_data_excels(
#     path ='parameters_planning_prova',
#     force_rewrite=True
# )

# read parameters data
model.read_input_data("parameters_planning_LS - CT60")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_LS_CT60", force_rewrite=True, postprocessing_module="it2020")

#%% 
# Low share of H2 + Carbon tax 120

# load sets
model = Model(path="sets_planning_v1", mode="Planning")

# # create parameteres
# model.create_data_excels(
#     path ='parameters_planning_prova',
#     force_rewrite=True
# )

# read parameters data
model.read_input_data("parameters_planning_LS - CT120")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_LS_CT120", force_rewrite=True, postprocessing_module="it2020")

#%% 
# Average share of H2

# load sets
model = Model(path="sets_planning_v1", mode="Planning")

# # create parameteres
# model.create_data_excels(
#     path ='parameters_planning_v2',
#     force_rewrite=True
# )

# read parameters data
model.read_input_data("parameters_planning_AS")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_AS", force_rewrite=True, postprocessing_module="it2020")

#%% 
# Average share of H2 + Carbon tax 20

# load sets
model = Model(path="sets_planning_v1", mode="Planning")

# # create parameteres
# model.create_data_excels(
#     path ='parameters_planning_v2',
#     force_rewrite=True
# )

# read parameters data
model.read_input_data("parameters_planning_AS - CT20")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_AS_CT20", force_rewrite=True, postprocessing_module="it2020")

#%% 
# Average share of H2 + Carbon tax 60

# load sets
model = Model(path="sets_planning_v1", mode="Planning")

# # create parameteres
# model.create_data_excels(
#     path ='parameters_planning_v2',
#     force_rewrite=True
# )

# read parameters data
model.read_input_data("parameters_planning_AS - CT60")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_AS_CT60", force_rewrite=True, postprocessing_module="it2020")

#%% 
# Average share of H2 + Carbon tax 120

# load sets
model = Model(path="sets_planning_v1", mode="Planning")

# # create parameteres
# model.create_data_excels(
#     path ='parameters_planning_v2',
#     force_rewrite=True
# )

# read parameters data
model.read_input_data("parameters_planning_AS - CT120")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_AS_CT120", force_rewrite=True, postprocessing_module="it2020")

#%% 
# High share of H2

# load sets
model = Model(path="sets_planning_v1", mode="Planning")

# # create parameteres
# model.create_data_excels(
#     path ='parameters_prova',
#     force_rewrite=True
# )

# read parameters data
model.read_input_data("parameters_planning_HS")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_HS", force_rewrite=True, postprocessing_module="it2020")

#%% 
# High share of H2 + Carbon tax 20

# load sets
model = Model(path="sets_planning_v1", mode="Planning")

# # create parameteres
# model.create_data_excels(
#     path ='parameters_planning_v2',
#     force_rewrite=True
# )

# read parameters data
model.read_input_data("parameters_planning_HS - CT20")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_HS_CT20", force_rewrite=True, postprocessing_module="it2020")

#%% 
# High share of H2 + Carbon tax 60

# load sets
model = Model(path="sets_planning_v1", mode="Planning")

# # create parameteres
# model.create_data_excels(
#     path ='parameters_planning_v2',
#     force_rewrite=True
# )

# read parameters data
model.read_input_data("parameters_planning_HS - CT60")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_HS_CT60", force_rewrite=True, postprocessing_module="it2020")

#%% 
# High share of H2 + Carbon tax 120

# load sets
model = Model(path="sets_planning_v1", mode="Planning")

# # create parameteres
# model.create_data_excels(
#     path ='parameters_planning_v2',
#     force_rewrite=True
# )

# read parameters data
model.read_input_data("parameters_planning_HS - CT120")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_HS_CT120", force_rewrite=True, postprocessing_module="it2020")

#%%
# Merge result csv for different scenarios
italy2020_merge_results(
    scenarios={
        # "scenario1": "results_planning" + "/result_scenario_LS_old/",
        # "scenario2": "results_planning" + "/result_scenario_LS_new/",
        "scenario1": "results_planning" + "/result_scenario_BC/",
        "scenario2": "results_planning" + "/result_scenario_LS/",
        "scenario3": "results_planning" + "/result_scenario_LS_CT20/",
        "scenario4": "results_planning" + "/result_scenario_LS_CT60/",
        "scenario5": "results_planning" + "/result_scenario_LS_CT120/",
        "scenario6": "results_planning" + "/result_scenario_AS/",
        "scenario7": "results_planning" + "/result_scenario_AS_CT20/",
        "scenario8": "results_planning" + "/result_scenario_AS_CT60/",
        "scenario9": "results_planning" + "/result_scenario_AS_CT120/",
        "scenario10": "results_planning" + "/result_scenario_HS/",
        "scenario11": "results_planning" + "/result_scenario_HS_CT20/",
        "scenario12": "results_planning" + "/result_scenario_HS_CT60/",
        "scenario13": "results_planning" + "/result_scenario_HS_CT120/",
    },
    path="results_planning" + "/merged_results_planning",
    force_rewrite=True
)

#%%
# AGGREGATION FILE
# generate aggregation for the 2 models.
# Since the 2 models sets are the same the generated file from the 2 models will be the same. Therefore I generate only 1 aggregation file
# which can be shared between the 2 models
# model.create_aggregation_config_file(path="results_planning" + "/aggregation_config_planning.xlsx")