import pulp

def get_linear_programming_scores(suppliers, data, objective, tends_to_value):
    supplier = pulp.LpVariable.dicts("supplier", suppliers, lowBound=0, cat='Integer')
    objective_fn = pulp.lpSum([(supplier[i] * (data[i]))] for i in suppliers)

    # Create the 'prob' variable to contain the problem data
    prob = pulp.LpProblem("Supplier_Performance_Problem", pulp.LpMaximize if objective == "Maximize" else pulp.LpMinimize)

    # The objective function is added to 'prob' first
    prob += objective_fn

    # The constraints are added to 'prob'
    if objective == "Maximize":
        prob += objective_fn <= tends_to_value
    else:
        prob += objective_fn >= tends_to_value

    pulp.PULP_CBC_CMD(msg=False).solve(prob)

    scores = {}

    for v in prob.variables():
        name = v.name[9:]
        try:
            scores[name] = v.varValue
        except Exception as e:
            print(f'v.varValue None {e}')
            scores[name] = 0

    return scores
