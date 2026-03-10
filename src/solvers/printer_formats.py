def format_complex(z, precision=4):
    """
    将复数（或实数）格式化为 'a+bi' 形式的字符串，虚部使用 i。
    自动处理虚部为 0、±1 的情况，并去除多余尾随零。
    """
    # 处理实数情况（直接返回格式化后的实数）
    if isinstance(z, (int, float)):
        real = float(z)
        imag = 0.0
    else:
        real = z.real
        imag = z.imag

    # 如果虚部接近于 0，当作实数处理
    if abs(imag) < 1e-12:
        if abs(real) < 1e-12:
            return "0"
        # 格式化实数，保留 precision 位小数，去除多余零
        real_str = f"{real:.{precision}f}".rstrip('0').rstrip('.')
        return real_str

    # 处理实部
    if abs(real) < 1e-12:
        real_str = ""
    else:
        real_str = f"{real:.{precision}f}".rstrip('0').rstrip('.')
        if real_str == "":
            real_str = "0"

    # 处理虚部
    if abs(imag - 1) < 1e-12:
        imag_str = "i"
    elif abs(imag + 1) < 1e-12:
        imag_str = "-i"
    else:
        imag_str = f"{abs(imag):.{precision}f}".rstrip('0').rstrip('.')
        if imag_str == "":
            imag_str = "1"
        imag_str += "i"
        if imag < 0:
            imag_str = "-" + imag_str

    # 组合实部和虚部
    if real_str == "":
        return imag_str
    else:
        if imag_str.startswith('-'):
            return f"{real_str}{imag_str}"
        else:
            return f"{real_str}+{imag_str}"

def format_polynomial(coeffs, precision=4):
    """
    将多项式系数列表格式化为美观的字符串（如 "(1+2i)x^4 + (-3-4i)x^3 + 5x^2 - 6 = 0"）。
    coeffs: list，从最高次到常数项，支持 int、float、complex。
    precision: 小数位数（用于格式化浮点数）。
    """
    # 复制系数列表，避免修改原列表
    coeffs = coeffs[:]
    # 去除前导零（系数为零的项）
    while coeffs and abs(coeffs[0]) < 1e-12:
        coeffs.pop(0)
    if not coeffs:
        return "0 = 0"

    n = len(coeffs) - 1          # 最高次数
    terms = []

    for i, a in enumerate(coeffs):
        if abs(a) < 1e-12:        # 跳过零系数
            continue
        exp = n - i                # 当前项的指数

        # 判断是否为复数（虚部非零）
        if isinstance(a, complex) and abs(a.imag) > 1e-12:
            # 复数系数
            coeff_str = format_complex(a, precision)
            coeff_str = f"({coeff_str})"   # 用括号括起来
        else:
            # 实数系数（包括虚部接近零的复数）
            real_val = a.real if isinstance(a, complex) else a
            abs_val = abs(real_val)
            # 系数部分（绝对值）
            if exp > 0:
                if abs_val == 1:
                    coeff_part = ""         # 系数为 ±1 时省略数字
                else:
                    coeff_part = f"{abs_val:.{precision}f}".rstrip('0').rstrip('.')
            else:
                coeff_part = f"{abs_val:.{precision}f}".rstrip('0').rstrip('.')
            # 变量部分
            if exp == 0:
                var_part = ""
            elif exp == 1:
                var_part = "x"
            else:
                var_part = f"x^{{{exp}}}"   # LaTeX 格式，纯文本可去掉花括号
            # 符号处理
            if real_val > 0:
                sign = "+" if terms else ""   # 第一项不加正号
            elif real_val < 0:
                sign = "-" if terms else "-"  # 第一项为负时直接加负号
            else:
                continue   # 已跳过零
            term = sign + coeff_part + var_part
            terms.append(term)
            continue   # 已添加，跳过下面的通用处理

        # 对于复数系数，构造项：括号 + 变量部分，并用加号连接（第一项不加）
        if exp == 0:
            var_part = ""
        elif exp == 1:
            var_part = "x"
        else:
            var_part = f"x^{{{exp}}}"
        if terms:
            term = "+" + coeff_str + var_part
        else:
            term = coeff_str + var_part
        terms.append(term)

    left_side = "".join(terms)
    return f"{left_side} = 0"