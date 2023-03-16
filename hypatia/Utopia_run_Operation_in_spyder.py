"""
Utopia MODEL
Operation mode
"""

# Import of the Model

from hypatia import Model
import os
from hypatia import Merge_results
from hypatia import Plotter

#%% 
# Create the model using as input the sets files

Utopia = Model(
    path="examples/Operation/sets_operation",                           # Path to the sets folder
    mode="Operation",                                                   # "Planning" or "Operation" mode
)

#%% 
# Create the parameters with default values

Utopia.create_data_excels(
    path ='examples\Operation\parameters_operation',                    # Path to the parameters folder
    force_rewrite=True                                                  # Overwrite the parameters files (True) or not (False)
)

#%% 
# Read the parameters

Utopia.read_input_data("examples\Operation\parameters_operation")       # Path to the parameters folder

#%% 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

#%% 
# Create the folder where to save the results

os.mkdir("examples/Operation/results_operation/")                       # Path to the results folder

#%% 
# Save the results as csv file in the previous folder

Utopia.to_csv(
    path='examples/Operation/results_operation',                        # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% 
# Create the configuration file for the plots

Utopia.create_config_file(
    path = 'examples/Operation/config_operation.xlsx'                   # Path to the config file
)

#%% 
# Read the configuration file

plots = Plotter(
    results = Utopia,                                                   # Name of the Model
    config = 'examples/Operation/config_operation.xlsx',                # Path to the config file
    hourly_resolution = True,                                           # if model has an hourly resultion otherwise False
)

#%% 
# Plot the total capacity of each technology in the tech_group in each year and save it in the plots folder 

plots.plot_total_capacity(
    path = 'examples/Operation/plots_operation/totalcapacity.html',     # Path to the folder in which the plot will be saved
    tech_group = 'Power Generation',                                    # The group of the techs, reported in the configuration file, to be plotted
    kind= "bar",                                                        # "Bar" or "Area" are the two kind of plots accepted
    decom_cap=True,                                                     # Decommissioning capacity can be included (True) or not (False)
    regions="all",                                                      # The regions considered. "all" to consider all of them, ["reg1", ...] to consider only some regions
    aggregate=False                                                     # True to aggregate the results of each region, False to plot them separately
)

#%% 
# Plot the annual production of each technology in the tech_group in each year and save it in the plots folder 

plots.plot_prod_by_tech(
    path = 'examples/Operation/plots_operation/prod_by_tech.html',      # Path to the folder in which the plot will be saved
    tech_group = 'Power Generation',                                    # The group of the techs, reported in the configuration file, to be plotted
    kind="bar",                                                         # "Bar" or "Area" are the two kind of plots accepted
    regions="all",                                                      # The regions considered. "all" to consider all of them, ["reg1", ...] to consider only some regions
    aggregate=False                                                     # True to aggregate the results of each region, False to plot them separately
)

#%% 
# Plot the annual consumption of each carrier in the fuel_group in each year and save it in the plots folder 

plots.plot_use_by_technology(
    path = 'examples/Operation/plots_operation/use_by_tech.html',       # Path to the folder in which the plot will be saved
    fuel_group = 'Oil',                                                 # The group of the carriers, reported in the configuration file, to be plotted
    kind="bar",                                                         # "Bar" or "Area" are the two kind of plots accepted
    regions="all",                                                      # The regions considered. "all" to consider all of them, ["reg1", ...] to consider only some regions
    aggregate=False                                                     # True to aggregate the results of each region, False to plot them separately
)

#%%
# Plot as Pie chart the annual consumption and production of each carrier in the fuel_group for a specific year and save it in the plots folder

plots.plot_fuel_prod_cons(
    path = 'examples/Operation/plots_operation/prod_con_share__.html',  # Path to the folder in which the plot will be saved
    years = ["Y0"],                                                     # Year considered 
    fuel_group = 'Electricity',                                         # The group of the carriers, reported in the configuration file, to be plotted
    trade=False,                                                        # Trade can be included (True) or not (False)
    regions="all",                                                      # The regions considered. "all" to consider all of them, ["reg1", ...] to consider only some regions
    aggregate=False                                                     # True to aggregate the results of each region, False to plot them separately
)

#%% 
# Plot the annual emission of the emission_type for each technology in the tech_group in each year and save it in the plots folder

plots.plot_emissions(
    path = 'examples/Operation/plots_operation/emissions.html',         # Path to the folder in which the plot will be saved
    tech_group = 'Power Generation',                                    # The group of the techs, reported in the configuration file, to be plotted
    emission_type = ["CO2"],                                            # The type of the emissions, reported in the configuration file, to be plotted
    kind="bar",                                                         # "Bar" or "Area" are the two kind of plots accepted
    regions="all",                                                      # The regions considered. "all" to consider all of them, ["reg1", ...] to consider only some regions
    aggregate=True                                                     # Global emission can be plotted (True) or emission for each region (False)
)

#%%
# Plot the hourly production of the carrier in the fuel_group for each tech in the tech_group, from the start to the end time

plots.plot_hourly_prod_by_tech(
    path = 'examples/Operation/plots_operation/hourlyprod.html',        # Path to the folder in which the plot will be saved
    tech_group = 'Power Generation',                                    # The group of the techs, reported in the configuration file, to be plotted
    fuel_group = 'Electricity',                                         # The group of the carriers, reported in the configuration file, to be plotted
    kind = "bar",                                                       # "Bar" or "Area" are the two kind of plots accepted
    year = ["Y0"],                                                      # Year considered 
    start="01-01-2019 00:00:00",                                        # Starting day and time 
    end="01-01-2019 23:00:00",                                          # Ending day and time
    regions="all",                                                      # The regions considered. "all" to consider all of them, ["reg1", ...] to consider only some regions
    aggregate=False                                                     # Global emission can be plotted (True) or emission for each region (False)
)

#%%
# Plot the annual costs in each year and save it in the plots folder

plots.plot_regional_costs(
    path = 'examples/Operation/plots_operation/regionalcosts_bytechs.html', # Path to the folder in which the plot will be saved
    stacked_by = 'techs',                                                   # Plot can be stacked by "techs" or by cost "items"
    exclude_tech_groups=[],                                                 # Excluded tech groups
    exclude_cost_items=[],                                                  # Excluded cost items
    regions="all",                                                          # The regions considered. "all" to consider all of them, ["reg1", ...] to consider only some regions
    aggregate=False                                                         # Global emission can be plotted (True) or emission for each region (False)
)

