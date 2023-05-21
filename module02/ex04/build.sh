#!/bin/bash

# Uninstall the package with pip
pip uninstall my_minipack

# Install / Upgrade pip and build
pip install --upgrade pip build

# Build the package
python3 -m build

# Install the package with pip
pip install ./dist/my_minipack-1.0.0.tar.gz
