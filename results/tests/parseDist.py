## parse data in txt files to get the mean, std, min, max

def parseStdLength(textFile):
    with open(textFile, "r") as file:
        data = file.readlines()
        std_length = data[1][1]
    return std_length

def parseActualLength(textFile):
    with open(textFile, "r") as file:
        data = file.readlines()
        actual_length = data[1].split(",")[1].split("actual")[0]
    return actual_length

def parseMean(textFile):
    with open(textFile, "r") as file:
        data = file.readlines()
        mean = data[3].split(":")[-1]
    return mean

def parseMeanBis(textFile):
    with open(textFile, "r") as file:
        data = file.readlines()
        mean_bis = data[4].split(":")[-1]
    return mean_bis

def parseStd(textFile):
    with open(textFile, "r") as file:
        data = file.readlines()
        std = data[6].split(":")[-1]
    return std

def parseStdBis(textFile):
    with open(textFile, "r") as file:
        data = file.readlines()
        std_bis = data[7].split(":")[-1]
    return std_bis

def parseMin(textFile):
    with open(textFile, "r") as file:
        data = file.readlines()
        min_dist = data[9].split(":")[-1]
    return min_dist

def parseMinBis(textFile):
    with open(textFile, "r") as file:
        data = file.readlines()
        min_dist_bis = data[10].split(":")[-1]
    return min_dist_bis

def parseMax(textFile):
    with open(textFile, "r") as file:
        data = file.readlines()
        max_dist = data[12].split(":")[-1]
    return max_dist

def parseMaxBis(textFile):
    with open(textFile, "r") as file:
        data = file.readlines()
        max_dist_bis = data[13].split(":")[-1]
    return max_dist_bis

def parseTime(textFile):
    with open(textFile, "r") as file:
        data = file.readlines()
        time = data[15].split(":")[-1].split(" ")[1]
    return time

