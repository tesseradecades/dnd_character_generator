# dnd_character_generator

[![Python application](https://github.com/tesseradecades/dnd_character_generator/actions/workflows/python-app.yml/badge.svg)](https://github.com/tesseradecades/dnd_character_generator/actions/workflows/python-app.yml)

## developer setup
* Set up virtual environment
```
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```
* Test the linter
```
black . --check --diff
```
* Run unit tests
```
pytest test
```
* start server
```
uvicorn main:app --reload
```