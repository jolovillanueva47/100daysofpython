import time
# current_time = time.time()
# print(current_time)

def speed_calc_decorator(function):
    def wrapper_func():
        start_time=time.time()
        function()
        end_time=time.time()
        return f"{function.__name__}:{end_time-start_time}"
    return wrapper_func

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast=fast_function()
print(fast)
slow=slow_function()
print(slow)