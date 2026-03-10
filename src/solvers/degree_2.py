import math
from pathlib import Path
from .printer_formats import format_polynomial, format_complex

project_root = Path(__file__).resolve().parents[2]
file_address = project_root / 'results' / 'degree_2_solution.md'

class Solver:
    def __init__(self, coeffs):
        self.a = coeffs[2]
        self.b = coeffs[3]
        self.c = coeffs[4]
        self.coeffs = coeffs
    
    def parameters(self):
        a, b, c = self.a, self.b, self.c
        Delta = b ** 2 - 4 * a * c
        return Delta

    def solver(self):
        a, b, c = self.a, self.b, self.c
        Delta = self.parameters()

        x_1 = (-b + Delta ** (1 / 2)) / (2 * a)
        x_2 = (-b - Delta ** (1 / 2)) / (2 * a)

        return x_1, x_2
    
    def printer(self):
        a, b, c = self.a, self.b, self.c
        x_1, x_2= self.solver()
        Delta = self.parameters()
        
        poly_str = format_polynomial(self.coeffs)

        a_str = format_complex(a)
        b_str = format_complex(b)
        c_str = format_complex(c)

        Delta_str = format_complex(Delta)

        x_1_str = format_complex(x_1)
        x_2_str = format_complex(x_2)
        
        if not (isinstance(x_1, (int, float)) and isinstance(x_2, (int, float))):
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
    b = {b_str} \\\\
    c = {c_str}
\\end{{cases}}
$$
Parameters:
$$
\\Delta = b^2 - 4ac = {Delta_str}
$$
Solutions:
$$
\\begin{{cases}}
x_1 = \\dfrac{{-b + \\sqrt{{\Delta}}}}{{2a}} = {x_1_str} \\\\
x_2 = \\dfrac{{-b - \\sqrt{{\Delta}}}}{{2a}} = {x_2_str}
\\end{{cases}}
$$
{complex_roots}
'''
        
        file_address.parent.mkdir(parents=True, exist_ok=True)
        with open(file_address, 'a', encoding='utf-8') as f:
            f.write(md)