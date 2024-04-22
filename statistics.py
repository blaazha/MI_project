from entities import Statistics
import numpy as np


def describe_run(outputs):
    final_results = __get_final_results(outputs)
    return str(Statistics(min=min(final_results), max=max(final_results),
                       median=np.median(final_results),
                       std=np.std(final_results), mean=np.mean(final_results)))


def __get_final_results(outputs):
    final_scores = []
    for output in outputs:
        best_score = float('inf')
        for run in output:
            if run[1] < best_score:
                best_score = run[1]
        final_scores.append(best_score)
    return final_scores
    #return [row[-1][1] for row in outputs]