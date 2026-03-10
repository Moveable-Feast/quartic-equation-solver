import math
from pathlib import Path
from .printer_formats import format_polynomial, format_complex

project_root = Path(__file__).resolve().parents[2]
file_address = project_root / 'results' / 'degree_3_solution.md'

class Solver:
    def __init__(self, coeffs):
        self.a = coeffs[1]
        self.b = coeffs[2]
        self.c = coeffs[3]
        self.d = coeffs[4]
        self.coeffs = coeffs

    def parameters(self):
        a, b, c, d = self.a, self.b, self.c, self.d
        alpha = b * c / (6 * a ** 2) - b ** 3 / (27 * a ** 3) - d / (2 * a)
        beta = c / (3 * a) - b ** 2 / (9 * a ** 2)
        Delta = alpha ** 2 + beta ** 3
        return alpha, beta, Delta
    
    def solver(self):
        a, b, c, d = self.a, self.b, self.c, self.d
        alpha, beta, Delta = self.parameters()
        omega = (-1 + math.sqrt(3) * 1j) / 2
        omega_bar = (-1 - math.sqrt(3) * 1j) / 2
        x_1 = -b / (3 * a) + (alpha + Delta ** (1 / 2)) ** (1 / 3) + (alpha - Delta ** (1 / 2)) ** (1 / 3)
        x_2 = -b / (3 * a) + omega * (alpha + Delta ** (1 / 2)) ** (1 / 3) + omega_bar * (alpha - Delta ** (1 / 2)) ** (1 / 3)
        x_3 = -b / (3 * a) + omega_bar * (alpha + Delta ** (1 / 2)) ** (1 / 3) + omega * (alpha - Delta ** (1 / 2)) ** (1 / 3)
        return x_1, x_2, x_3
    
    def printer(self):
        a, b, c, d = self.a, self.b, self.c, self.d
        alpha, beta, Delta = self.parameters()
        x_1, x_2, x_3 = self.solver()

        poly_str = format_polynomial(self.coeffs)

        a_str = format_complex(a)
        b_str = format_complex(b)
        c_str = format_complex(c)
        d_str = format_complex(d)

        alpha_str = format_complex(alpha)
        beta_str = format_complex(beta)
        Delta_str = format_complex(Delta)

        x_1_str = format_complex(x_1)
        x_2_str = format_complex(x_2)
        x_3_str = format_complex(x_3)
        
        if not (isinstance(x_1, (int, float)) and isinstance(x_2, (int, float)) and isinstance(x_3, (int, float))):
            complex_roots = f'''
where
$$
i = \\sqrt{{-1}}, \omega = \\dfrac{{-1 + \\sqrt{{3}}i}}{{2}}.
$$
'''
        else:
            complex_roots = f'''
where
$$
\omega = \\dfrac{{-1 + \\sqrt{{3}}i}}{{2}}.
$$
'''

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
    c = {c_str} \\\\
    d = {d_str}
\\end{{cases}}
$$
Parameters:
$$
\\begin{{cases}}
    \\alpha = \\dfrac{{bc}}{{6a ^ 2}} - \\dfrac{{b ^ 3}}{{27a ^ 3}} - \\dfrac{{d}}{{2a}} = {alpha_str} \\\\
    \\beta = \\dfrac{{c}}{{3a}} - \\dfrac{{b ^ 2}}{{9a ^ 2}} = {beta_str} \\\\
    \\Delta = \\alpha ^ 2 + \\beta ^ 3 = {Delta_str}
\\end{{cases}}
$$
Solutions:
$$
\\begin{{cases}}
x_1 = \\dfrac{{-b}}{{3a}} + \\sqrt[3]{{\\alpha + \\sqrt{{\Delta}}}} + \\sqrt[3]{{\\alpha - \\sqrt{{\Delta}}}} = {x_1_str} \\\\
x_2 = \\dfrac{{-b}}{{3a}} + \\omega\\sqrt[3]{{\\alpha + \\sqrt{{\Delta}}}} + \\overline{{\\omega}}\\sqrt[3]{{\\alpha - \\sqrt{{\Delta}}}} = {x_2_str} \\\\
x_3 = \\dfrac{{-b}}{{3a}} + \\overline{{\\omega}}\\sqrt[3]{{\\alpha + \\sqrt{{\Delta}}}} + \\omega\\sqrt[3]{{\\alpha - \\sqrt{{\Delta}}}} = {x_3_str}
\\end{{cases}}
$$
{complex_roots}
'''
        
        file_address.parent.mkdir(parents=True, exist_ok=True)
        with open(file_address, 'a', encoding='utf-8') as f:
            f.write(md)