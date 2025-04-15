from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiply(base: float):
        return base * multiplier

    return multiply
