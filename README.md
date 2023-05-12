# Modern python app boilerplate

Included in this boilerplate:

 - pyenv for python version management
 - [poetry](https://python-poetry.org/) for dependency management
 - [pre-commit](https://pre-commit.com/) for linting and formatting
 - [pytest](https://docs.pytest.org/en/stable/) for testing
 - [black]() for formatting
 - [flake8]() for linting
 - [isort]() for sorting imports
 - [mypy]() for static type checking


## How to start

1. Make sure you have python required interpreter installed in pyenv e.g.
2. Rename app folder to your app name if needed and then:

       find ./ -type f -not -path "./.git/*" -exec sed -i 's/app_name/new_app_name/g' {} \;
       find ./ -type f -not -path "./.git/*" -exec sed -i 's/app-name/new-app-name/g' {} \;

3. mv app_name new_app_name
4. `make install`
5. `make test`
6. Make sure it's working: `poetry run app-cli "Developer"`
7. Optionally, squeeze history into one commit: `git reset $(git commit-tree HEAD^{tree} -m "Initial commit")`
