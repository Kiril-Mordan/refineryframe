# generate md file for example
jupyter nbconvert --to markdown --execute example_notebooks/general_example_1.ipynb --output-dir=docs

# generate md file for feature list
python -m generate_feature_list

# combine README_base.md with example
cat docs/README_base.md > README.md
cat docs/feature_list.md >> README.md
echo ' ' >> README.md
cat docs/general_example_1.md >> README.md
