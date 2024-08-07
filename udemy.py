import subprocess, sys, os
from IPython.display import clear_output, HTML, display
import base64 

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
            print(f"Installing {package_name} library not by default in Google Colab")
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
def display_selected_ticker(ticker, df):
    code = ticker
    name = df[df['code'] == ticker]['name'].values[0]
    print(f"Selected Ticker: {code}\nCompany Name: {name}")
    return code, name  # Return code and name
    
def cloning_repo():
    # This function will clone or update the repo in github with all the files
    # But it's in the Google Colab environment, not in the local user's computer
    # Call the function to execute the process of cloning or updating the repository
    # udemy.cloning_repo()
    repo_path = '/content/udemy_advances_ta_ml'  # Path where the repository will be cloned
    
    # Check if the repository directory already exists
    if not os.path.exists(repo_path):
        # It does not exist, clone the repository
        os.system(f'git clone https://github.com/AImetricsIO/udemy_advances_ta_ml.git {repo_path}')
        print(f"Repository cloned successfully in Google Colab environment to {repo_path}")
    else:
        # It does exist, update the repository
        try:
            os.chdir(repo_path)
            os.system('git pull origin main')
            print(f"Repository cloning updated successfully in Google Colab environment to {repo_path}")
        except Exception as e:
            print(f"Failed to update repository: {e}")

# Function to create a download button
def create_download_link(df, filename, title="Download CSV file"):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # Codificar en base64 para la descarga
    href = f'data:text/csv;base64,{b64}'  # Crear el enlace de descarga
    
    # Generar el botón de descarga
    button_html = f'<a download="{filename}" href="{href}" target="_blank">{title}</a>'
    
    return HTML(button_html)

