# pytest-api

### Setup

Prerequisite: install python 3.7, e.g.:

brew install python3

git clone this_project

Install required packages at root of project:

./setup.sh


#### Run all tests:

./run_tests.sh


#### Adding new dependencies

1) Enter the environment:
source venv/bin/activate

2) Install new dependencies:
pip install foo

3) Freeze requirements to file requitements.txt 
pip freeze > requirements.txt

4) Check-in updated requirements.txt
