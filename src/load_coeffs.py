import json
import sys
from pathlib import Path

def parse_coeff_item(item):
    """
    将配置项解析为复数或浮点数。
    支持：数字 -> 浮点数（虚部为0）
          [real, imag] -> complex(real, imag)
    """
    if isinstance(item, (int, float)):
        return float(item)               # 纯实数
    if isinstance(item, list) and len(item) == 2:
        real, imag = item
        return complex(float(real), float(imag))
    raise ValueError(f"无法解析为复数: {item}")

def load_coeffs_from_config(config_path='configs/config.json'):
    """从 JSON 配置文件读取系数列表"""
    project_root = Path(__file__).parents[1]
    config_file = project_root / config_path
    
    if not config_file.exists():
        print(f"错误：配置文件 {config_file} 不存在。")
        sys.exit(1)

    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        coeffs_raw = data.get("coeffs")
        if coeffs_raw is None or not isinstance(coeffs_raw, list) or len(coeffs_raw) != 5:
            print("错误：配置文件中必须包含长度为5的列表 'coeffs'。")
            sys.exit(1)
        coeffs = [parse_coeff_item(item) for item in coeffs_raw]
        return coeffs
    except (json.JSONDecodeError, ValueError) as e:
        print(f"配置文件解析失败：{e}")
        sys.exit(1)