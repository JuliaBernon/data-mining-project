from parseDist import *
import matplotlib.pyplot as plt
import os 

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
    return acts, means, means_bis, stds, stds_bis, min_dists, min_dists_bis, max_dists, max_dists_bis


ap = "./results/tests/distances/apriori"
fp = "./results/tests/distances/fpgrowth"
directory1000 = "std1000"
directory500 = "std500"
directory100 = "std100"

## apriori algorithm
acts100, means100, means_bis100, stds100, stds_bis100, min_dists100, min_dists_bis100, max_dists100, max_dists_bis100 = parseFile(ap, directory100)
acts500, means500, means_bis500, stds500, stds_bis500, min_dists500, min_dists_bis500, max_dists500, max_dists_bis500 = parseFile(ap, directory500)
acts1000, means1000, means_bis1000, stds1000, stds_bis1000, min_dists1000, min_dists_bis1000, max_dists1000, max_dists_bis1000 = parseFile(ap, directory1000)

## fpgrowth algorithm 
# acts100, means100, means_bis100, stds100, stds_bis100, min_dists100, min_dists_bis100, max_dists100, max_dists_bis100 = parseFile(fp, directory100)
# acts500, means500, means_bis500, stds500, stds_bis500, min_dists500, min_dists_bis500, max_dists500, max_dists_bis500 = parseFile(fp, directory500)
# acts1000, means1000, means_bis1000, stds1000, stds_bis1000, min_dists1000, min_dists_bis1000, max_dists1000, max_dists_bis1000 = parseFile(fp, directory1000)

acts100_fp, means100_fp, means_bis100_fp, stds100_fp, stds_bis100_fp, min_dists100_fp, min_dists_bis100_fp, max_dists100_fp, max_dists_bis100_fp = parseFile(fp, directory100)
acts500_fp, means500_fp, means_bis500_fp, stds500_fp, stds_bis500_fp, min_dists500_fp, min_dists_bis500_fp, max_dists500_fp, max_dists_bis500_fp = parseFile(fp, directory500)
acts1000_fp, means1000_fp, means_bis1000_fp, stds1000_fp, stds_bis1000_fp, min_dists1000_fp, min_dists_bis1000_fp, max_dists1000_fp, max_dists_bis1000_fp = parseFile(fp, directory1000)


means100 = [float(mean) for mean in means100]
means_bis100 = [float(mean_bis) for mean_bis in means_bis100]
stds100 = [float(std) for std in stds100]
stds_bis100 = [float(std_bis) for std_bis in stds_bis100]

means500 = [float(mean) for mean in means500]
means_bis500 = [float(mean_bis) for mean_bis in means_bis500]
stds500 = [float(std) for std in stds500]
stds_bis500 = [float(std_bis) for std_bis in stds_bis500]

means1000 = [float(mean) for mean in means1000]
means_bis1000 = [float(mean_bis) for mean_bis in means_bis1000]
stds1000 = [float(std) for std in stds1000]
stds_bis1000 = [float(std_bis) for std_bis in stds_bis1000]

acts100 = sorted([float(act) for act in acts100])
acts500 = sorted([float(act) for act in acts500])
acts1000 = sorted([float(act) for act in acts1000])

means100_fp = [float(mean) for mean in means100_fp]
means_bis100_fp = [float(mean_bis) for mean_bis in means_bis100_fp]
stds100_fp = [float(std) for std in stds100_fp]
stds_bis100_fp = [float(std_bis) for std_bis in stds_bis100_fp]

means500_fp = [float(mean) for mean in means500_fp]
means_bis500_fp = [float(mean_bis) for mean_bis in means_bis500_fp]
stds500_fp = [float(std) for std in stds500_fp]
stds_bis500_fp = [float(std_bis) for std_bis in stds_bis500_fp]

means1000_fp = [float(mean) for mean in means1000_fp]
means_bis1000_fp = [float(mean_bis) for mean_bis in means_bis1000_fp]
stds1000_fp = [float(std) for std in stds1000_fp]
stds_bis1000_fp = [float(std_bis) for std_bis in stds_bis1000_fp]

acts100_fp = sorted([float(act) for act in acts100_fp])
acts500_fp = sorted([float(act) for act in acts500_fp])
acts1000_fp = sorted([float(act) for act in acts1000_fp])


plt.scatter(acts100, means100, label="apriori - mean std/act 100", color="orange")
plt.plot(acts100, means100, color="orange", linewidth=0.8)
plt.scatter(acts100, means_bis100, label="apriori - mean newstd/newact 100", color="red")
plt.plot(acts100, means_bis100, color="red", linewidth=0.8)

plt.scatter(acts500, means500, label="apriori - mean std/act 500", color="orange")
plt.plot(acts500, means500, color="orange", linewidth=0.8)
plt.scatter(acts500, means_bis500, label="apriori - mean newstd/newact 500", color="red")
plt.plot(acts500, means_bis500, color="red", linewidth=0.8)

plt.scatter(acts1000, means1000, label="apriori - mean std/act 1000", color="orange")
plt.plot(acts1000, means1000, color="orange", linewidth=0.8)
plt.scatter(acts1000, means_bis1000, label="apriori - mean newstd/newact 1000", color="red")
plt.plot(acts1000, means_bis1000, color="red", linewidth=0.8)

plt.scatter(acts100_fp, means100_fp, label="fpgrowth - mean std/act 100", color="blue")
plt.plot(acts100_fp, means100_fp, color="blue", linewidth=0.8)
plt.scatter(acts100_fp, means_bis100_fp, label="fpgrowth - mean newstd/newact 100", color="green")
plt.plot(acts100_fp, means_bis100_fp, color="green", linewidth=0.8)

plt.scatter(acts500_fp, means500_fp, label="fpgrowth - mean std/act 500", color="blue")
plt.plot(acts500_fp, means500_fp, color="blue", linewidth=0.8)
plt.scatter(acts500_fp, means_bis500_fp, label="fpgrowth - mean newstd/newact 500", color="green")
plt.plot(acts500_fp, means_bis500_fp, color="green", linewidth=0.8)

plt.scatter(acts1000_fp, means1000_fp, label="fpgrowth - mean std/act 1000", color="blue")
plt.plot(acts1000_fp, means1000_fp, color="blue", linewidth=0.8)
plt.scatter(acts1000_fp, means_bis1000_fp, label="fpgrowth - mean newstd/newact 1000", color="green")
plt.plot(acts1000_fp, means_bis1000_fp, color="green", linewidth=0.8)

plt.title("Mean distances between actual routes and standard routes and between new actual routes and new standard routes")
plt.xlabel("Number of actual routes")
plt.ylabel("Mean Distance")
plt.legend()
plt.show()

