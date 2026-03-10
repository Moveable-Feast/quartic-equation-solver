from pathlib import Path
from .printer_formats import format_polynomial, format_complex

project_root = Path(__file__).resolve().parents[2]
file_address = project_root / 'results' / 'degree_1_solution.md'

class Solver:
    def __init__(self, coeffs):
        self.a = coeffs[3]
        self.b = coeffs[4]
        self.coeffs = coeffs
    
    def solver(self):
        a, b = self.a, self.b
        x = -b / a

        return x
    
    def printer(self):
        a, b = self.a, self.b
        x = self.solver()
        
        poly_str = format_polynomial(self.coeffs)

        a_str = format_complex(a)
        b_str = format_complex(b)

        x_str = format_complex(x)

        if not (isinstance(x, (int, float))):
            complex_roots = f'''
where
$$
i = \\sqrt{{-1}}.
$$
'''
        else:
            complex_roots = ''

        md = f'''
---
Solve:
$$
{poly_str}
$$
Coefficients:
$$
\\begin{{cases}}
    a = {a_str} \\\\
    b = {b_str}
\\end{{cases}}
$$
Solutions:
$$
x = -b / a = {x_str}
$$
{complex_roots}
'''
        
        file_address.parent.mkdir(parents=True, exist_ok=True)
        with open(file_address, 'a', encoding='utf-8') as f:
            f.write(md)