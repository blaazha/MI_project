import functions
import searches
import utils
import matplotlib.pyplot as plt

RANDOM_SEARCH_ITERATIONS = 1000

# RANDOM SEARCH 5D
rs_results = []
for i in range(30):
    _, rs_steps = searches.random_search(functions.dejong_1st, (-5, 5), 5, RANDOM_SEARCH_ITERATIONS)
    rs_results.append(rs_steps)

for rs_result in rs_results:
    plt.plot([point[0] for point in rs_result],
             [point[1] for point in rs_result], marker='', linestyle='-')

utils.plot_template('Random search - jednotlivá spuštění dejong 1 (5D)')

# AVG STEPS RANDOM SEARCH 5D
rs_avg_steps = utils.average_score(rs_results)
plt.plot([point[0] for point in rs_avg_steps],
         [point[1] for point in rs_avg_steps], marker='', linestyle='-')
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

# AVG STEPS RANDOM SEARCH 10D
rs_avg_steps = utils.average_score(rs_results)
plt.plot([point[0] for point in rs_avg_steps],
         [point[1] for point in rs_avg_steps], marker='', linestyle='-')
utils.plot_template('Průměr vyhledávání RS dejong 1 (10D)')

# -----------
