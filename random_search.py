import functions
import searches
import utils
import matplotlib.pyplot as plt
from statistics import describe_run
from simulated_annealing import execute_sa

RANDOM_SEARCH_ITERATIONS = 10000

# RANDOM SEARCH 5D
rs_results_5d = []
for i in range(30):
    _, rs_steps = searches.random_search(functions.dejong_1st, (-5, 5), 5, RANDOM_SEARCH_ITERATIONS)
    rs_results_5d.append(rs_steps)

for rs_result in rs_results_5d:
    plt.plot([point[0] for point in rs_result],
             [point[1] for point in rs_result], marker='', linestyle='-')

utils.plot_template('Random search - jednotlivá spuštění dejong 1 (5D)')
print("Random search - jednotlivá spuštění dejong 1 (5D)" + describe_run(outputs=rs_results_5d))

# AVG STEPS RANDOM SEARCH 5D
rs_avg_dj1_5d = utils.average_score(rs_results_5d)
plt.plot([point[0] for point in rs_avg_dj1_5d],
         [point[1] for point in rs_avg_dj1_5d], marker='', linestyle='-')
utils.plot_template('Průměr vyhledávání RS dejong 1 (5D)')

# RANDOM SEARCH 10D
rs_results = []
for i in range(30):
    _, rs_steps = searches.random_search(functions.dejong_1st, (-5, 5), 10, RANDOM_SEARCH_ITERATIONS)
    rs_results.append(rs_steps)

for rs_result in rs_results:
    plt.plot([point[0] for point in rs_result],
             [point[1] for point in rs_result], marker='', linestyle='-')

utils.plot_template('Random search - jednotlivá spuštění dejong 1 (10D)')
print("Random search - jednotlivá spuštění dejong 1 (10D)" + describe_run(outputs=rs_results))

# AVG STEPS RANDOM SEARCH 10D
rs_avg_dj1_10d = utils.average_score(rs_results)
plt.plot([point[0] for point in rs_avg_dj1_10d],
         [point[1] for point in rs_avg_dj1_10d], marker='', linestyle='-')
utils.plot_template('Průměr vyhledávání RS dejong 1 (10D)')

# -----------
# RANDOM SEARCH 5D DEJONG 2
rs_results = []
for i in range(30):
    _, rs_steps = searches.random_search(functions.dejong_2nd, (-5, 5), 5, RANDOM_SEARCH_ITERATIONS)
    rs_results.append(rs_steps)

for rs_result in rs_results:
    plt.plot([point[0] for point in rs_result],
             [point[1] for point in rs_result], marker='', linestyle='-')

utils.plot_template('Random search - jednotlivá spuštění dejong 2 (5D)')
print("Random search - jednotlivá spuštění dejong 2 (5D)" + describe_run(outputs=rs_results))


# AVG STEPS RANDOM SEARCH 5D DEJONG 2
rs_avg_dj2_5d = utils.average_score(rs_results)
plt.plot([point[0] for point in rs_avg_dj2_5d],
         [point[1] for point in rs_avg_dj2_5d], marker='', linestyle='-')
utils.plot_template('Průměr vyhledávání RS dejong 2 (5D)')

# RANDOM SEARCH 10D DEJONG 2
rs_results = []
for i in range(30):
    _, rs_steps = searches.random_search(functions.dejong_2nd, (-5, 5), 10, RANDOM_SEARCH_ITERATIONS)
    rs_results.append(rs_steps)

for rs_result in rs_results:
    plt.plot([point[0] for point in rs_result],
             [point[1] for point in rs_result], marker='', linestyle='-')

utils.plot_template('Random search - jednotlivá spuštění dejong 2 (10D)')
print("Random search - jednotlivá spuštění dejong 2 (10D)" + describe_run(outputs=rs_results))

# AVG STEPS RANDOM SEARCH 10D DEJONG 2
rs_avg_dj2_10d = utils.average_score(rs_results)
plt.plot([point[0] for point in rs_avg_dj2_10d],
         [point[1] for point in rs_avg_dj2_10d], marker='', linestyle='-')
utils.plot_template('Průměr vyhledávání RS dejong 2 (10D)')

# ----------------

# RANDOM SEARCH 5D Schweffel
rs_results = []
for i in range(30):
    _, rs_steps = searches.random_search(functions.schweffel, (-500, 500), 5, RANDOM_SEARCH_ITERATIONS)
    rs_results.append(rs_steps)

for rs_result in rs_results:
    plt.plot([point[0] for point in rs_result],
             [point[1] for point in rs_result], marker='', linestyle='-')

utils.plot_template('Random search - jednotlivá spuštění Schweffel (5D)')
print("Random search - jednotlivá spuštění Schweffel (5D) " + describe_run(outputs=rs_results))


# AVG STEPS RANDOM SEARCH 5D Schweffel
rs_avg_sch_5d = utils.average_score(rs_results)
plt.plot([point[0] for point in rs_avg_sch_5d],
         [point[1] for point in rs_avg_sch_5d], marker='', linestyle='-')
utils.plot_template('Průměr vyhledávání RS Schweffel (5D)')

# RANDOM SEARCH 10D Schweffel
rs_results = []
for i in range(30):
    _, rs_steps = searches.random_search(functions.schweffel, (-500, 500), 10, RANDOM_SEARCH_ITERATIONS)
    rs_results.append(rs_steps)

for rs_result in rs_results:
    plt.plot([point[0] for point in rs_result],
             [point[1] for point in rs_result], marker='', linestyle='-')

utils.plot_template('Random search - jednotlivá spuštění Schweffel (10D)')
print("Random search - jednotlivá spuštění Schweffel (10D) " + describe_run(outputs=rs_results))


# AVG STEPS RANDOM SEARCH 10D Schweffel
rs_avg_sch_10d = utils.average_score(rs_results)
plt.plot([point[0] for point in rs_avg_sch_10d],
         [point[1] for point in rs_avg_sch_10d], marker='', linestyle='-')
utils.plot_template('Průměr vyhledávání RS Schweffel (10D)')


def plot_avgs(rs_avg, sa_avg, title: str):
    plt.plot([point[0] for point in rs_avg],
             [point[1] for point in rs_avg], marker='', linestyle='-', label='Random search')
    plt.plot([point[0] for point in sa_avg],
             [point[1] for point in sa_avg], marker='', linestyle='-', label='Simulated annealing')
    plt.legend()
    utils.plot_template('Průměry ' + title)

sa_avg_dej1_5d = execute_sa(functions.dejong_1st, 5, 'SA Dejong 1 5D')
plot_avgs(rs_avg_dj1_5d, sa_avg_dej1_5d, 'DJ1 5D')
sa_avg_dej1_10d = execute_sa(functions.dejong_1st, 10, 'SA Dejong 1 10D')
plot_avgs(rs_avg_dj1_10d, sa_avg_dej1_10d, 'DJ1 10D')
sa_avg_dej2_5d = execute_sa(functions.dejong_2nd, 5, 'SA Dejong 2 5D')
plot_avgs(rs_avg_dj2_5d, sa_avg_dej2_5d, 'DJ2 5D')
sa_avg_dej2_10d = execute_sa(functions.dejong_2nd, 10, 'SA Dejong 2 10D')
plot_avgs(rs_avg_dj2_10d, sa_avg_dej2_10d, 'DJ2 10D')
sa_avg_sch_5d = execute_sa(functions.schweffel, 5, 'SA Schweffel 5D')
plot_avgs(rs_avg_sch_5d, sa_avg_sch_5d, 'Schweffel 5D')
sa_avg_sch_10d = execute_sa(functions.schweffel, 10, 'SA Schweffel 10D')
plot_avgs(rs_avg_sch_10d, sa_avg_sch_10d, 'Schweffel 10D')

