# sudo apt install python3.10.12-venv
#!/bin/bash
python3 -m venv venv

# Activate the virtual environment 
source ./venv/bin/activate

# Install the dependencies from requirments.txt
pip install -r requirments.txt

# Run the main application
python main.py 

# Deactivate the virtual environment

deactivate