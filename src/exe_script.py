import os
# run : python3 exe_script.py

def run_script(script,arg):
    try:
        os.system(f"python {script} {arg}")
    except Exception as e:
        print(f"Error while running {script}: {e}")

# Generate drivers, standard routes, and actual routes
scripts = [
    ("./src/driverGeneration.py", 100), # see number by default in each script
    ("./src/stdGeneration.py", 500),
    ("./src/actualGeneration.py", 1000),
    ("./src/recStandard.py", 500),
]

for script, arg in scripts:
    run_script(script,arg)
