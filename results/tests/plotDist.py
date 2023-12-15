from parseDist import *
import matplotlib.pyplot as plt
import numpy as np
import os

# Read and parse distances
means = []
means_bis = []
stds = []
stds_bis = []
min_dists = []
min_dists_bis = []
max_dists = []
max_dists_bis = []
execution_times = []

acts = []

acts100 = []
acts500 = []
means500 = []
means_bis500 = []
means100 = []
means_bis100 = []
stds100 = []
stds_bis100 = []
stds500 = []
stds_bis500 = []

# for all .txt files in results/tests/distances, parse mean data
for file in os.listdir("./results/tests/distances/std1000"):
    if file.endswith(".txt"):
        acts.append(parseActualLength("./results/tests/distances/std1000/" + file))
        means.append(parseMean("./results/tests/distances/std1000/" + file))
        means_bis.append(parseMeanBis("./results/tests/distances/std1000/" + file))
        stds.append(parseStd("./results/tests/distances/std1000/" + file))
        stds_bis.append(parseStdBis("./results/tests/distances/std1000/" + file))
        min_dists.append(parseMin("./results/tests/distances/std1000/" + file))
        min_dists_bis.append(parseMinBis("./results/tests/distances/std1000/" + file))
        max_dists.append(parseMax("./results/tests/distances/std1000/" + file))
        max_dists_bis.append(parseMaxBis("./results/tests/distances/std1000/" + file))
        execution_times.append(parseTime("./results/tests/distances/std1000/" + file))

for file in os.listdir("./results/tests/distances/std100bis"):
    if file.endswith(".txt"):
        means100.append(parseMean("./results/tests/distances/std100bis/" + file))
        means_bis100.append(parseMeanBis("./results/tests/distances/std100bis/" + file))
        acts100.append(parseActualLength("./results/tests/distances/std100bis/" + file))
        stds100.append(parseStd("./results/tests/distances/std100bis/" + file))
        stds_bis100.append(parseStdBis("./results/tests/distances/std100bis/" + file))

for file in os.listdir("./results/tests/distances/std500bis"):
    if file.endswith(".txt"):
        means500.append(parseMean("./results/tests/distances/std500bis/" + file))
        means_bis500.append(parseMeanBis("./results/tests/distances/std500bis/" + file))
        acts500.append(parseActualLength("./results/tests/distances/std500bis/" + file))
        stds500.append(parseStd("./results/tests/distances/std500bis/" + file))
        stds_bis500.append(parseStdBis("./results/tests/distances/std500bis/" + file))

# convert lists of strings to lists of floats
stds = [float(std) for std in stds]
acts = sorted([float(act) for act in acts])
means = [float(mean) for mean in means]
means_bis = [float(mean_bis) for mean_bis in means_bis]
stds = [float(std) for std in stds]
stds_bis = [float(std_bis) for std_bis in stds_bis]
min_dists = [float(min_dist) for min_dist in min_dists]
min_dists_bis = [float(min_dist_bis) for min_dist_bis in min_dists_bis]
max_dists = [float(max_dist) for max_dist in max_dists]
max_dists_bis = [float(max_dist_bis) for max_dist_bis in max_dists_bis]
execution_times = [float(time) for time in execution_times]

means100 = [float(mean) for mean in means100]
means_bis100 = [float(mean_bis) for mean_bis in means_bis100]
means500 = [float(mean) for mean in means500]
means_bis500 = [float(mean_bis) for mean_bis in means_bis500]
acts100 = sorted([float(act) for act in acts100])
acts500 = sorted([float(act) for act in acts500])
stds100 = [float(std) for std in stds100]
stds_bis100 = [float(std_bis) for std_bis in stds_bis100]
stds500 = [float(std) for std in stds500]
stds_bis500 = [float(std_bis) for std_bis in stds_bis500]


# plot on the same graph the mean distances between actual routes and standard routes and the mean distances between new actual routes and new standard routes
fig, axs = plt.subplots(2, 1, figsize=(8, 10))

# Plot for 100 standard routes
axs[0].scatter(acts100, means100, label="mean std/act 100", color="orange")
axs[0].plot(acts100, means100, color="orange", linewidth=0.8)
axs[0].scatter(acts100, means_bis100, label="mean newstd/newact 100", color="red")
axs[0].plot(acts100, means_bis100, color="red", linewidth=0.8)

# Plot for 500 standard routes
axs[0].scatter(acts500, means500, label="mean std/act 500", color="green")
axs[0].plot(acts500, means500, color="green", linewidth=0.8)
axs[0].scatter(acts500, means_bis500, label="mean newstd/newact 500", color="darkgreen")
axs[0].plot(acts500, means_bis500, color="green", linewidth=0.8)

# Plot for 1000 standard routes
axs[0].scatter(acts, means, label="mean std/act 1000", color="blue")
axs[0].plot(acts, means, color="blue", linewidth=0.8)
axs[0].scatter(acts, means_bis, label="mean newstd/newact 1000", color="cyan")
axs[0].plot(acts, means_bis, color="cyan", linewidth=0.8)

axs[0].set_title("Mean distances between actual routes and standard routes and between new actual routes and new standard routes")
axs[0].legend()

# Plot for 100 standard routes
axs[1].scatter(acts100, stds100, label="std std/act 100", color="orange")
axs[1].plot(acts100, stds100, color="orange", linewidth=0.8)
axs[1].scatter(acts100, stds_bis100, label="std newstd/newact 100", color="red")
axs[1].plot(acts100, stds_bis100, color="red", linewidth=0.8)

# Plot for 500 standard routes
axs[1].scatter(acts500, stds500, label="std std/act 500", color="green")
axs[1].plot(acts500, stds500, color="green", linewidth=0.8)
axs[1].scatter(acts500, stds_bis500, label="std newstd/newact 500", color="darkgreen")
axs[1].plot(acts500, stds_bis500, color="green", linewidth=0.8)

# Plot for 1000 standard routes
axs[1].scatter(acts, stds, label="std std/act 1000", color="blue")
axs[1].plot(acts, stds, color="blue", linewidth=0.8)
axs[1].scatter(acts, stds_bis, label="std newstd/newact 1000", color="cyan")
axs[1].plot(acts, stds_bis, color="cyan", linewidth=0.8)

axs[1].set_title("Standard deviations of distances between actual routes and standard routes and between new actual routes and new standard routes")
axs[1].legend()

plt.tight_layout()
plt.show()

