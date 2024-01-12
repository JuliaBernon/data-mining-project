import os
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def parseTime(textFile):
    time = []
    with open(textFile, "r") as file:
        data = file.readlines()
        for line in data:
            time.append(line.split(":")[-1].split(" ")[1])
    return time

nbactuals100 = ['100', '200', '300', '400', '500', 
                '1000','2000', '4000', '8000',
                '10000', '15000', '20000',
                '25000', '50000', '75000',
                '100000']

nbactuals500 = ['500', 
                '1000','2000', '4000', '8000',
                '10000', '15000', '20000',
                '25000', '50000', '75000',
                '100000']

nbactuals1000 = ['1000','2000', '4000', '8000',
                '10000', '15000', '20000',
                '25000', '50000', '75000',
                '100000']

times100 = parseTime("./results/tests/distances/apriori/exectime100.txt")
times500 = parseTime("./results/tests/distances/apriori/exectime500.txt")
times1000 = parseTime("./results/tests/distances/apriori/exectime1000.txt")

times100 = [float(time) for time in times100]
times500 = [float(time) for time in times500]
times1000 = [float(time) for time in times1000]

def plot_exec_time(nbactuals, times, label, color):
    plt.scatter(nbactuals, times, label=label, color=color)
    plt.plot(nbactuals, times, color=color, linewidth=0.8)

def regression_analysis(x_values, y_values):
    slope, intercept, r_value, p_value, std_err = linregress(x_values, y_values)
    return slope, intercept, r_value

# perform regression analysis
slope100, intercept100, r_value100 = regression_analysis([float(nbactual) for nbactual in nbactuals100], times100)  
slope500, intercept500, r_value500 = regression_analysis([float(nbactual) for nbactual in nbactuals500], times500)
slope1000, intercept1000, r_value1000 = regression_analysis([float(nbactual) for nbactual in nbactuals1000], times1000)

# plot the evolution of execution times with the number of actual routes
plt
plot_exec_time(nbactuals100, times100, label="with 100 standard routes", color="orange")
plt.plot(nbactuals100, np.polyval([slope100, intercept100], list(map(int, nbactuals100))), color="red", linewidth=0.8)

plot_exec_time(nbactuals500, times500, label="with 500 standard routes", color="green")
plt.plot(nbactuals500, np.polyval([slope500, intercept500], list(map(int, nbactuals500))), color="darkgreen", linewidth=0.8)

plot_exec_time(nbactuals1000, times1000, label="with 1000 standard routes", color="blue")
plt.plot(nbactuals1000, np.polyval([slope1000, intercept1000], list(map(int, nbactuals1000))), color="cyan", linewidth=0.8)

equation100 = f'Regression (100 routes): y = {slope100:.4f}x + {intercept100:.4f}, r = {r_value100:.4f}'
equation500 = f'Regression (500 routes): y = {slope500:.4f}x + {intercept500:.4f}, r = {r_value500:.4f}'
equation1000 = f'Regression (1000 routes): y = {slope1000:.4f}x + {intercept1000:.4f}, r = {r_value1000:.4f}'


# display the regression equations
plt.annotate(equation100, (0.5, 100), fontsize=10, color="red")
plt.annotate(equation500, (0.5, 95), fontsize=10, color="darkgreen")
plt.annotate(equation1000, (0.5, 90), fontsize=10, color="blue")

# display the correlation coefficient


plt.title("Execution time according to the number of actual routes (apriori algorithm)")
plt.xlabel("Number of actual routes")
plt.ylabel("Execution time (s)")
plt.legend()
plt.show()
