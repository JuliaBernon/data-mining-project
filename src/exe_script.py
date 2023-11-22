import os

def run_script(script):
    try:
        os.system(f"python {script}")
    except Exception as e:
        print(f"Error while running {script}: {e}")

# Generate drivers, standard routes, and actual routes
scripts = ["./src/driverGeneration.py", "./src/stdGeneration.py", "./src/actualGeneration.py"]
for script in scripts:
    run_script(script)

