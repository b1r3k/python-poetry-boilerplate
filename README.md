# Modern python app boilerplate

Included in this boilerplate:

 - pyenv for python version management
 - [poetry](https://python-poetry.org/) for dependency management integrated with pyenv
 - [pre-commit](https://pre-commit.com/) for linting and formatting
 - [pytest](https://docs.pytest.org/en/stable/) for testing
 - [black]() for formatting
 - [flake8]() for linting
 - [isort]() for sorting imports
 - [mypy]() for static type checking
 - virtualenv created by poetry resides in `.venv` folder


## How to start

1. Make sure you have python required interpreter installed in pyenv e.g.
2. Rename app folder to your app name if needed (`mv app_name new_app_name`) and then:

       find ./ -type f -not -path "./.git/*" -exec sed -i 's/app_name/new_app_name/g' {} \;
       find ./ -type f -not -path "./.git/*" -exec sed -i 's/app-name/new-app-name/g' {} \;

3. `make install`
4. `make test`
5. Make sure it's working: `poetry run app-cli "Developer"`
6. Optionally, squeeze history into one commit: `git reset $(git commit-tree HEAD^{tree} -m "Initial commit")`

## Other useful commands

 - Check current poetry virtualenv and change it

   $ poetry env info
   $ poetry env list
   $ poetry env remove /home/PATH/bin/python
   $ make install

 - Cherry-pick commit from repository cloned from this one:

   $ git remote add projectB /home/you/projectB
   $ git fetch projectB
   $ git cherry-pick <commit from projectB repo>
