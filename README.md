[![CI](https://github.com/b1r3k/python-poetry-boilerplate/actions/workflows/ci.yaml/badge.svg)](https://github.com/b1r3k/python-poetry-boilerplate/actions/workflows/ci.yaml)

# Modern python app boilerplate

Included in this boilerplate:

 - [pyenv](https://github.com/pyenv/pyenv) for python version management
 - [poetry](https://python-poetry.org/) for dependency management integrated with pyenv
 - [pre-commit](https://pre-commit.com/) for linting and formatting
 - [pytest](https://docs.pytest.org/en/stable/) for testing
 - [ruff](https://docs.astral.sh/ruff/) for formatting, linting, sorting imports etc.
 - [mypy](https://mypy.readthedocs.io/en/stable/) for static type checking
 - settings management implemented using [pydantic/pydantic-settings](https://github.com/pydantic/pydantic-settings) allows overriding settings values by environment variables, .env file etc.
 - root logger based on settings

## What is going on?

Pyenv selects python version according to .python-version file in the root of the project. Poetry creates virtualenv in .venv directory in the root of the project. Pre-commit installs hooks in .git/hooks folder. Ruff is used by pre-commit to format, lint, sort imports etc.


## How to start

1. Make sure you have python required interpreter installed in pyenv e.g.
2. Rename project:
 - Rename app folder to your app name if needed (`mv app_name new_app_name`) and then:

       find ./ -type f -not -path "./.git/*" -exec sed -i 's/app_name/new_app_name/g' {} \;
       find ./ -type f -not -path "./.git/*" -exec sed -i 's/app-name/new-app-name/g' {} \;
 - or use `make rename-project NEW_APP_NAME=new_app_name` to do it for you

3. `make install`
4. `make test`
5. Make sure it's working: `poetry run app-cli "Developer"`
6. Optionally, squeeze history into one commit: `git reset $(git commit-tree HEAD^{tree} -m "Initial commit")`

## Other useful commands

 - Check current poetry virtualenv and change it

```bash
   $ poetry env info
   $ poetry env list
   $ poetry env remove /home/PATH/bin/python
   $ make install
```

 - Cherry-pick commit from repository cloned from this one:

```bash
   $ git remote add projectB /home/you/projectB
   $ git fetch projectB
   $ git cherry-pick <commit from projectB repo>
```
