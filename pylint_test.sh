#!/bin/bash

# Function to run Pylint on a Python script and capture the score
function run_pylint() {
    pylint_output=$(pylint "$1")
    pylint_score=$(echo "$pylint_output" | grep -o 'Your code has been rated at [0-9.]\+')
    echo "${pylint_score#* }"
}

# List of Python files to check
scripts=("refineryframe/other.py" "refineryframe/detect_unexpected.py" "refineryframe/replace_unexpected.py" "refineryframe/refiner.py")

# Threshold score to pass the Pylint check
threshold_score=8

# Loop through the list of scripts and check Pylint score
all_pass=true
for script in "${scripts[@]}"; do
    score=$(run_pylint "$script")
    echo "Pylint score for $script is $score"
    if (( $(awk -v score="$score" -v threshold="$threshold_score" 'BEGIN { print (score >= threshold) }') )); then
        all_pass=true
    fi
done

# Check if all scripts passed the Pylint check
if $all_pass; then
    echo "All scripts passed the Pylint check!"
    exit 0
else
    echo "Some scripts did not pass the Pylint check!"
    exit 1
fi

