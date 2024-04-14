import random


def random_search(func, bounds, dimensions, iterations):
    min_val, max_val = bounds
    best_solution = None
    fitness_arr = [(0, float('inf'))]

    for i in range(iterations):
        func_args = [random.uniform(min_val, max_val) for _ in range(dimensions)]
        fitness = func(func_args)

        if fitness < fitness_arr[-1][1]:
            best_solution = func_args
            fitness_arr.append((i+1, fitness))
        else:
            fitness_arr.append(fitness_arr[-1])

    return best_solution, fitness_arr[1:]
