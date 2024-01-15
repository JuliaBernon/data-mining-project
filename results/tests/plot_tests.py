import os
import matplotlib.pyplot as plt

def get_data_folder(folder_adress):
    list_file = os.listdir(folder_adress)
    data = {}
    for file in list_file:
        with open(folder_adress+"/"+file, "r") as fichier:
            lines = fichier.readlines()
            temp = []
            for line in lines:
                temp.append(line[:-1])
            lines = temp
            if lines[6] not in data.keys():
                data[lines[6]] = []
            data[lines[6]].append({"actuals":lines[8],"result":lines[14],"time":lines[16]})
    for key in data.keys():
        data[key].sort(key = lambda tup : float(tup["actuals"]))
    
    return(data)          

def plot_q2():
    folder_adress = "results/tests/q2"
    name = "q2"
    data = get_data_folder(folder_adress)
    all = {}
    for key in data.keys():
        print(key)
        actuals = []
        results = []
        times = []
        for i in data[key]:
            actuals.append(float(i["actuals"]))
            results.append(float(i["result"])*100/float(key))
            times.append(float(i["time"]))
        all[key] = [actuals,results,times]
    #plot the times 
    fig, ax = plt.subplots()
    ax.plot(all["100"][0],all["100"][2])
    ax.scatter(all["100"][0],all["100"][2],label = "100 standard routes")
    ax.plot(all["500"][0],all["500"][2])
    ax.scatter(all["500"][0],all["500"][2],label = "500 standard routes")
    ax.plot(all["1000"][0],all["1000"][2])
    ax.scatter(all["1000"][0],all["1000"][2],label = "1000 standard routes")
    ax.set_xlabel("Number of actual routes")
    ax.set_ylabel("Execution time (s)")
    plt.legend()
    plt.savefig(f"results/tests/graphs/time_per_standard_{name}.png")
    #plot the results
    fig, ax = plt.subplots()
    ax.plot(all["100"][0],all["100"][1])
    ax.scatter(all["100"][0],all["100"][1],label = "100 standard routes")
    ax.plot(all["500"][0],all["500"][1])
    ax.scatter(all["500"][0],all["500"][1],label = "500 standard routes")
    ax.plot(all["1000"][0],all["1000"][1])
    ax.scatter(all["1000"][0],all["1000"][1],label = "1000 standard routes")
    ax.set_xlabel("Number of actual routes")
    ax.set_ylabel("Error (%)")
    plt.legend()
    plt.savefig(f"results/tests/graphs/results_per_standard_{name}.png")

def plot_q3():
    folder_adress = "results/tests/q3"
    name = "q3"
    data = get_data_folder(folder_adress)
    all = {}
    for key in data.keys():
        print(key)
        actuals = []
        results = []
        times = []
        for i in data[key]:
            actuals.append(float(i["actuals"]))
            results.append(float(i["result"])*100)
            times.append(float(i["time"]))
        all[key] = [actuals,results,times]
    #plot the times 
    fig, ax = plt.subplots()
    ax.plot(all["100"][0],all["100"][2])
    ax.scatter(all["100"][0],all["100"][2],label = "100 standard routes")
    ax.plot(all["500"][0],all["500"][2])
    ax.scatter(all["500"][0],all["500"][2],label = "500 standard routes")
    ax.plot(all["1000"][0],all["1000"][2])
    ax.scatter(all["1000"][0],all["1000"][2],label = "1000 standard routes")
    ax.set_xlabel("Number of actual routes")
    ax.set_ylabel("Execution time (s)")
    plt.legend()
    plt.savefig(f"results/tests/graphs/time_per_standard_{name}.png")
    #plot the results
    fig, ax = plt.subplots()
    ax.plot(all["100"][0],all["100"][1])
    ax.scatter(all["100"][0],all["100"][1],label = "100 standard routes")
    ax.plot(all["500"][0],all["500"][1])
    ax.scatter(all["500"][0],all["500"][1],label = "500 standard routes")
    ax.plot(all["1000"][0],all["1000"][1])
    ax.scatter(all["1000"][0],all["1000"][1],label = "1000 standard routes")
    ax.set_xlabel("Number of actual routes")
    ax.set_ylabel("Reduction of deviation (%)")
    plt.legend()
    plt.savefig(f"results/tests/graphs/results_per_standard_{name}.png")

plot_q2()
plot_q3()