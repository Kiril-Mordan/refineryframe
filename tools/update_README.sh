# generate md file for example
echo 'Generating md file for example'
jupyter nbconvert --to markdown --execute example_notebooks/general_example_1.ipynb --output-dir=docs

# generate md file for feature list
echo 'Generating md file for feature list'
cd tools/
python -m generate_feature_list
cd ..

# make README_base.md a beginning of README.md
echo 'making README_base.md a beginning of README.md'
cat docs/README_base.md > README.md

# add feature list to README.md
echo 'adding feature list to README.md'
cat docs/feature_list.md >> README.md
echo '' >> README.md

# add example1 to README.md
echo 'adding example1 to README.md'
cat docs/general_example_1.md >> README.md
echo '' >> README.md

# add score to README.md
echo 'adding score to README.md'
cat docs/scores.md >> README.md
echo '' >> README.md



