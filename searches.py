import random
import math
import numpy as np

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
            fitness_arr.append((i+1, fitness_arr[-1][1]))

    return best_solution, fitness_arr[1:]


def simulated_annealing(func, bounds, dimensions):
    # PARAMS
    T0 = 12
    T_decrease = 0.011999
    metropolis_calls = 10
    iterations = 1000
    #
    T = T0
    min_val, max_val = bounds
    current_state = [random.uniform(min_val, max_val) for _ in range(dimensions)]
    fitness_arr = []

    for i in range(iterations):
        for j in range(metropolis_calls):
            new_state = __sa_generate_new_state(current_state=current_state, bounds=bounds)
            if __sa_accept_solution(func(current_state), func(new_state), T):
                current_state = new_state
            fitness_arr.append((i * metropolis_calls + j + 1, func(current_state)))
        T -= T_decrease

    return fitness_arr


def __sa_accept_solution(current_score, next_score, T) -> bool:
    if current_score > next_score:
        return True
    threshold = pow(math.e, -(next_score - current_score)/T)
    rnd = random.uniform(0, 1)
    return rnd <= threshold


def __sa_generate_new_state(current_state, bounds):
    interval_width = abs((bounds[0] - bounds[1]) * 0.1)
    new_state = [np.random.normal(loc=x0, scale=interval_width/2) for x0 in current_state]
    return [max(min(x, bounds[1]), bounds[0]) for x in new_state]
