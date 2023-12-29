#!/bin/bash

# Activate your virtual environment if you are using one
# source /path/to/your/venv/bin/activate

# Set the path to your Python interpreter
PYTHON_EXECUTABLE=/etc/custom/app/echosync/env/bin/python

# Set the path to your main application file
APP_FILE=/etc/custom/app/echosync/run.py

# Run the app
$PYTHON_EXECUTABLE $APP_FILE
