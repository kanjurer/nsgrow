#!/bin/bash

# Find all .ipynb files and sort them
notebooks=($(find ./src -maxdepth 1 -type f -name "*.ipynb" | sort))

# Check if there are any notebooks found
if [ ${#notebooks[@]} -eq 0 ]; then
    echo "No .ipynb files found in the current directory."
    exit 1
fi

# Loop through each notebook and execute it
for notebook in "${notebooks[@]}"
do
    echo "Running notebook: $notebook"
    output_dir="output_notebooks/"
    mkdir -p "$output_dir"
    output_notebook="$output_dir$(basename "$notebook")"
    jupyter nbconvert --to notebook --execute "$notebook" --output "$output_notebook"

    # Check the exit status of the execution
    if [ $? -eq 0 ]; then
        echo "Notebook ran successfully: $notebook"
    else
        echo "Error running notebook: $notebook"
        exit 1
    fi
done

echo "All notebooks executed successfully"