class Statistics:
    def __init__(self, min, max, mean, median, std):
        self.min = min
        self.max = max
        self.mean = mean
        self.median = median
        self.std = std

    def __str__(self):
        return ("Statistics(min={}, max={}, mean={}, median={}, std={})"
                .format(self.min, self.max, self.mean, self.median, self.std))
