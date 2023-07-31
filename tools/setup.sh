# run lint test
echo 'running lint test'
./tools/pylint_test.sh

# uplate licence year
echo 'updating licence year'
./tools/update_licence.sh

# update README.md
echo 'updating README.md'
./tools/update_README.sh

# update package version
echo 'updating package version'
./tools/update_package_version.sh

# build and upload latest version to pypi
#python setup.py sdist bdist_wheel
#twine upload --skip-existing dist/*



