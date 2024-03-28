import numba
import numpy as np
import time
from typing import Callable


def time_it(func:Callable, args:list) -> float:
    start = time.perf_counter()
    func(*args)
    end = time.perf_counter()
    return end - start


    