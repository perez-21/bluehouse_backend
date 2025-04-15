from typing import Mapping, Any, Union


def safely_get_value[T](
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
