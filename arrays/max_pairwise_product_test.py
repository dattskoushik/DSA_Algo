import random
import time
from max_pairwise_product import maxPairWiseProduct, maxPairWiseProductFast

def generate_random_input(size):
    return [random.randint(0, 1000) for _ in range(size)]

def stress_test(func, input_size):
    input_data = generate_random_input(input_size)
    start_time = time.time()
    result = func(input_data)
    end_time = time.time()
    print(f"Function {func.__name__} took {end_time - start_time:.2f} seconds to execute with input size {input_size}")
    return result

input_sizes = [100, 1000, 10000, 100000]
for size in input_sizes:
    stress_test(maxPairWiseProduct(), size)
    stress_test(maxPairWiseProductFast, size)