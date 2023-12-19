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

    ("./src/actualGeneration.py", 10000, "./data/standard.json", "./data/actual.json"),
    #("./src/merchFIAndAssoRules.py", 0.3, 0.8, "./data/actual.json", "./data/csv/freq_items.csv", "./data/csv/asso_rules.csv", "./data/freq_items.json"),
    #("./src/recStandard.py", 500, "./data/csv/freq_items.csv", "./results/recStandard.json"),
    #("./src/actualGeneration.py", 1000, "./results/recStandard.json", "./data/newActual.json")
    
    #("./src/rankings.py", ""),# takes a bit of time (~1min)
    #("./src/question_2.py", ""),# takes a lot of time (at least 10 secs per driver)
    #("./src/q2_test.py", ""),# takes a lot of time (at least 10 secs per driver)
]
for script_args in scripts:
    run_script(*script_args)


## for all the tests : threshold = 0.8, support = 0.3, max_len = 3
