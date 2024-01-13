import os
# run : python3 exe_script.py

def run_script(script, *args):
    try:
        os.system(f"python {script} {' '.join(map(str, args))}")
    except Exception as e:
        print(f"Error while running {script}: {e}")

# Generate drivers, standard routes, and actual routes

stdid = 500
nbactual = 5000
fileid = f"{stdid}_{nbactual}"
fileid = ""


scripts = [
    ("./src/mainRulesGeneration.py",""),
    ("./src/driverGeneration.py", 100), # see number by default in each script
    ("./src/stdGeneration.py", stdid),
    ("./src/actualGeneration.py", nbactual, f"./data/standard{stdid}.json", f"./data/actual{fileid}.json"),
    ("./src/merchFIAndAssoRules.py", 0.3, 0.8, f"./data/actual{fileid}.json", f"./data/csv/freq_items{fileid}.csv", f"./data/csv/asso_rules{fileid}.csv", f"./data/freq_items{fileid}.json"),
]
for script_args in scripts:
    run_script(*script_args)


## for all the tests : threshold = 0.8, support = 0.3, max_len = 3
