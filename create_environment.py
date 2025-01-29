# import os
# import sys
# import subprocess

# def create_virtualenv(env_name):
#     # Create virtual environment
#     subprocess.run([sys.executable, '-m', 'venv', env_name])

# def activate_virtualenv(env_name):
#     activate_script = ''
#     if os.name == 'nt':  # For Windows
#         activate_script = os.path.join(env_name, 'Scripts', 'activate.bat')
#     else:  # For macOS and Linux
#         activate_script = os.path.join(env_name, 'bin', 'activate')
    
#     print(f"Run the following command to activate the virtual environment:\nsource {activate_script}" if os.name != 'nt' else f"{activate_script}")

# def install_dependencies(env_name, requirements_file):
#     # Construct the pip install command
#     if os.name == 'nt':
#         pip_executable = os.path.join(env_name, 'Scripts', 'pip')
#     else:
#         pip_executable = os.path.join(env_name, 'bin', 'pip')
    
#     subprocess.run([pip_executable, 'install', '-r', requirements_file])

# def run_ollama_pull():
#     try:
#         # Execute the shell command
#         # result = subprocess.run(['ollama', 'pull', 'phi3'], check=True, capture_output=True, text=True)
#         result = subprocess.run(['ollama', 'pull', 'llama3.2-vision'], check=True, capture_output=True, text=True)
#         # Print the standard output
#         print(result.stdout)
#     except subprocess.CalledProcessError as e:
#         # Print the standard error if the command fails
#         print(f"An error occurred: {e.stderr}")

# if __name__ == "__main__":
#     env_name = 'aia_venv'
#     requirements_file = 'requirements.txt'
    
#     create_virtualenv(env_name)
#     activate_virtualenv(env_name)
#     # After activation, install dependencies
#     install_dependencies(env_name, requirements_file)

#     run_ollama_pull()


import os
import sys
import subprocess

def create_virtualenv(env_name):
    """
    Creates a virtual environment with the specified name.
    """
    subprocess.run([sys.executable, '-m', 'venv', env_name], check=True)
    print(f"Virtual environment '{env_name}' created successfully.")

def get_pip_executable(env_name):
    """
    Returns the path to the pip executable within the virtual environment.
    """
    if os.name == 'nt':  # For Windows
        return os.path.join(env_name, 'Scripts', 'pip')
    else:  # For macOS and Linux
        return os.path.join(env_name, 'bin', 'pip')

def update_pip(env_name):
    """
    Upgrades pip inside the virtual environment.
    """
    pip_executable = get_pip_executable(env_name)
    subprocess.run([pip_executable, 'install', '--upgrade', 'pip'], check=True)
    print("Pip has been upgraded inside the virtual environment.")

def install_dependencies(env_name, requirements_file):
    """
    Installs dependencies listed in the requirements file inside the virtual environment.
    """
    pip_executable = get_pip_executable(env_name)
    subprocess.run([pip_executable, 'install', '-r', requirements_file], check=True)
    print(f"Dependencies from '{requirements_file}' have been installed.")

def run_ollama_pull():
    """
    Runs the ollama pull command to download the specified model.
    """
    try:
        result = subprocess.run(['ollama', 'pull', 'llama3.2-vision'], check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while pulling the model: {e.stderr}")

if __name__ == "__main__":
    env_name = 'aia_venv'
    requirements_file = 'requirements.txt'
    
    try:
        create_virtualenv(env_name)
        
        # You would need to manually activate the virtual environment as this is not possible in a script.
        print(f"Activate the virtual environment by running the following command:")
        if os.name == 'nt':
            print(f"    .\\{env_name}\\Scripts\\activate")
        else:
            print(f"    source ./{env_name}/bin/activate")
        
        # Upgrade pip inside the virtual environment
        update_pip(env_name)
        
        # Install dependencies
        install_dependencies(env_name, requirements_file)

        # Run the ollama pull command
        run_ollama_pull()

    except subprocess.CalledProcessError as e:
        print(f"An error occurred during the process: {e}")
