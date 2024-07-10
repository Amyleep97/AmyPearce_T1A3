#!/bin/bash

check if git is installed 
check if python is installed
check if pip installed
check if virtual environemnt exsits

run appplication

echo "Start Video Game Trivia"
python3 -m venv venv
source ./venv/bin/activate

python main.py 

deactivate