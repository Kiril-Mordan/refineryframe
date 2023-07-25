# generate md file for example
jupyter nbconvert --to markdown --execute example_notebooks/duv_score_class.ipynb --output-dir=docs

# combine README_base.md with example
cat docs/README_base.md > README.md
cat docs/duv_score_class.md >> README.md

# generate new files
python3 setup.py sdist bdist_wheel

