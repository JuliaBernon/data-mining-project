# Data Mining project - DM23_Bernon_Marcandella

Authors : Julia Bernon - Ulysse Marcandella

Team name : TNCY

## Description
Subject : 
**On identifying the compensation for vaguely followed trips**

This project falls within the *Data Mining Course, University of Trento*, 2023-2024

Instructor : Prof. Yannis Valagrakis


## How2 - Step1 : Clone the project from GitHub
*See Step3 for Google Drive instructions*

**Clone the project**

```sh
# with SSH
git clone git@github.com:JuliaBernon/data-mining-project.git

# or with HTTPS
git clone https://github.com/JuliaBernon/data-mining-project.git
```

**Open the directory**

```bash
cd data-mining-project
```

## How2 - Step2 : Set up a virtual environment
```bash
# create a virtual environment
python3 -m venv env

# activate the environment
source env/bin/activate

# installing requirements in the environment
(env) pip install -r requirements.txt

# deactivate the environment
(env) deactivate
```

**Commands for PowerShell**

```powershell
# open the directory
PS C:\> cd .\data-mining-project

# create a virtual environment
PS C:\> python3 -m venv env

# activate the environment by running activation script
PS C:\> .\env\Scripts\activate
```

In case you encounter issues when running the activation script, you must change the privacy of your system.

For that, execute PowerShell in admin mode, and run the following command : 

```powershell
PS C:\> Set-ExecutionPolicy AllSigned
```

Once it is done, launch a new PowerShell window. The activation script must be now executable

```bash
PS C:\> .\env\Scripts\activate
(env) PS C:\> # you are now in the (env) environment
```


## How2 - Project recovery on Google Drive


## How2 - Prepare the synthetic datasets

**Step 1 - Install the requirements**
```sh
pip install -r requirements.txt
```

**Step2 - Generate the data**

All the following mentionned JSON files should appear into *data* directory

```sh
# on Linux or WSL
python3 ./src/mainRulesGeneration.py
# establish the main rules that will affect drivers' agenda

python3 ./src/driverGeneration.py <nb_drivers>
# create <nb_drivers> drivers (if none, create 10)

python3 ./src/stdGeneration.py <nb_std_routes>
# create <nb_std_routes> standard routes into  (if none, create 500)
# save file into standard<nb_std_routes>.json file

python3 ./src/actualGeneration.py <nb_act_routes> <std_routes_file> <actual_file_to_save>  
# create <nb_act_routes> actual routes (if none, create 1000) based on <std_routes_file> file
# save data into <actual_file_to_save> file
# warning : all arguments must be filled !

# on PowerShell
```
If you want to specify the number of each, add the number as argument
```bash
python3 ./src/<filename>Generation.py <number>
```

**By default**
```sh
python3 ./src/exe_script.py
```

This command will execute driverGeneration.py, stdGeneration.py, actualGeneration.py, and will create 100 drivers, 1000 standard routes, and 5000 actual routes, by default.


# Step 1 : Recommanded standard routes

**Identifying frequent itemsets and association rules**

```sh
python3 ./src/merchFIAndAssoRules.py <support> <threshold> <actual_routes_file> <FI_to_save_csv> <assoRules_to_save_csv> <FI_to_save_json>
```
Based on the <actual_routes_file> provided, extract the frequent itemsets and association rules with 'support' support and 'threshold' threshold.
It will save the frequent itemsets and association rules into *./data/csv/* directory in CSV files. A JSON file with the found frequent itemsets will also be created in *./data/* directory.

**Recommanding standard routes**
```sh
python3 ./src/recStandard.py <nb_recStd_routes> <FI_file_csv> <recStandard_file_to_save>
```


# Step 2 : List of 5 standard routes for each driver to minimize diversions

# Step 3 : Best standard route for each driver

