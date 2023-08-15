# generate md file for examples
echo 'Generating md file for example1'
jupyter nbconvert --to markdown --execute example_notebooks/general_example_1.ipynb --output-dir=doc

echo 'Generating md file for example2'
jupyter nbconvert --to markdown --execute example_notebooks/general_example_2.ipynb --output-dir=doc


# generate md file for feature list
echo 'Generating md file for feature list'
cd tools/
python -m generate_feature_list
cd ..

# make README_base.md a beginning of README.md
echo 'making README_base.md a beginning of README.md'
cat doc/README_base.md > README.md
echo '' >> README.md

# add feature list to README.md
echo 'adding feature list to README.md'
cat doc/feature_list.md >> README.md
echo '' >> README.md

# add content table to README.md
echo 'adding content table to README.md'
cat doc/content.md >> README.md
echo '' >> README.md
echo '' >> README.md

# add example1 to README.md
echo 'adding example1 to README.md'
cat doc/general_example_1.md >> README.md
echo '' >> README.md

# add example1 to README.md
echo 'adding example2 to README.md'
cat doc/general_example_2.md >> README.md
echo '' >> README.md

# add score to README.md
echo 'adding score to README.md'
cat doc/scores.md >> README.md
echo '' >> README.md



