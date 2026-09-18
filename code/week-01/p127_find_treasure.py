"""
deep-ml #127 Find Captain Redbeard's Hidden Treasure (medium, calculus)
Суть: точка минимума f(x) = x^4 - 3x^3 + 2 при любом start_x.
Вывод: чистый GD сходится к седлу x=0 при старте < 0 -> надёжно аналитическое решение.
Статус: сдана 2026-09-18
"""

import numpy as np


def find_treasure(start_x: float) -> float:
    """
    Find the x-coordinate where f(x) = x^4 - 3x^3 + 2 is minimized.

  Returns:
        float: The x-coordinate of the minimum point.
    """
    # Аналитическое решение:
    # x^2(4x - 9) = 0
    # x^2 = 0 -> x = 0
    # 4x - 9 = 0 -> x = 9/4

    # Выбор минимума: f''(x) = 12x^2 - 18x
    #   f''(0)   = 0     -> седло, не минимум
    #   f''(9/4) = 20.25 -> минимум -> возвращаем 9/4
    
    return 9/4

print(find_treasure(-1))