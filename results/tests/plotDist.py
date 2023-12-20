from parseDist import *
import matplotlib.pyplot as plt
import numpy as np
import os

# for all .txt files in results/tests/distances, parse mean data

def parseFile(apfp, directory):
    acts, means, means_bis, stds, stds_bis, min_dists, min_dists_bis, max_dists, max_dists_bis = [], [], [], [], [], [], [], [], []
    for file in os.listdir(f"{apfp}/{directory}"):
        if file.endswith(".txt"):
            acts.append(parseActualLength(f"{apfp}/{directory}/" + file))

            means.append(parseMean(f"{apfp}/{directory}/" + file))
            means_bis.append(parseMeanBis(f"{apfp}/{directory}/" + file))

            stds.append(parseStd(f"{apfp}/{directory}/" + file))
            stds_bis.append(parseStdBis(f"{apfp}/{directory}/" + file))
            
            min_dists.append(parseMin(f"{apfp}/{directory}/" + file))
            min_dists_bis.append(parseMinBis(f"{apfp}/{directory}/" + file))
            
            max_dists.append(parseMax(f"{apfp}/{directory}/" + file))
            max_dists_bis.append(parseMaxBis(f"{apfp}/{directory}/" + file))
    return sorted(acts), sorted(means), sorted(means_bis), sorted(stds), sorted(stds_bis), sorted(min_dists), sorted(min_dists_bis), sorted(max_dists), sorted(max_dists_bis)


ap = "./results/tests/distances/apriori"
fp = "./results/tests/distances/fpgrowth"
directory1000 = "std1000"
directory500 = "std500"
directory100 = "std100"
# Read and parse distances

## apriori algorithm
acts100, means100, means_bis100, stds100, stds_bis100, min_dists100, min_dists_bis100, max_dists100, max_dists_bis100 = parseFile(ap, directory100)
acts500, means500, means_bis500, stds500, stds_bis500, min_dists500, min_dists_bis500, max_dists500, max_dists_bis500 = parseFile(ap, directory500)
acts1000, means1000, means_bis1000, stds1000, stds_bis1000, min_dists1000, min_dists_bis1000, max_dists1000, max_dists_bis1000 = parseFile(ap, directory1000)

# ## fpgrowth algorithm 
# acts100, means100, means_bis100, stds100, stds_bis100, min_dists100, min_dists_bis100, max_dists100, max_dists_bis100 = parseFile(fp, directory100)
# acts500, means500, means_bis500, stds500, stds_bis500, min_dists500, min_dists_bis500, max_dists500, max_dists_bis500 = parseFile(fp, directory500)
# acts1000, means1000, means_bis1000, stds1000, stds_bis1000, min_dists1000, min_dists_bis1000, max_dists1000, max_dists_bis1000 = parseFile(fp, directory1000)

# # plot on the same graph the mean distances between actual routes and standard routes and the mean distances between new actual routes and new standard routes
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
axs[0].scatter(acts1000, means1000, label="mean std/act 1000", color="blue")
axs[0].plot(acts1000, means1000, color="blue", linewidth=0.8)
axs[0].scatter(acts1000, means_bis1000, label="mean newstd/newact 1000", color="cyan")
axs[0].plot(acts1000, means_bis1000, color="cyan", linewidth=0.8)

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
axs[1].scatter(acts1000, stds1000, label="std std/act 1000", color="blue")
axs[1].plot(acts1000, stds1000, color="blue", linewidth=0.8)
axs[1].scatter(acts1000, stds_bis1000, label="std newstd/newact 1000", color="cyan")
axs[1].plot(acts1000, stds_bis1000, color="cyan", linewidth=0.8)

axs[1].set_title("Standard deviations of distances between actual routes and standard routes and between new actual routes and new standard routes")
axs[1].legend()

plt.tight_layout()
plt.show()

