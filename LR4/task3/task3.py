import statistics
import math
import matplotlib.pyplot as plt
import numpy as np


class XValuesClass:
    def __init__(self):
        self.x_vals = np.arange(-1, 1, 0.05)


class Series(XValuesClass):
    def __init__(self):
        super().__init__()
        self.eps = 1e-1

    def calculate_series(self):
        y_vals = []
        result = 0.0
        i = 1
        for x in self.x_vals:
            while i <= 500:
                term = (-1) * (x ** i / i)
                if abs(term) < self.eps:
                    break
                result += term
                i += 1
            i = 1
            y_vals.append(result)
            result = 0.0
        return y_vals

    def calculate_math_series(self):
        y_vals = []
        for x in self.x_vals:
            y_vals.append(math.log(1-x, math.e))
        return y_vals


class SeriesPlot(XValuesClass):
    def __init__(self, y_values: list, y_math_values):
        super().__init__()
        self.y_vals = y_values
        self.y_math_vals = y_math_values

    def build_plots(self):
        plt.plot(self.x_vals, self.y_vals, label='My series')
        plt.plot(self.x_vals, self.y_math_vals, label='Math series')
        plt.legend()
        plt.savefig('task3/functions.png')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Series plot')
        plt.grid(True)
        plt.show()


def run_task():
    a = Series()
    y = a.calculate_series()
    print(f"Mean: {statistics.mean(y)}\n"
          f"Median: {statistics.median(y)}\n"
          f"Dispersion: {statistics.variance(y)}\n"
          f"MSE: {statistics.stdev(y)}\n"
          f"Mode: {statistics.mode(y)}")

    y_math = a.calculate_math_series()

    plot = SeriesPlot(y, y_math)
    plot.build_plots()
