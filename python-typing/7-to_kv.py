from typing import Tuple


def to_kv(k: str, v: int | float) -> tuple[str, float]:
    return (k, pow(v, 2))
