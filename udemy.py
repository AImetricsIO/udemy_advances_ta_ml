import subprocess
import sys
from IPython.display import clear_output

def install_and_import(package_name):
    # How to call it: install_and_import('pandas_ta')
    # Installs in Google Colab external libraries
    try:
        # Try to import the package
        __import__(package_name)
        print(f"{package_name} is already installed.")
    except ImportError:
        # If not installed, attempt to install the package
        try:
            print(f"Installing {package_name} library not by default in Colab")
            result = subprocess.run([sys.executable, "-m", "pip", "install", package_name], capture_output=True, text=True)
            # If the installation is successful, clear the partial output and show the final message
            if result.returncode == 0:
                clear_output(wait=True)
                print(f"Successfully installed {package_name}")
                __import__(package_name)
            else:
                # If there's an error, print the full output
                print(result.stdout)
                print(result.stderr)
        except Exception as e:
            print(f"An error occurred during installation: {e}")

# Funcion to show the company in selector
def display_selected_ticker(ticker):
    global code, name
    code = ticker
    name = df[df['code'] == ticker]['name'].values[0]
    print(f"Selected Ticker: {code}\nCompany Name: {name}")

import os
# This function will clone or update the repo in github with all the files
# But it's in the Google Colab environment, not in the local user's computer
def cloning_repo():
    repo_path = '/content/udemy_advances_ta_ml'  # Path where the repository will be cloned
    
    # Check if the repository directory already exists
    if not os.path.exists(repo_path):
        # It does not exist, clone the repository
        !git clone https://github.com/AImetricsIO/udemy_advances_ta_ml.git $repo_path
    else:
        # It does exist, update the repository
        try:
            %cd $repo_path
            !git pull origin main
        except:
            print(f"Failed to change directory to {repo_path}. Make sure the repository is cloned correctly.")

# Call the function to execute the process of cloning or updating the repository
cloning_repo()
