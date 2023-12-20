import os
# run : python3 exe_script.py

def run_script(script, *args):
    try:
        os.system(f"python {script} {' '.join(map(str, args))}")
    except Exception as e:
        print(f"Error while running {script}: {e}")

# Generate drivers, standard routes, and actual routes

stdid = 1000
nbactual = 8000
fileid = f"{stdid}_{nbactual}"


scripts = [
    # ("./src/mainRulesGeneration.py",""),
    # ("./src/driverGeneration.py", 100), # see number by default in each script
    
    # ("./src/stdGeneration.py", 500),

    ("./src/actualGeneration.py", nbactual, f"./data/standard{stdid}.json", f"./data/actual{fileid}.json"),
    ("./src/merchFIAndAssoRules.py", 0.3, 0.8, f"./data/actual{fileid}.json", f"./data/csv/freq_items{fileid}.csv", f"./data/csv/asso_rules{fileid}.csv", f"./data/freq_items{fileid}.json"),
    ("./src/recStandard.py", stdid, f"./data/csv/freq_items{fileid}.csv", f"./results/recStandard{fileid}.json"),
    ("./src/actualGeneration.py", nbactual, f"./results/recStandard{fileid}.json", f"./data/newActual{fileid}.json")
    
    #("./src/rankings.py", ""),# takes a bit of time (~1min)
    #("./src/question_2.py", ""),# takes a lot of time (at least 10 secs per driver)
    #("./src/q2_test.py", ""),# takes a lot of time (at least 10 secs per driver)
]
for script_args in scripts:
    run_script(*script_args)


## for all the tests : threshold = 0.8, support = 0.3, max_len = 3
