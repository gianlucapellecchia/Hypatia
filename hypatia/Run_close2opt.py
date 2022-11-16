from hypatia import Model

import os

from hypatia import Utilities_close2opt

from hypatia.postprocessing import Italy2020PostProcessing

# First, define the optimization mode. It is possible to choose 2 options:
# "Single" -> traditional least-cost single solution optimization model  
# "Close2optimal" -> multiple solutions, where the first one is the same as the single solution, and the others have a different objective 
#                    function and an additional economic constraint (cost relaxation with respect to the total cost of the single solution result).

optimization_mode = "Close2optimal"

# Then, define the number of solutions you want to have while running the model. Please note that this only applies if the optimization mode is "Close2optimal". 
# Indeed, if it is in "Single", the model will still give only the results of the single traditional solution.
#
# If running in "Close2optimal", the type of solutions are going to be:
#
# (Multinode)
# 1: Traditional single solution
# 2: Close to optimal solution with GINI objective function
# 3 -> last_GINI_solution: Close to optimal solution with GINI objective function (randomic coefficients multiplying each production technology)
# last_GINI_solution + 1: Close to optimal solution with LAND objective function
# last_GINI_solution + 2 -> number_of_solutions: Close to optimal solution with LAND objective function (randomic coefficients multiplying each generation and storage technology)
#
# (Single node)
# 1: Traditional single solution
# 2: Close to optimal solution with LAND objective function
# 3 -> number_of_solutions: Close to optimal solution with LAND objective function (randomic coefficients multiplying each generation and storage technology)

number_of_solutions = 5

last_GINI_solution = 3

# This just described is the procedure if the user wants to run both the objective functions. 
# If, instead, the user wants to run with only either the land or the GINI objective function, it can be done in the following way:
# Assign 1 to the modality preferred, while for the other two modalities, leave a value different from 1. 
# for example, if we want to run with only the land objective function:
# both_solutions = 0
# land_only_solutions = 1
# GINI_only_solutions = 0
# The default setting is set to run with both the objective functions

both_solutions = 0
land_only_solutions = 1
GINI_only_solutions = 0

# These next five lines, check that only one mode has been chosen

count = 0
for modality in [both_solutions,land_only_solutions,GINI_only_solutions]:
    if modality == 1:
        count += 1
assert (count == 1)

# If the user desires to run with both objective functions, the model needs to check the following:

if both_solutions == 1:
    assert (last_GINI_solution < number_of_solutions)

# Then, choose the desired value of cost relaxation. Please note that the percentage value must be written in decimals (e.g. 15% -> 0.15)

cost_relaxation = 0.25



# This next line initializes the iterative solution_number to 1 (from utilities)

solution_number = Utilities_close2opt.Solution_number

#Inidicate the path where to store the results. The If-cycle allows to create a new results_path if the one indicated does not exist yet.

results_path = "/Users/giovannifalcione/opt/anaconda3/envs/hypatia/lib/python3.8/site-packages/hypatia/results_close_to_optimal_onlyland_RES_studycase"

if not os.path.exists(results_path):
    os.mkdir(results_path)

#The next line intializes a list with all the optimal values found. They will be printed after all the solutions have been run.

optimal_values = []

scenarios = {}

while solution_number <= number_of_solutions:
    model = Model(path="/Users/giovannifalcione/opt/anaconda3/envs/hypatia/lib/python3.8/site-packages/hypatia/sets_Carlo", mode="Planning", optimization = optimization_mode)
    # model.create_data_excels(
    # path ='/Users/giovannifalcione/opt/anaconda3/envs/hypatia/lib/python3.8/site-packages/hypatia/parameters_planning_RES_case_study',
    # force_rewrite=True
    # )
    model.read_input_data('/Users/giovannifalcione/opt/anaconda3/envs/hypatia/lib/python3.8/site-packages/hypatia/parameters_Carlo')
    print('Now running solution number:',str(solution_number))

    # 

    # This section is to print wich objective functions we are using in the whole cycle
    mod_vals = []
    for modality in [Utilities_close2opt.Both_solutions,Utilities_close2opt.Land_only_solutions,Utilities_close2opt.GINI_only_solutions]:
        mod_vals.append(modality)
    
    if mod_vals[0] == 1:
        print('Running with both objective functions mode')
    elif mod_vals[1] == 1:
        print('Running with only land objective function mode')
    elif mod_vals[2] == 1:
        print('Running with only GINI objective function mode')
    
    #

    optimal_value = model.run(solver='Gurobi')

    optimal_values.append(optimal_value)

    if not os.path.exists(results_path + "/results_" + str(solution_number)):
        os.mkdir(results_path + "/results_" + str(solution_number))
    
    model.to_csv(path=results_path + "/results_" + str(solution_number), force_rewrite=True, postprocessing_module="it2020")

    scenarios["scenario_" + str(solution_number)] = results_path + "/results_" + str(solution_number)

    if solution_number == 1:
        Utilities_close2opt.optimal_value = optimal_value
    
    if optimization_mode == "Single":
        break
    else:
        solution_number = solution_number + 1
        Utilities_close2opt.Solution_number = solution_number
        Utilities_close2opt.cost_relaxation = cost_relaxation
        Utilities_close2opt.Last_GINI_solution = last_GINI_solution 
        Utilities_close2opt.Both_solutions = both_solutions
        Utilities_close2opt.Land_only_solutions = land_only_solutions
        Utilities_close2opt.GINI_only_solutions = GINI_only_solutions

print(optimal_values)

print(scenarios)

Italy2020PostProcessing.italy2020_merge_results(scenarios=scenarios, path = '/Users/giovannifalcione/opt/anaconda3/envs/hypatia/lib/python3.8/site-packages/hypatia/merged_results_prova_25', force_rewrite= True)


        
