#!/usr/bin/python
import euler

Costs = euler.read_matrix('data/p081_matrix.txt')

PathCost = []
for r in Costs:
    assert len(r) == len(Costs)
    PathCost.append([-1] * len(r))

# Sentinel
PathCost[len(Costs)-1][len(Costs)-1] = Costs[len(Costs)-1][len(Costs)-1]

def get_cost(costs, path_costs, r, c):
    if path_costs[r][c] < 0:
        valid = []
        if (c < len(costs) - 1): valid.append(get_cost(Costs, path_costs, r, c+1))
        if (r < len(costs) - 1): valid.append(get_cost(Costs, path_costs, r+1, c))
            
        path_costs[r][c] = costs[r][c] + min(valid)
        
    return path_costs[r][c]
    
print(get_cost(Costs, PathCost, 0, 0))
