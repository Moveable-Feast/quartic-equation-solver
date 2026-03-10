from pathlib import Path
from .printer_formats import format_polynomial

project_root = Path(__file__).resolve().parents[2]
file_address = project_root / 'results' / 'degree_0_solution.md'

class Solver:
    def __init__(self, coeffs):
        self.a = coeffs[4]
        self.coeffs = coeffs
    
    def printer(self):
        a = self.a
        poly_str = format_polynomial(self.coeffs)

        if a == 0:
            md = f'''
---
Solve:
$$
{poly_str}
$$
Solutions:
$$
x \in \mathbb{{C}}
$$
'''
        else:
            md = f'''---
Solve:
$$
{poly_str}
$$
Solution:
$$
x \in \\varnothing
$$
'''
        file_address.parent.mkdir(parents=True, exist_ok=True)
        with open(file_address, 'a', encoding='utf-8') as f:
            f.write(md)