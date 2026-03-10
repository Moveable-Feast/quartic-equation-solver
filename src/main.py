import math
import load_coeffs

from solvers.degree_0 import Solver as d0
from solvers.degree_1 import Solver as d1
from solvers.degree_2 import Solver as d2
from solvers.degree_3 import Solver as d3
from solvers.degree_4 import Solver as d4

'''
config.json输入格式：
{
    "coeffs": [
        [0, 0],
        [0, 0],
        [0, 0],
        [2, 5],
        [-7, -2]
    ]
}
其中，[u, v]表示复数z=u+v*i。
'''

coeffs = load_coeffs.load_coeffs_from_config()

if coeffs[0] == 0:
    if coeffs[1] == 0:
        if coeffs[2] == 0:
            if coeffs[3] == 0:
                sol = d0(coeffs)
                sol.printer()
            else:
                sol = d1(coeffs)
                sol.printer()
        else:
            sol = d2(coeffs)
            sol.printer()
    else:
        sol = d3(coeffs)
        sol.printer()
else:
    sol = d4(coeffs)
    sol.printer()