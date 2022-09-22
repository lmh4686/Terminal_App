#!/bin/bash
printf 'To run the prgoram,\nI need your permission to install the following modules:\n'
cat requirements.txt
echo "Do you authorise to install? [Y,n]"
read input
if [[ $input == "Y" || $input == "y" ]]; then
    echo "Creaing & Activaing Virtual Environment..."
    python3 -m venv .venv 
    source .venv/bin/activate
    echo "Installing packages..."
    pip install -r requirements.txt
    python3 main.py $1
    exit 0
else
    echo "Program terminating"
    exit 1
fi