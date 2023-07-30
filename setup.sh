# run lint test
echo 'running lint test'
./pylint_test.sh

# uplate licence year
echo 'updating licence year'
./update_licence.sh

# update README.md
echo 'updating README.md'
./update_README.sh

# update package version
echo 'updating package version'
./update_package_version.sh

# build and upload latest version to pypi
#python setup.py sdist bdist_wheel
#twine upload --skip-existing dist/*



