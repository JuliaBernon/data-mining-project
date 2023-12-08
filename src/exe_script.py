import os
# run : python3 exe_script.py

def run_script(script, *args):
    try:
        os.system(f"python {script} {' '.join(map(str, args))}")
    except Exception as e:
        print(f"Error while running {script}: {e}")

# Generate drivers, standard routes, and actual routes
scripts = [
    ("./src/mainRulesGeneration.py",""),
    ("./src/driverGeneration.py", 100), # see number by default in each script
    ("./src/stdGeneration.py", 500),
    ("./src/actualGeneration.py", 11000, "./data/standard.json", "./data/actual21.json"),
    ("./src/merchFIAndAssoRules.py", 0.3, 0.75, "./data/actual21.json", "./data/csv/freq_items21.csv", "./data/csv/asso_rules21.csv", "./data/freq_items21.json"),
    ("./src/recStandard.py", 500, "./data/csv/freq_items21.csv", "./results/recStandard21.json"),
    #("./src/actualGeneration.py", 11000, "./results/recStandard21.json", "./data/newActual21.json")
    ("./src/rankings.py", ""),# takes a bit of time (~1min)
    ("./src/question_2.py", ""),# takes a lot of time (at least 10 secs per driver)
    ("./src/q2_test.py", ""),# takes a lot of time (at least 10 secs per driver)
]
for script_args in scripts:
    run_script(*script_args)

# actual : 1000, threshold : 0.75, recStandard : 500, newActual : 1000
# actual1 : 1000, threshold : 0.8, recStandard : 500, newActual : 1000
# actual2 : 2000, threshold : 0.8, recStandard : 500, newActual : 2000
# actual3 : 3000, threshold : 0.8, recStandard : 500, newActual : 3000
# actual4 : 10000, threshold : 0.75, recStandard : 500, newActual : 10000
# actual5 : 10000, threshold : 0.75, recStandard : 500, newActual : 10000

# actual6 : 1000, threshold : 0.75, recStandard : 500, newActual : 1000
# actual7 : 1000, threshold : 0.75, recStandard : 500, newActual : 1000
# actual8 : 1000, threshold : 0.75, recStandard : 500, newActual : 1000
# actual9 : 1000, threshold : 0.75, recStandard : 500, newActual : 1000

# actual10 : 2000, threshold : 0.8, recStandard : 500, newActual : 2000
# actual11 : 2000, threshold : 0.8, recStandard : 500, newActual : 2000
# actual12 : 2000, threshold : 0.8, recStandard : 500, newActual : 2000
# actual13 : 2000, threshold : 0.8, recStandard : 500, newActual : 2000

# actual14 : 3000, threshold : 0.8, recStandard : 500, newActual : 3000
# actual15 : 3000, threshold : 0.8, recStandard : 500, newActual : 3000
# actual16 : 3000, threshold : 0.8, recStandard : 500, newActual : 3000
# actual17 : 3000, threshold : 0.8, recStandard : 500, newActual : 3000

# actual18 : 10000, threshold : 0.75, recStandard : 500, newActual : 10000
# actual19 : 10000, threshold : 0.75, recStandard : 500, newActual : 10000
# actual20 : 10000, threshold : 0.75, recStandard : 500, newActual : 10000
# actual21 : 10000, threshold : 0.75, recStandard : 500, newActual : 10000

