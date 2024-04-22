from searches import simulated_annealing
import functions
import matplotlib.pyplot as plt
import utils
from statistics import describe_run


def execute_sa(func, dimensions: int, title: str):
    results = []
    for i in range(30):
        result = simulated_annealing(func, functions.func_limits(func), dimensions)
        results.append(result)
        plt.plot([point[0] for point in result],
                 [point[1] for point in result], marker='', linestyle='-')
    utils.plot_template(title + " jednotlivá spuštění")

    avg_res = utils.average_score(results)
    plt.plot([point[0] for point in avg_res],
            [point[1] for point in avg_res], marker='', linestyle='-')
    utils.plot_template(title + " Average")
    print(title + " " + describe_run(results))
    return avg_res

if __name__ == '__main__':
    sa_avg_dej1_5d = execute_sa(functions.dejong_1st, 5, 'SA Dejong 1 5D')
    sa_avg_dej1_10d = execute_sa(functions.dejong_1st, 10, 'SA Dejong 1 10D')
    sa_avg_dej2_5d = execute_sa(functions.dejong_2nd, 5, 'SA Dejong 2 5D')
    sa_avg_dej2_10d = execute_sa(functions.dejong_2nd, 10, 'SA Dejong 2 10D')
    sa_avg_sch_5d = execute_sa(functions.schweffel, 5, 'SA Schweffel 5D')
    sa_avg_sch_10d = execute_sa(functions.schweffel, 10, 'SA Schweffel 10D')
