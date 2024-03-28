import time
from random import randint


class Prime_Finder:
    def __init__(self):
        self.set:set = set()
    
    def is_prime(self, num):
        if num <= 1: return False
        i = 2
        while i * i <= num:
            if num % i == 0: return False
            i += 1
        return True
        
    def find_all_primes(self, range_ints):
        found:set = set()
        
        for i in range(*range_ints):
            if self.is_prime(i):
                found.add(i)

        return found
        
    
class Function_Timer:
    def __init__(self):
        pass
        
    def time_it(self, func, args):
        start_time = time.perf_counter()
        func(*args)
        end_time = time.perf_counter()
   
        return end_time - start_time
    
    def time_it_with_res(self, func, args):
        start_time = time.perf_counter()
        res = func(*args)
        end_time = time.perf_counter()
   
        return (end_time - start_time, res)
        
        
if __name__ == '__main__':
    tester = Function_Timer()
    finder = Prime_Finder()
    range_vals = 0, 234789
    ##result = finder.find_all_primes(range_vals)
    time_took = tester.time_it(finder.find_all_primes, [range_vals])
    print(time_took)