from typing import Tuple, List, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:

    zoomed_in: List = [item for item in lst for i in range(factor)]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

# bob@dylan:~$ mypy 102-type_checking.py
# Success: no issues found in 1 source file
# bob@dylan:~$ cat 102-main.py
