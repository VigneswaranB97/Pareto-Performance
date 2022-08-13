import matplotlib.pyplot as plt
import numpy as np

from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.optimize import minimize
from pymoo.visualization.scatter import Scatter
from pymoo.core.problem import ElementwiseProblem

class MyProblem(ElementwiseProblem):

    def __init__(self, n_var=2, n_obj=2, n_ieq_constr=2, xl=np.array([0, 0]), xu=np.array([2, 2]) ):
        super().__init__(n_var=n_var,
                         n_obj=n_obj,
                         n_ieq_constr=n_ieq_constr,
                         xl=xl,
                         xu=xu)

    def _evaluate(self, x, out, *args, **kwargs):
        f1 = 100 * (x[0]**2 + x[1]**2)
        f2 = (x[0]-1)**2 + x[1]**2

        g1 = 2*(x[0]-0.1) * (x[0]-0.9) / 0.18
        g2 = - 20*(x[0]-0.4) * (x[0]-0.6) / 4.8

        out["F"] = [f1, f2]
        out["G"] = [g1, g2]





problem = MyProblem()

algorithm = NSGA2()

res = minimize(problem,
               algorithm,
               ('n_gen', 200),
               seed=1,
               verbose=True)

print(res.X)
print(res.F)

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
Scatter(fig=fig, ax=ax1, title="Design Space").add(res.X, color="blue").do()
Scatter(fig=fig, ax=ax2, title="Objective Space").add(res.F, color="red").do()
plt.show()