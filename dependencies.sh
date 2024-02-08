#!/bin/bash

# Define required dependencies
dependencies=(
    g4f
    typing
    termcolor
    pexels-api-py
    requests
    # Add more packages as needed
)

# Install dependencies using pip
for package in "${dependencies[@]}"; do
    pip install "$package"
done