import subprocess
import os

def execute_data_generation(user_email):
    """ Runs the data generation script with the user's email as an argument. """
    script_url = "https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/datagen.py"
    command = f"uv pip install uv && python -c \"import urllib.request; exec(urllib.request.urlopen('{script_url}').read().decode())\" {user_email}"
    
    try:
        subprocess.run(command, shell=True, check=True)
        print("Data generation completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error in data generation: {e}")

def execute_prettier_format():
    """ Formats the contents of /data/format.md using Prettier 3.4.2 """
    try:
        subprocess.run(["npx", "prettier@3.4.2", "--write", "/data/format.md"], check=True)
        print("Formatting completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error in formatting: {e}")