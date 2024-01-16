# Data Mining project - DM23_Bernon_Marcandella

Authors : Julia Bernon - Ulysse Marcandella

Team name : TNCY

## Description
Subject : 
**On identifying the compensation for vaguely followed trips**

This project falls within the *Data Mining Course, University of Trento*, 2023-2024

Instructor : Prof. Yannis Velegrakis


## How2 - Clone the project from GitHub

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get autoremove
```

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
code .
```

## How2 - Set up a virtual environment
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

If not already installed, run the following command before creating a virtual environment : 

```bash
sudo apt install python3.8-venv
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

## Project structure 
```sh
data-mining-project
├───data                # data files
│   ├───apriori         # actualX_Y.json, using apriori algorithm
│   ├───csv             # {asso_rulesX_Y,freq_itemsX_Y}.csv, other csv files
│   └───fpgrowth        # actualX_Y.json, using fpgrowth algorithm
├───figures             # figures generated for results and tests
├───results             # results and test files
│   ├───apriori         # recStandardX_Y.json, using apriori algorithm
│   ├───fpgrowth        # recStandardX_Y.json, using fpgrowth algorithm
│   └───tests           # files created for and by tests
│       ├───distances   # tests concerning distances
│       │   ├───apriori         # using apriori algorithm
│       │   │   ├───std100          # based on 100 standard routes
│       │   │   ├───std1000         # based on 1000 standard routes
│       │   │   └───std500          # based on 500 standard routes
│       │   ├───fpgrowth        # using fpgrowth algorithm
│       │   │   ├───std100          # based on 100 standard routes
│       │   │   ├───std1000         # based on 1000 standard routes
│       │   └───└───std500          # based on 500 standard routes
│       ├───graphs      # graphs for questions 2 and 3
│       ├───q2          # test files concerning question2
│       └───q3          # test files concerning question3
├───src                     # main source code files
└───└───dataGenerator       # files to generate data
```

The files that already exist in `./results/` and `./data/` when cloning the project have no other purposes than to be an example of the data we obtained and used, and to ensure the existence of all needed directories.


## How2 - Prepare the synthetic datasets

**Step 1 - Generate the data**

This step aim to create all the files needed for the execution of questions 1, 2, and 3. 

All the following mentionned JSON files should appear into `./data/` directory

```sh
# on Linux or WSL
python3 ./src/mainRulesGeneration.py
# establish the main rules that will affect drivers' agenda

python3 ./src/driverGeneration.py <nb_drivers>
# create <nb_drivers> drivers (if none, create 10)

python3 ./src/stdGeneration.py <nb_std_routes>
# create <nb_std_routes> standard routes into  (if none, create 500)
# save file into standard<nb_std_routes>.json file

python3 ./src/actualGeneration.py <nb_act_routes> ./data/<std_routes_file>.json ./data/<actual_file_to_save>.json 
# create <nb_act_routes> actual routes based on <std_routes_file> file
# save data into <actual_file_to_save> file (./data/actual.json, according to the subject)
# warning : all arguments must be filled !
```

**Step 2 - Identify association rules and frequent itemsets**
```sh
python3 ./src/merchFIAndAssoRules.py <support> <threshold> ./data/<actual_routes_file> ./data/csv/<FI_to_save_csv>.csv ./data/csv/<assoRules_to_save_csv>.csv ./data/<FI_to_save_json>.json
# e.g. support = 0.3, threshold = 0.8
```
Based on the <actual_routes_file> provided (i.e. the one previously created for example), extract the frequent itemsets and association rules with 'support' support and 'threshold' threshold.
It will save the frequent itemsets and association rules into `./data/csv/` directory in CSV files. A JSON file with the found frequent itemsets will also be created in `./data/` directory.


**By default**
```sh
python3 ./src/exe_script.py
```

This command will execute `mainRulesGeneration.py`, `driverGeneration.py`, `stdGeneration.py`, `actualGeneration.py`, `merchFIAndAssoRules`, and will create 100 drivers, 500 standard routes, 5000 actual routes, and create frequent itemsets and association rules files, by default.

It will store the data created in `./data/` directory, as followed :

```sh
data
├───apriori
├───csv
├    - freq_items.csv
├    - asso_rules.csv
└───fpgrowth
- actual.json
- drivers.json
- freq_items.json
- mainRules.json
- standard.json
```

**WARNING**

Because of random selections concerning the routes creations, this error may be raised : 
```bash
ValueError: The input DataFrame `df` containing the frequent itemsets is empty.
```
In that case, execute the script again. 

**Note for next steps**

The main code, for each of the following steps, is respectively written in the files : 

- `./src/q1_recStandard.py`
- `./src/q2_driver.py`
- `./src/q3_perfectRoute.py`

# Step 1 : Recommanded standard routes

**Prerequisites**

To make recommandations, it is necessary to have the following file (or any other frequent itemsets csv file in that directory):

- `./data/csv/freq_items.csv`


**Recommanding standard routes**
To create a list of recommanded standard routes, execute the following command : 

```sh
python3 ./src/q1_recStandard.py <nb_recStd_routes> ./data/csv/<FI_file_csv>.csv ./results/<recStandard_file_to_save>.json
```

This returns `./results/recStandard.json`.

# Step 2 : List of 5 standard routes for each driver to minimize diversions

**Prerequisites**

- `./results/recStandard.json` (the file must have this name)

**Identify, for each driver, 5 best routes to minimize diversions**

In order to identify, for each driver, the five routes that, if a driver does them, it minimizes the diversion, run the following command : 

```sh
python3 ./src/q2_driver.py
```

It will create `./data/std_rankings.json`, and will return `./results/driver.json`.

# Step 3 : Best standard route for each driver

**Best standard route for each driver**

```sh
python3 ./src/q3_perfectRoute.py
```

This returns `./results/perfectRoute.json`.

