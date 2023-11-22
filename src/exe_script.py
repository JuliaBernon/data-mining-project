import os
# run : python3 exe_script.py

def run_script(script,arg):
    try:
        os.system(f"python {script} {arg}")
    except Exception as e:
        print(f"Error while running {script}: {e}")

# Generate drivers, standard routes, and actual routes
scripts = [
    ("./src/driverGeneration.py", 100),
    ("./src/stdGeneration.py", 1000),
    ("./src/actualGeneration.py", 5000)
]

for script, arg in scripts:
    run_script(script,arg)
