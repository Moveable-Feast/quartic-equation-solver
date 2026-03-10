from email.charset import QP
import math
from pathlib import Path
from .printer_formats import format_polynomial, format_complex

project_root = Path(__file__).resolve().parents[2]
file_address = project_root / 'results' / 'degree_4_solution.md'

class Solver:
    def __init__(self, coeffs):
        self.a = coeffs[0]
        self.b = coeffs[1]
        self.c = coeffs[2]
        self.d = coeffs[3]
        self.e = coeffs[4]
        self.coeffs = coeffs

    def parameters_1(self):
        alpha = -3 * self.b ** 2 / (8 * self.a ** 2) + self.c / self.a
        beta = self.b ** 3 / (8 * self.a ** 3) - self.b * self.c / (2 * self.a ** 2) + self.d / self.a
        gamma = -3 * self.b ** 4 / (256 * self.a ** 4) + self.b ** 2 * self.c / (16 * self.a ** 3) - self.b * self.d / (4 * self.a ** 2) + self.e / self.a
        return alpha, beta, gamma
    
    def parameters_2(self):
        alpha, beta, gamma = self.parameters_1()
        P = -alpha ** 2 / 12 - gamma
        Q = -alpha ** 3 / 108 + alpha * gamma / 3 - beta ** 2 / 8
        Delta = Q ** 2 / 4 + P ** 3 / 27
        R = -Q / 2 + Delta ** (1 / 2)
        U = R ** (1 / 3)
        return P, Q, R, U
    
    def parameter_y(self):
        alpha, beta, gamma = self.parameters_1()
        P, Q, R, U = self.parameters_2()
        if R == 0:
            y = (-5 / 6) * alpha - Q ** (1 / 3)
        else:
            y = (-5 / 6) * alpha + U - P / (3 * U)
        return y
    
    def solver(self):
        a, b, c, d, e = self.a, self.b, self.c, self.d, self.e
        alpha, beta, gamma = self.parameters_1()
        P, Q, R, U = self.parameters_2()
        y = self.parameter_y()
        if beta == 0:
            x_1 = -b / (4 * a) + ((-alpha + (alpha ** 2 - 4 * gamma) ** (1 / 2)) / 2) ** (1 / 2)
            x_2 = -b / (4 * a) + ((-alpha - (alpha ** 2 - 4 * gamma) ** (1 / 2)) / 2) ** (1 / 2)
            x_3 = -b / (4 * a) - ((-alpha + (alpha ** 2 - 4 * gamma) ** (1 / 2)) / 2) ** (1 / 2)
            x_4 = -b / (4 * a) - ((-alpha - (alpha ** 2 - 4 * gamma) ** (1 / 2)) / 2) ** (1 / 2)
        else:
            x_1 = -b / (4 * a) + ((alpha + 2 * y) ** (1 / 2) + (-(3 * alpha + 2 * y + 2 * beta / (alpha + 2 * y) ** (1 / 2))) ** (1 / 2)) / 2
            x_2 = -b / (4 * a) + ((alpha + 2 * y) ** (1 / 2) - (-(3 * alpha + 2 * y + 2 * beta / (alpha + 2 * y) ** (1 / 2))) ** (1 / 2)) / 2
            x_3 = -b / (4 * a) + (-(alpha + 2 * y) ** (1 / 2) + (-(3 * alpha + 2 * y - 2 * beta / (alpha + 2 * y) ** (1 / 2))) ** (1 / 2)) / 2
            x_4 = -b / (4 * a) + (-(alpha + 2 * y) ** (1 / 2) - (-(3 * alpha + 2 * y - 2 * beta / (alpha + 2 * y) ** (1 / 2))) ** (1 / 2)) / 2
        return x_1, x_2, x_3, x_4
    
    def printer(self):
        a, b, c, d, e = self.a, self.b, self.c, self.d, self.e
        alpha, beta, gamma = self.parameters_1()
        P, Q, R, U = self.parameters_2()
        y = self.parameter_y()
        x_1, x_2, x_3, x_4 = self.solver()

        poly_str = format_polynomial(self.coeffs)

        a_str = format_complex(a)
        b_str = format_complex(b)
        c_str = format_complex(c)
        d_str = format_complex(d)
        e_str = format_complex(e)

        alpha_str = format_complex(alpha)
        beta_str = format_complex(beta)
        gamma_str = format_complex(gamma)

        P_str = format_complex(P)
        Q_str = format_complex(Q)
        R_str = format_complex(R)
        U_str = format_complex(U)

        y_str = format_complex(y)

        x_1_str = format_complex(x_1)
        x_2_str = format_complex(x_2)
        x_3_str = format_complex(x_3)
        x_4_str = format_complex(x_4)
        
        if not (isinstance(x_1, (int, float)) and isinstance(x_2, (int, float)) and isinstance(x_3, (int, float)) and isinstance(x_4, (int, float))):
            complex_roots = f'''
where
$$
i = \\sqrt{{-1}}.
$$
'''
        else:
            complex_roots = ''

        if beta == 0:
            solution_md = f'''
$$
\\begin{{cases}}
    x_1 = -\\dfrac{{b}}{{4a}} + \\sqrt{{\\dfrac{{-\\alpha + \\sqrt{{\\alpha^2 - 4\\gamma}}}}{{2}}}} = {x_1_str} \\\\
    x_2 = -\\dfrac{{b}}{{4a}} + \\sqrt{{\\dfrac{{-\\alpha - \\sqrt{{\\alpha^2 - 4\\gamma}}}}{{2}}}} = {x_2_str} \\\\
    x_3 = -\\dfrac{{b}}{{4a}} - \\sqrt{{\\dfrac{{-\\alpha + \\sqrt{{\\alpha^2 - 4\\gamma}}}}{{2}}}} = {x_3_str} \\\\
    x_4 = -\\dfrac{{b}}{{4a}} - \\sqrt{{\\dfrac{{-\\alpha - \\sqrt{{\\alpha^2 - 4\\gamma}}}}{{2}}}} = {x_4_str}
\\end{{cases}}
$$
'''
        else:
            solution_md = f'''
$$
\\begin{{cases}}
    x_1 = -\\dfrac{{b}}{{4a}} + \\dfrac{{\\sqrt{{\\alpha + 2y}} + \\sqrt{{-(3\\alpha + 2y + \\dfrac{{2\\beta}}{{\\sqrt{{\\alpha + 2y}}}})}}}}{{2}} = {x_1_str} \\\\
    x_2 = -\\dfrac{{b}}{{4a}} + \\dfrac{{\\sqrt{{\\alpha + 2y}} - \\sqrt{{-(3\\alpha + 2y + \\dfrac{{2\\beta}}{{\\sqrt{{\\alpha + 2y}}}})}}}}{{2}} = {x_2_str} \\\\
    x_3 = -\\dfrac{{b}}{{4a}} + \\dfrac{{-\\sqrt{{\\alpha + 2y}} + \\sqrt{{-(3\\alpha + 2y - \\dfrac{{2\\beta}}{{\\sqrt{{\\alpha + 2y}}}})}}}}{{2}} = {x_3_str} \\\\
    x_4 = -\\dfrac{{b}}{{4a}} + \\dfrac{{-\\sqrt{{\\alpha + 2y}} - \\sqrt{{-(3\\alpha + 2y - \\dfrac{{2\\beta}}{{\\sqrt{{\\alpha + 2y}}}})}}}}{{2}} = {x_4_str}
\\end{{cases}}
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
    d = {d_str} \\\\
    e = {e_str}
\\end{{cases}}
$$
Parameters:
$$
\\begin{{cases}}
    \\alpha = -\\dfrac{{3b^2}}{{8a^2}} + \\dfrac{{c}}{{a}} = {alpha_str} \\\\
    \\beta = \\dfrac{{b^3}}{{8a^3}} - \\dfrac{{bc}}{{2a^2}} + \\dfrac{{d}}{{a}} = {beta_str} \\\\
    \\gamma = -\\dfrac{{3b^4}}{{256a^4}} + \\dfrac{{b^2c}}{{16a^3}} - \\dfrac{{bd}}{{4a^2}} + \\dfrac{{e}}{{a}} = {gamma_str} \\\\
    P = -\\dfrac{{\\alpha^2}}{{12}} - \\gamma = {P_str} \\\\
    Q = -\\dfrac{{a^3}}{{108}} + \\dfrac{{\\alpha\\gamma}}{{3}} - \\dfrac{{\\beta^2}}{{8}} = {Q_str} \\\\
    R = -\\dfrac{{Q}}{{2}} \\pm \\sqrt{{\\dfrac{{Q^2}}{{4}} + \\dfrac{{P^3}}{{27}}}} = {R_str} \\\\
    U = \\sqrt[3]{{R}} = {U_str} \\\\
    y = -\\dfrac{{5}}{{6}}\\alpha +
    \\begin{{cases}}
        -\\sqrt[3]{{Q}}, U = 0 \\\\
        U - \\dfrac{{P}}{{3U}}, U \\neq 0
    \\end{{cases}}
    = {y_str}
\\end{{cases}}
$$
Solutions:
{solution_md}
{complex_roots}
'''
        
        file_address.parent.mkdir(parents=True, exist_ok=True)
        with open(file_address, 'a', encoding='utf-8') as f:
            f.write(md)