#!/bin/bash

# Read the current version from the setup.py file
VERSION=$(grep -o "VERSION = '[0-9.]\+'" setup.py | grep -o "[0-9.]\+")

# Increment the last number in the version string
VERSION=$(echo $VERSION | awk -F. '{$NF = $NF + 1;} 1' OFS=.)

# Replace the old version with the updated version in the setup.py file
awk -v new_version="$VERSION" '/VERSION =/ {gsub(/\047[0-9.]+\047/, "\047" new_version "\047")} 1' setup.py > setup.py.tmp && mv setup.py.tmp setup.py

# Replace the old version with the updated version in the __init__.py file and preserve the other content
awk -v new_version="$VERSION" '/__version__ =/ {gsub(/\047[0-9.]+\047/, "\047" new_version "\047")} 1' refineryframe/__init__.py > refineryframe/__init__.py.tmp && mv refineryframe/__init__.py.tmp refineryframe/__init__.py

echo "Updated version to $VERSION"
