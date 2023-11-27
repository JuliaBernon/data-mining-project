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
    ("./src/actualGeneration.py", 1000, "./data/standard.json", "./data/actual.json"),
    # ("./src/merchFIAndAssoRules.py", ""), fichier à modifier en faveur du script
    ("./src/recStandard.py", 500),
    ("./src/actualGeneration.py", 1000, "./results/recStandard.json", "./data/newActual.json")
]
for script_args in scripts:
    run_script(*script_args)

