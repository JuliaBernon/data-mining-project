# Data Mining project - DM23_Bernon_Marcandella

Subject : 
**On identifying the compensation for vaguely followed trips**

This project falls within the *Data Mining Course, University of Trento*, 2023-2024

Instructor : Prof. Yannis Valagrakis

## Members
Julia Bernon - Ulysse Marcandella

Team name : 

## Description

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


## How2 - Prepare the datasets

**Step 1 - Install the requirements**
```sh
pip install -r requirements.txt
```

**Step2 (optionnal) - Execute unit tests**
```sh
# installing pytest library
pip install -U pytest

# executing tests
pytest --verbose
```

**Step3 - Generate the data**

- Create actual.json and standard.json into *data* directory

```sh
# on Linux or WSL
python3 ./src/dataGeneration.py

# on PowerShell
```

*Display the data in shell*

This command displays, for each standard route, the associated actual routes, the concerned driver, and the different divergence computations.

```sh
# on Linux or WSL
python3 ./tests/dataParsing.py

# on PowerShell
```

# Step 1 : Recommended standard routes

# Step 2 : List of 5 standard routes for each driver to minimize diversions

# Step 3 : Best standard route for each driver

