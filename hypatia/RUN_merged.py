#%%
# # -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 10:15:56 2022
@author: Gianluca Pellecchia
"""

from hypatia import Model
import os
from hypatia import italy2020_merge_results

 # %% 
# # Paramters creation

# # load sets
# model = Model(path="sets_planning_v1", mode="Planning")

# # create parameteres
# model.create_data_excels(
#     path ='parameters_planning_new',
#     force_rewrite=True
# )

# #%% 
# # Basecase

# # load sets
# model = Model(path="sets_planning_v1", mode="Planning")

# # # create parameteres
# # model.create_data_excels(
# #     path ='parameters_Carlo1',
# #     force_rewrite=True
# # )

# # read parameters data
# model.read_input_data("parameters_planning_BC")

# # solve model
# model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# # create a new results folder (only if you haven't done so already)
# # os.mkdir(base_path + "/results/")

# # write result to csv in the it2020 format
# model.to_csv(path="results_planning" + r"\result_scenario_BC", force_rewrite=True, postprocessing_module="it2020")

# #%% 
# # Low share of H2

# # load sets
# model = Model(path="sets_planning_v1", mode="Planning")

# # # create parameteres
# # model.create_data_excels(
# #     path ='parameters_planning_prova',
# #     force_rewrite=True
# # )

# # read parameters data
# model.read_input_data("parameters_planning_LS")

# # solve model
# model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# # create a new results folder (only if you haven't done so already)
# # os.mkdir(base_path + "/results/")

# # write result to csv in the it2020 format
# model.to_csv(path="results_planning" + r"\result_scenario_LS", force_rewrite=True, postprocessing_module="it2020")

# #%% 
# # Low share of H2 + Carbon Tax 20 

# # load sets
# model = Model(path="sets_planning_v1", mode="Planning")

# # # create parameteres
# # model.create_data_excels(
# #     path ='parameters_planning_prova',
# #     force_rewrite=True
# # )

# # read parameters data
# model.read_input_data("parameters_planning_LS - CT20")

# # solve model
# model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# # create a new results folder (only if you haven't done so already)
# # os.mkdir(base_path + "/results/")

# # write result to csv in the it2020 format
# model.to_csv(path="results_planning" + r"\result_scenario_LS_CT20", force_rewrite=True, postprocessing_module="it2020")

# #%% 
# # Low share of H2 + Carbon tax 60

# # load sets
# model = Model(path="sets_planning_v1", mode="Planning")

# # # create parameteres
# # model.create_data_excels(
# #     path ='parameters_planning_prova',
# #     force_rewrite=True
# # )

# # read parameters data
# model.read_input_data("parameters_planning_LS - CT60")

# # solve model
# model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# # create a new results folder (only if you haven't done so already)
# # os.mkdir(base_path + "/results/")

# # write result to csv in the it2020 format
# model.to_csv(path="results_planning" + r"\result_scenario_LS_CT60", force_rewrite=True, postprocessing_module="it2020")

# #%% 
# # Low share of H2 + Carbon tax 120

# # load sets
# model = Model(path="sets_planning_v1", mode="Planning")

# # # create parameteres
# # model.create_data_excels(
# #     path ='parameters_planning_prova',
# #     force_rewrite=True
# # )

# # read parameters data
# model.read_input_data("parameters_planning_LS - CT120")

# # solve model
# model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# # create a new results folder (only if you haven't done so already)
# # os.mkdir(base_path + "/results/")

# # write result to csv in the it2020 format
# model.to_csv(path="results_planning" + r"\result_scenario_LS_CT120", force_rewrite=True, postprocessing_module="it2020")

# #%% 
# # Low share of H2

# # load sets
# model = Model(path="sets_planning_v1", mode="Planning")

# # # create parameteres
# # model.create_data_excels(
# #     path ='parameters_planning_prova',
# #     force_rewrite=True
# # )

# # read parameters data
# model.read_input_data("parameters_planning_LS - LR19")

# # solve model
# model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# # create a new results folder (only if you haven't done so already)
# # os.mkdir(base_path + "/results/")

# # write result to csv in the it2020 format
# model.to_csv(path="results_planning" + r"\result_scenario_LS_LR19", force_rewrite=True, postprocessing_module="it2020")

# #%% 
# # Low share of H2 + Carbon Tax 20 

# # load sets
# model = Model(path="sets_planning_v1", mode="Planning")

# # # create parameteres
# # model.create_data_excels(
# #     path ='parameters_planning_prova',
# #     force_rewrite=True
# # )

# # read parameters data
# model.read_input_data("parameters_planning_LS - LR19 - CT20")

# # solve model
# model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# # create a new results folder (only if you haven't done so already)
# # os.mkdir(base_path + "/results/")

# # write result to csv in the it2020 format
# model.to_csv(path="results_planning" + r"\result_scenario_LS_LR19_CT20", force_rewrite=True, postprocessing_module="it2020")

# #%% 
# # Low share of H2 + Carbon tax 60

# # load sets
# model = Model(path="sets_planning_v1", mode="Planning")

# # # create parameteres
# # model.create_data_excels(
# #     path ='parameters_planning_prova',
# #     force_rewrite=True
# # )

# # read parameters data
# model.read_input_data("parameters_planning_LS - LR19 - CT60")

# # solve model
# model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# # create a new results folder (only if you haven't done so already)
# # os.mkdir(base_path + "/results/")

# # write result to csv in the it2020 format
# model.to_csv(path="results_planning" + r"\result_scenario_LS_LR19_CT60", force_rewrite=True, postprocessing_module="it2020")

# #%% 
# # Low share of H2 + Carbon tax 120

# # load sets
# model = Model(path="sets_planning_v1", mode="Planning")

# # # create parameteres
# # model.create_data_excels(
# #     path ='parameters_planning_prova',
# #     force_rewrite=True
# # )

# # read parameters data
# model.read_input_data("parameters_planning_LS - LR19 - CT120")

# # solve model
# model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# # create a new results folder (only if you haven't done so already)
# # os.mkdir(base_path + "/results/")

# # write result to csv in the it2020 format
# model.to_csv(path="results_planning" + r"\result_scenario_LS_LR19_CT120", force_rewrite=True, postprocessing_module="it2020")

# #%% 
# # Low share of H2

# # load sets
# model = Model(path="sets_planning_v1", mode="Planning")

# # # create parameteres
# # model.create_data_excels(
# #     path ='parameters_planning_prova',
# #     force_rewrite=True
# # )

# # read parameters data
# model.read_input_data("parameters_planning_LS - LR22")

# # solve model
# model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# # create a new results folder (only if you haven't done so already)
# # os.mkdir(base_path + "/results/")

# # write result to csv in the it2020 format
# model.to_csv(path="results_planning" + r"\result_scenario_LS_LR22", force_rewrite=True, postprocessing_module="it2020")

# #%% 
# # Low share of H2 + Carbon Tax 20 

# # load sets
# model = Model(path="sets_planning_v1", mode="Planning")

# # # create parameteres
# # model.create_data_excels(
# #     path ='parameters_planning_prova',
# #     force_rewrite=True
# # )

# # read parameters data
# model.read_input_data("parameters_planning_LS - LR22 - CT20")

# # solve model
# model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# # create a new results folder (only if you haven't done so already)
# # os.mkdir(base_path + "/results/")

# # write result to csv in the it2020 format
# model.to_csv(path="results_planning" + r"\result_scenario_LS_LR22_CT20", force_rewrite=True, postprocessing_module="it2020")

# #%% 
# # Low share of H2 + Carbon tax 60

# # load sets
# model = Model(path="sets_planning_v1", mode="Planning")

# # # create parameteres
# # model.create_data_excels(
# #     path ='parameters_planning_prova',
# #     force_rewrite=True
# # )

# # read parameters data
# model.read_input_data("parameters_planning_LS - LR22 - CT60")

# # solve model
# model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# # create a new results folder (only if you haven't done so already)
# # os.mkdir(base_path + "/results/")

# # write result to csv in the it2020 format
# model.to_csv(path="results_planning" + r"\result_scenario_LS_LR22_CT60", force_rewrite=True, postprocessing_module="it2020")

# #%% 
# # Low share of H2 + Carbon tax 120

# # load sets
# model = Model(path="sets_planning_v1", mode="Planning")

# # # create parameteres
# # model.create_data_excels(
# #     path ='parameters_planning_prova',
# #     force_rewrite=True
# # )

# # read parameters data
# model.read_input_data("parameters_planning_LS - LR22 - CT120")

# # solve model
# model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# # create a new results folder (only if you haven't done so already)
# # os.mkdir(base_path + "/results/")

# # write result to csv in the it2020 format
# model.to_csv(path="results_planning" + r"\result_scenario_LS_LR22_CT120", force_rewrite=True, postprocessing_module="it2020")

# #%% 
# # Low share of H2

# # load sets
# model = Model(path="sets_planning_v1", mode="Planning")

# # # create parameteres
# # model.create_data_excels(
# #     path ='parameters_planning_prova',
# #     force_rewrite=True
# # )

# # read parameters data
# model.read_input_data("parameters_planning_LS - LR25")

# # solve model
# model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# # create a new results folder (only if you haven't done so already)
# # os.mkdir(base_path + "/results/")

# # write result to csv in the it2020 format
# model.to_csv(path="results_planning" + r"\result_scenario_LS_LR25", force_rewrite=True, postprocessing_module="it2020")

# #%% 
# # Low share of H2 + Carbon Tax 20 

# # load sets
# model = Model(path="sets_planning_v1", mode="Planning")

# # # create parameteres
# # model.create_data_excels(
# #     path ='parameters_planning_prova',
# #     force_rewrite=True
# # )

# # read parameters data
# model.read_input_data("parameters_planning_LS - LR25 - CT20")

# # solve model
# model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# # create a new results folder (only if you haven't done so already)
# # os.mkdir(base_path + "/results/")

# # write result to csv in the it2020 format
# model.to_csv(path="results_planning" + r"\result_scenario_LS_LR25_CT20", force_rewrite=True, postprocessing_module="it2020")

# #%% 
# # Low share of H2 + Carbon tax 60

# # load sets
# model = Model(path="sets_planning_v1", mode="Planning")

# # # create parameteres
# # model.create_data_excels(
# #     path ='parameters_planning_prova',
# #     force_rewrite=True
# # )

# # read parameters data
# model.read_input_data("parameters_planning_LS - LR25 - CT60")

# # solve model
# model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# # create a new results folder (only if you haven't done so already)
# # os.mkdir(base_path + "/results/")

# # write result to csv in the it2020 format
# model.to_csv(path="results_planning" + r"\result_scenario_LS_LR25_CT60", force_rewrite=True, postprocessing_module="it2020")

# #%% 
# # Low share of H2 + Carbon tax 120

# # load sets
# model = Model(path="sets_planning_v1", mode="Planning")

# # # create parameteres
# # model.create_data_excels(
# #     path ='parameters_planning_prova',
# #     force_rewrite=True
# # )

# # read parameters data
# model.read_input_data("parameters_planning_LS - LR25 - CT120")

# # solve model
# model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# # create a new results folder (only if you haven't done so already)
# # os.mkdir(base_path + "/results/")

# # write result to csv in the it2020 format
# model.to_csv(path="results_planning" + r"\result_scenario_LS_LR25_CT120", force_rewrite=True, postprocessing_module="it2020")

# #%% 
# # Low share of H2

# # load sets
# model = Model(path="sets_planning_v1", mode="Planning")

# # # create parameteres
# # model.create_data_excels(
# #     path ='parameters_planning_prova',
# #     force_rewrite=True
# # )

# # read parameters data
# model.read_input_data("parameters_planning_LS - LR28")

# # solve model
# model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# # create a new results folder (only if you haven't done so already)
# # os.mkdir(base_path + "/results/")

# # write result to csv in the it2020 format
# model.to_csv(path="results_planning" + r"\result_scenario_LS_LR28", force_rewrite=True, postprocessing_module="it2020")

# #%% 
# # Low share of H2 + Carbon Tax 20 

# # load sets
# model = Model(path="sets_planning_v1", mode="Planning")

# # # create parameteres
# # model.create_data_excels(
# #     path ='parameters_planning_prova',
# #     force_rewrite=True
# # )

# # read parameters data
# model.read_input_data("parameters_planning_LS - LR28 - CT20")

# # solve model
# model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# # create a new results folder (only if you haven't done so already)
# # os.mkdir(base_path + "/results/")

# # write result to csv in the it2020 format
# model.to_csv(path="results_planning" + r"\result_scenario_LS_LR28_CT20", force_rewrite=True, postprocessing_module="it2020")

# #%% 
# # Low share of H2 + Carbon tax 60

# # load sets
# model = Model(path="sets_planning_v1", mode="Planning")

# # # create parameteres
# # model.create_data_excels(
# #     path ='parameters_planning_prova',
# #     force_rewrite=True
# # )

# # read parameters data
# model.read_input_data("parameters_planning_LS - LR28 - CT60")

# # solve model
# model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# # create a new results folder (only if you haven't done so already)
# # os.mkdir(base_path + "/results/")

# # write result to csv in the it2020 format
# model.to_csv(path="results_planning" + r"\result_scenario_LS_LR28_CT60", force_rewrite=True, postprocessing_module="it2020")

# #%% 
# # Low share of H2 + Carbon tax 120

# # load sets
# model = Model(path="sets_planning_v1", mode="Planning")

# # # create parameteres
# # model.create_data_excels(
# #     path ='parameters_planning_prova',
# #     force_rewrite=True
# # )

# # read parameters data
# model.read_input_data("parameters_planning_LS - LR28 - CT120")

# # solve model
# model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# # create a new results folder (only if you haven't done so already)
# # os.mkdir(base_path + "/results/")

# # write result to csv in the it2020 format
# model.to_csv(path="results_planning" + r"\result_scenario_LS_LR28_CT120", force_rewrite=True, postprocessing_module="it2020")

# #%% 
# # Low share of H2

# # load sets
# model = Model(path="sets_planning_v1", mode="Planning")

# # # create parameteres
# # model.create_data_excels(
# #     path ='parameters_planning_prova',
# #     force_rewrite=True
# # )

# # read parameters data
# model.read_input_data("parameters_planning_LS - LR31")

# # solve model
# model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# # create a new results folder (only if you haven't done so already)
# # os.mkdir(base_path + "/results/")

# # write result to csv in the it2020 format
# model.to_csv(path="results_planning" + r"\result_scenario_LS_LR31", force_rewrite=True, postprocessing_module="it2020")

# #%% 
# # Low share of H2 + Carbon Tax 20 

# # load sets
# model = Model(path="sets_planning_v1", mode="Planning")

# # # create parameteres
# # model.create_data_excels(
# #     path ='parameters_planning_prova',
# #     force_rewrite=True
# # )

# # read parameters data
# model.read_input_data("parameters_planning_LS - LR31 - CT20")

# # solve model
# model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# # create a new results folder (only if you haven't done so already)
# # os.mkdir(base_path + "/results/")

# # write result to csv in the it2020 format
# model.to_csv(path="results_planning" + r"\result_scenario_LS_LR31_CT20", force_rewrite=True, postprocessing_module="it2020")

# #%% 
# # Low share of H2 + Carbon tax 60

# # load sets
# model = Model(path="sets_planning_v1", mode="Planning")

# # # create parameteres
# # model.create_data_excels(
# #     path ='parameters_planning_prova',
# #     force_rewrite=True
# # )

# # read parameters data
# model.read_input_data("parameters_planning_LS - LR31 - CT60")

# # solve model
# model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# # create a new results folder (only if you haven't done so already)
# # os.mkdir(base_path + "/results/")

# # write result to csv in the it2020 format
# model.to_csv(path="results_planning" + r"\result_scenario_LS_LR31_CT60", force_rewrite=True, postprocessing_module="it2020")

# #%% 
# # Low share of H2 + Carbon tax 120

# # load sets
# model = Model(path="sets_planning_v1", mode="Planning")

# # # create parameteres
# # model.create_data_excels(
# #     path ='parameters_planning_prova',
# #     force_rewrite=True
# # )

# # read parameters data
# model.read_input_data("parameters_planning_LS - LR31 - CT120")

# # solve model
# model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# # create a new results folder (only if you haven't done so already)
# # os.mkdir(base_path + "/results/")

# # write result to csv in the it2020 format
# model.to_csv(path="results_planning" + r"\result_scenario_LS_LR31_CT120", force_rewrite=True, postprocessing_module="it2020")

# #%% 
# # Low share of H2

# # load sets
# model = Model(path="sets_planning_v1", mode="Planning")

# # # create parameteres
# # model.create_data_excels(
# #     path ='parameters_planning_prova',
# #     force_rewrite=True
# # )

# # read parameters data
# model.read_input_data("parameters_planning_LS - LR34")

# # solve model
# model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# # create a new results folder (only if you haven't done so already)
# # os.mkdir(base_path + "/results/")

# # write result to csv in the it2020 format
# model.to_csv(path="results_planning" + r"\result_scenario_LS_LR34", force_rewrite=True, postprocessing_module="it2020")

# #%% 
# # Low share of H2 + Carbon Tax 20 

# # load sets
# model = Model(path="sets_planning_v1", mode="Planning")

# # # create parameteres
# # model.create_data_excels(
# #     path ='parameters_planning_prova',
# #     force_rewrite=True
# # )

# # read parameters data
# model.read_input_data("parameters_planning_LS - LR34 - CT20")

# # solve model
# model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# # create a new results folder (only if you haven't done so already)
# # os.mkdir(base_path + "/results/")

# # write result to csv in the it2020 format
# model.to_csv(path="results_planning" + r"\result_scenario_LS_LR34_CT20", force_rewrite=True, postprocessing_module="it2020")

# #%% 
# # Low share of H2 + Carbon tax 60

# # load sets
# model = Model(path="sets_planning_v1", mode="Planning")

# # # create parameteres
# # model.create_data_excels(
# #     path ='parameters_planning_prova',
# #     force_rewrite=True
# # )

# # read parameters data
# model.read_input_data("parameters_planning_LS - LR34 - CT60")

# # solve model
# model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# # create a new results folder (only if you haven't done so already)
# # os.mkdir(base_path + "/results/")

# # write result to csv in the it2020 format
# model.to_csv(path="results_planning" + r"\result_scenario_LS_LR34_CT60", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_LS - LR34 - CT120")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_LS_LR34_CT120", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_LS - LR37")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_LS_LR37", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_LS - LR37 - CT20")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_LS_LR37_CT20", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_LS - LR37 - CT60")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_LS_LR37_CT60", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_LS - LR37 - CT120")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_LS_LR37_CT120", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_LS - LR40")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_LS_LR40", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_LS - LR40 - CT20")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_LS_LR40_CT20", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_LS - LR40 - CT60")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_LS_LR40_CT60", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_LS - LR40 - CT120")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_LS_LR40_CT120", force_rewrite=True, postprocessing_module="it2020")

#%% 
# # Average share of H2

# # load sets
# model = Model(path="sets_planning_v1", mode="Planning")

# # # create parameteres
# # model.create_data_excels(
# #     path ='parameters_planning_v2',
# #     force_rewrite=True
# # )

# # read parameters data
# model.read_input_data("parameters_planning_AS")

# # solve model
# model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# # create a new results folder (only if you haven't done so already)
# # os.mkdir(base_path + "/results/")

# # write result to csv in the it2020 format
# model.to_csv(path="results_planning" + r"\result_scenario_AS", force_rewrite=True, postprocessing_module="it2020")

# #%% 
# # Average share of H2 + Carbon tax 20

# # load sets
# model = Model(path="sets_planning_v1", mode="Planning")

# # # create parameteres
# # model.create_data_excels(
# #     path ='parameters_planning_v2',
# #     force_rewrite=True
# # )

# # read parameters data
# model.read_input_data("parameters_planning_AS - CT20")

# # solve model
# model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# # create a new results folder (only if you haven't done so already)
# # os.mkdir(base_path + "/results/")

# # write result to csv in the it2020 format
# model.to_csv(path="results_planning" + r"\result_scenario_AS_CT20", force_rewrite=True, postprocessing_module="it2020")

# #%% 
# # Average share of H2 + Carbon tax 60

# # load sets
# model = Model(path="sets_planning_v1", mode="Planning")

# # # create parameteres
# # model.create_data_excels(
# #     path ='parameters_planning_v2',
# #     force_rewrite=True
# # )

# # read parameters data
# model.read_input_data("parameters_planning_AS - CT60")

# # solve model
# model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# # create a new results folder (only if you haven't done so already)
# # os.mkdir(base_path + "/results/")

# # write result to csv in the it2020 format
# model.to_csv(path="results_planning" + r"\result_scenario_AS_CT60", force_rewrite=True, postprocessing_module="it2020")

# #%% 
# # Average share of H2 + Carbon tax 120

# # load sets
# model = Model(path="sets_planning_v1", mode="Planning")

# # # create parameteres
# # model.create_data_excels(
# #     path ='parameters_planning_v2',
# #     force_rewrite=True
# # )

# # read parameters data
# model.read_input_data("parameters_planning_AS - CT120")

# # solve model
# model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# # create a new results folder (only if you haven't done so already)
# # os.mkdir(base_path + "/results/")

# # write result to csv in the it2020 format
# model.to_csv(path="results_planning" + r"\result_scenario_AS_CT120", force_rewrite=True, postprocessing_module="it2020")

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
# High share of H2

# load sets
model = Model(path="sets_planning_v1", mode="Planning")

# # create parameteres
# model.create_data_excels(
#     path ='parameters_prova',
#     force_rewrite=True
# )

# read parameters data
model.read_input_data("parameters_planning_HS - LR19")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_HS_LR19", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_HS - LR19 - CT20")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_HS_LR19_CT20", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_HS - LR19 - CT60")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_HS_LR19_CT60", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_HS - LR19 - CT120")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_HS_LR19_CT120", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_HS - LR22")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_HS_LR22", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_HS - LR22 - CT20")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_HS_LR22_CT20", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_HS - LR22 - CT60")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_HS_LR22_CT60", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_HS - LR22 - CT120")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_HS_LR22_CT120", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_HS - LR25")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_HS_LR25", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_HS - LR25 - CT20")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_HS_LR25_CT20", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_HS - LR25 - CT60")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_HS_LR25_CT60", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_HS - LR25 - CT120")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_HS_LR25_CT120", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_HS - LR28")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_HS_LR28", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_HS - LR28 - CT20")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_HS_LR28_CT20", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_HS - LR28 - CT60")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_HS_LR28_CT60", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_HS - LR28 - CT120")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_HS_LR28_CT120", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_HS - LR31")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_HS_LR31", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_HS - LR31 - CT20")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_HS_LR31_CT20", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_HS - LR31 - CT60")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_HS_LR31_CT60", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_HS - LR31 - CT120")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_HS_LR31_CT120", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_HS - LR34")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_HS_LR34", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_HS - LR34 - CT20")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_HS_LR34_CT20", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_HS - LR34 - CT60")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_HS_LR34_CT60", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_HS - LR34 - CT120")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_HS_LR34_CT120", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_HS - LR37")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_HS_LR37", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_HS - LR37 - CT20")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_HS_LR37_CT20", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_HS - LR37 - CT60")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_HS_LR37_CT60", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_HS - LR37 - CT120")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_HS_LR37_CT120", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_HS - LR40")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_HS_LR40", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_HS - LR40 - CT20")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_HS_LR40_CT20", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_HS - LR40 - CT60")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_HS_LR40_CT60", force_rewrite=True, postprocessing_module="it2020")

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
model.read_input_data("parameters_planning_HS - LR40 - CT120")

# solve model
model.run(solver='gurobi',verbosity=True, force_rewrite= True)

# create a new results folder (only if you haven't done so already)
# os.mkdir(base_path + "/results/")

# write result to csv in the it2020 format
model.to_csv(path="results_planning" + r"\result_scenario_HS_LR40_CT120", force_rewrite=True, postprocessing_module="it2020")

#%%
# Merge result csv for different scenarios
italy2020_merge_results(
    scenarios={
        "scenario1": "results_planning" + "/result_scenario_BC/",
        "scenario2": "results_planning" + "/result_scenario_LS/",
        "scenario3": "results_planning" + "/result_scenario_LS_CT20/",
        "scenario4": "results_planning" + "/result_scenario_LS_CT60/",
        "scenario5": "results_planning" + "/result_scenario_LS_CT120/",
        "scenario6": "results_planning" + "/result_scenario_LS_LR19/",
        "scenario7": "results_planning" + "/result_scenario_LS_LR19_CT20/",
        "scenario8": "results_planning" + "/result_scenario_LS_LR19_CT60/",
        "scenario9": "results_planning" + "/result_scenario_LS_LR19_CT120/",
        "scenario10": "results_planning" + "/result_scenario_LS_LR22/",
        "scenario11": "results_planning" + "/result_scenario_LS_LR22_CT20/",
        "scenario12": "results_planning" + "/result_scenario_LS_LR22_CT60/",
        "scenario13": "results_planning" + "/result_scenario_LS_LR22_CT120/",
        "scenario14": "results_planning" + "/result_scenario_LS_LR25/",
        "scenario15": "results_planning" + "/result_scenario_LS_LR25_CT20/",
        "scenario16": "results_planning" + "/result_scenario_LS_LR25_CT60/",
        "scenario17": "results_planning" + "/result_scenario_LS_LR25_CT120/",
        "scenario18": "results_planning" + "/result_scenario_LS_LR28/",
        "scenario19": "results_planning" + "/result_scenario_LS_LR28_CT20/",
        "scenario20": "results_planning" + "/result_scenario_LS_LR28_CT60/",
        "scenario21": "results_planning" + "/result_scenario_LS_LR28_CT120/",
        "scenario22": "results_planning" + "/result_scenario_LS_LR31/",
        "scenario23": "results_planning" + "/result_scenario_LS_LR31_CT20/",
        "scenario24": "results_planning" + "/result_scenario_LS_LR31_CT60/",
        "scenario25": "results_planning" + "/result_scenario_LS_LR31_CT120/",
        "scenario26": "results_planning" + "/result_scenario_LS_LR34/",
        "scenario27": "results_planning" + "/result_scenario_LS_LR34_CT20/",
        "scenario28": "results_planning" + "/result_scenario_LS_LR34_CT60/",
        "scenario29": "results_planning" + "/result_scenario_LS_LR34_CT120/",
        "scenario30": "results_planning" + "/result_scenario_LS_LR37/",
        "scenario31": "results_planning" + "/result_scenario_LS_LR37_CT20/",
        "scenario32": "results_planning" + "/result_scenario_LS_LR37_CT60/",
        "scenario33": "results_planning" + "/result_scenario_LS_LR37_CT120/",
        "scenario34": "results_planning" + "/result_scenario_LS_LR40/",
        "scenario35": "results_planning" + "/result_scenario_LS_LR40_CT20/",
        "scenario36": "results_planning" + "/result_scenario_LS_LR40_CT60/",
        "scenario37": "results_planning" + "/result_scenario_LS_LR40_CT120/",
        "scenario38": "results_planning" + "/result_scenario_HS/",
        "scenario39": "results_planning" + "/result_scenario_HS_CT20/",
        "scenario40": "results_planning" + "/result_scenario_HS_CT60/",
        "scenario41": "results_planning" + "/result_scenario_HS_CT120/",
        "scenario42": "results_planning" + "/result_scenario_HS_LR19/",
        "scenario43": "results_planning" + "/result_scenario_HS_LR19_CT20/",
        "scenario44": "results_planning" + "/result_scenario_HS_LR19_CT60/",
        "scenario45": "results_planning" + "/result_scenario_HS_LR19_CT120/",
        "scenario46": "results_planning" + "/result_scenario_HS_LR22/",
        "scenario47": "results_planning" + "/result_scenario_HS_LR22_CT20/",
        "scenario48": "results_planning" + "/result_scenario_HS_LR22_CT60/",
        "scenario49": "results_planning" + "/result_scenario_HS_LR22_CT120/",
        "scenario50": "results_planning" + "/result_scenario_HS_LR25/",
        "scenario51": "results_planning" + "/result_scenario_HS_LR25_CT20/",
        "scenario52": "results_planning" + "/result_scenario_HS_LR25_CT60/",
        "scenario53": "results_planning" + "/result_scenario_HS_LR25_CT120/",
        "scenario54": "results_planning" + "/result_scenario_HS_LR28/",
        "scenario55": "results_planning" + "/result_scenario_HS_LR28_CT20/",
        "scenario56": "results_planning" + "/result_scenario_HS_LR28_CT60/",
        "scenario57": "results_planning" + "/result_scenario_HS_LR28_CT120/",
        "scenario58": "results_planning" + "/result_scenario_HS_LR31/",
        "scenario59": "results_planning" + "/result_scenario_HS_LR31_CT20/",
        "scenario60": "results_planning" + "/result_scenario_HS_LR31_CT60/",
        "scenario61": "results_planning" + "/result_scenario_HS_LR31_CT120/",
        "scenario62": "results_planning" + "/result_scenario_HS_LR34/",
        "scenario63": "results_planning" + "/result_scenario_HS_LR34_CT20/",
        "scenario64": "results_planning" + "/result_scenario_HS_LR34_CT60/",
        "scenario65": "results_planning" + "/result_scenario_HS_LR34_CT120/",
        "scenario66": "results_planning" + "/result_scenario_HS_LR37/",
        "scenario67": "results_planning" + "/result_scenario_HS_LR37_CT20/",
        "scenario68": "results_planning" + "/result_scenario_HS_LR37_CT60/",
        "scenario69": "results_planning" + "/result_scenario_HS_LR37_CT120/",
        "scenario70": "results_planning" + "/result_scenario_HS_LR40/",
        "scenario71": "results_planning" + "/result_scenario_HS_LR40_CT20/",
        "scenario72": "results_planning" + "/result_scenario_HS_LR40_CT60/",
        "scenario73": "results_planning" + "/result_scenario_HS_LR40_CT120/",
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