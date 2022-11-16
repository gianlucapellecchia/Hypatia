Solution_number = 1

optimal_value = 1

cost_relaxation = 0

Last_GINI_solution = 7

Land_only_solutions = 0

GINI_only_solutions = 0

Both_solutions = 0



import numpy as np
import cvxpy as cp

def Gini(demand, generation):
    assert(len(demand)== len(generation))
    bins = np.linspace(0., 100., len(demand))
    total_demand = float(np.sum(demand))
    total_generation = float(np.sum(generation))
    yvals_demand = []
    yvals_generation = []
    demand_fraction = np.zeros(len(demand))
    generation_fraction = np.zeros(len(generation))
    demand_vals = np.zeros(len(demand))
    generation_vals = np.zeros(len(generation))

    for d in bins:
        demand_vals = demand[demand <= np.percentile(demand, d)]
        #print(demand_vals)
        demand_fraction = (np.sum(demand_vals) / total_demand) * 100.0
        yvals_demand.append(demand_fraction)
        
    #print(yvals_demand)

    for g in bins:
        generation_vals = generation[generation <= np.percentile(generation, g)]
        generation_fraction = (np.sum(generation_vals) / total_generation) * 100.0
        yvals_generation.append(generation_fraction)
        
    #print(yvals_generation)
    # perfect equality area
    pe_area = np.trapz(yvals_demand, x=yvals_demand)
    # lorenz area
    lorenz_area = np.trapz(yvals_generation, x=yvals_demand)
    gini_val = abs((pe_area - lorenz_area) / float(pe_area))
    return gini_val

demand = np.array([150,250,300,300,10000])
generation = np.array([100,3,300,250,150])


def G(v):
    bins = np.linspace(0., 100., 11)
    total = float(np.sum(v))
    yvals = []
    for b in bins:
        bin_vals = v[v <= np.percentile(v, b)]
        print(bin_vals)
        bin_fraction = (np.sum(bin_vals) / total) * 100.0
        yvals.append(bin_fraction)
    # perfect equality area
    pe_area = np.trapz(bins, x=bins)
    # lorenz area
    lorenz_area = np.trapz(yvals, x=bins)
    gini_val = (pe_area - lorenz_area) / float(pe_area)
    return bins, yvals, gini_val

d = {}
e = {}
d['Y0'] = (150, 200,300, 200, 180, 250)
d['Y1'] = (150, 20,300, 200, 180, 250)
e['Y0'] = (150, 200,300, 200, 180, 250)
e['Y1'] = (1500, 10,300, 2000, 180, 250)
f = {'a':2000, 'b':20, 'c':20000, 'd': 2000, 'e': 1800, 'f':250}
z = np.array(list(d.values()))
j = np.array(list(e.values()))
y = []
#print(z,type(z))
#print(e,type(e))
for i in range(len(z)):
    y.append(Gini(z[i],j[i]))
#print(y)
l = list(d.values())
g = list(f.values())
b = np.array(g)
a = np.array(l)

def Gini2(demand, generation):
    bins = np.linspace(0., 100., len(demand))
    total_demand = float(np.sum(demand))
    total_generation = float(np.sum(generation))
    yvals_demand = []
    yvals_generation = []
    yvals = []
    demand_fraction = np.zeros(len(demand))
    generation_fraction = np.zeros(len(generation))
    demand_vals = np.zeros(len(demand))
    generation_vals = np.zeros(len(generation))

    for d in bins:
        demand_vals = demand[demand <= np.percentile(demand, d)]
        #print(demand_vals)
        demand_fraction = (np.sum(demand_vals) / total_demand) * 100.0
        yvals_demand.append(demand_fraction)
        
    #print(yvals_demand)

    for g in bins:
        generation_vals = generation[generation <= np.percentile(generation, g)]
        generation_fraction = (np.sum(generation_vals) / total_generation) * 100.0
        yvals_generation.append(generation_fraction)
        
    #print(yvals_generation)
    for i in range(len(yvals_demand)):
        if yvals_demand[i] >= yvals_generation[i]:
            yvals.append(yvals_generation[i])
        else:
            yvals.append(2*yvals_demand[i]-yvals_generation[i])
    # perfect equality area
    pe_area = np.trapz(yvals_demand, x=yvals_demand)
    # lorenz area
    lorenz_area = np.trapz(yvals, x=yvals_demand)
    gini_val = (pe_area - lorenz_area) / float(pe_area)
    return bins, yvals_demand,yvals_generation, yvals ,gini_val

#print(Gini(demand,generation))

r = np.tile(np.random.random((1,5)),(2,1))
s = cp.sum(cp.sum(r, axis = 0, keepdims = True), axis = 1, keepdims = True)
#print(r, np.shape(r), type(r))
#print(s, np.shape(s), type(s))
#print(s+ 2)
 
    


import pandas as pd

# data = pd.read_csv('/Users/giovannifalcione/opt/anaconda3/envs/hypatia/lib/python3.8/site-packages/hypatia/results_close_to_optimal/results_1/actualized_total_cost.csv')
# tot_trad = 0
# for val in data.values[:,1]:
#     tot_trad += val
#     #print(val)

# print('the tot is',tot_trad)

# dataland = pd.read_csv('/Users/giovannifalcione/opt/anaconda3/envs/hypatia/lib/python3.8/site-packages/hypatia/results_close_to_optimal/results_2/actualized_total_cost.csv')
# tot_land = 0
# for val in dataland.values[:,1]:
#     tot_land += val
#     #print(val)

# print('the tot is',tot_land)

# cost_ratio =  tot_land/tot_trad
# print(cost_ratio)  

# datalandrand = pd.read_csv('/Users/giovannifalcione/opt/anaconda3/envs/hypatia/lib/python3.8/site-packages/hypatia/results_close_to_optimal/results_3/actualized_total_cost.csv')
# tot_landrand = 0
# for val in datalandrand.values[:,1]:
#     tot_landrand += val
#     #print(val)

# print('the tot is',tot_landrand)

# cost_ratiorand =  tot_landrand/tot_trad
# print(cost_ratiorand) 

tot_cost_land = np.zeros(4)
cost_ratio = np.zeros(4)

for i in range(2,6):
    dataland = pd.read_csv('/Users/giovannifalcione/opt/anaconda3/envs/hypatia/lib/python3.8/site-packages/hypatia/results_close_to_optimal_onlyland_RES_studycase/results_' + str(i) + '/actualized_total_cost.csv')
    for val in dataland.values[:,1]:
        tot_cost_land[i-2] += val
    cost_ratio[i-2] = (tot_cost_land[i-2]/642603828360.5422 - 1) * 100 


print(tot_cost_land)
print(cost_ratio)

# data_capacity = pd.read_csv('/Users/giovannifalcione/opt/anaconda3/envs/hypatia/lib/python3.8/site-packages/hypatia/results_close_to_optimal/results_4/total_capacity.csv')

# solar_values = data_capacity.values[306:357,5]

# wind_values = data_capacity.values[357:408,5]










