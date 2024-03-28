import time
from numba import njit, prange
from typing import Callable

precision = 10000000

@njit(nopython=True, fastmath=True)
def funcion(x):
    return x**2 + 5

@njit(parallel=True, fastmath=True)
def find_integral(func:Callable, a:float, b:float, precision:int) -> float:
    sum_vals:float = 0
    domain:float = b - a
    inverse_precision:float = 1/precision
    
    for i in prange(1, precision):
        sum_vals += func(b - i * domain * inverse_precision)
        
    return sum_vals * domain * inverse_precision

def time_it(func, a, b, precision):
    sum_returns = 0
    for i in range(20):
        start = time.perf_counter()
        val = find_integral(func, a, b, precision)
        end = time.perf_counter()
        sum_returns += end - start
    print(sum_returns)
    
    
time_it(funcion, -900, 900, precision)