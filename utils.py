import matplotlib.pyplot as plt


def average_score(steps):
    num_of_steps = len(steps[0])
    avg_steps = []
    for i in range(num_of_steps):
        step_avg = 0.0
        for j in range(len(steps)):
            step_avg += steps[j][i][1]
        avg_steps.append((i, step_avg / len(steps)))
    return avg_steps


def plot_template(title: str):
    plt.xlabel('Iterace')
    plt.ylabel('Hodnota funkce')
    plt.title(title)
    plt.grid(True)
    plt.show()
