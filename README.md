# MovieBox

## Requirements
1. python +3.7
2. pip
3. node
4. npm

## Installation
After cloning the project, in the main directory:
1. Create venv: `virtualenv -p python3 venv`
2. Activate venv: `source venv/bin/activate`
3. Packages install: `pip install -r requirements/dev.pip`
5. To start django app: `python manage.py runserver 0:8000`
6. Run within theme/static_src: `npm install`
7. To start tailwind: `python manage.py tailwind start`

## Installing flake8 pre-commit hook
1. Install git pre-commit hook by: `flake8 --install-hook git`
2. Configure it to be strict with: `git config --bool flake8.strict true`
