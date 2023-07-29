#!/bin/bash

# Read the current version from the setup.py file
VERSION=$(grep -o "VERSION = '[0-9.]\+'" setup.py | grep -o "[0-9.]\+")

# Increment the last number in the version string
VERSION=$(echo $VERSION | awk -F. '{print $1"."$2"."$3+1}')

# Replace the old version with the updated version using Python
python3 - <<EOF
import re

with open('setup.py', 'r') as file:
    setup_py = file.read()

# Replace the old version with the updated version using regex
setup_py = re.sub(r"VERSION = '[0-9.]+'", "VERSION = '{}'".format("$VERSION"), setup_py)

with open('setup.py', 'w') as file:
    file.write(setup_py)
EOF

echo "Updated version to $VERSION"

