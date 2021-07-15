import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(func):
    def wrapper():
        current_time = time.time()
        func()
        end_time = time.time()
        print(f"{func.__name__}:{end_time-current_time}")
    return wrapper

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()

