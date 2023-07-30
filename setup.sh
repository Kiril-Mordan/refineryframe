# run lint test
./pylint_test.sh

# generate md file for example
jupyter nbconvert --to markdown --execute example_notebooks/duv_score_class.ipynb --output-dir=docs

# uplate licence year
./update_licence.sh

# combine README_base.md with example
cat docs/README_base.md > README.md
cat docs/duv_score_class.md >> README.md

# update package version
./update_package_version.sh

# generate new files
#python3 setup.py sdist bdist_wheel

