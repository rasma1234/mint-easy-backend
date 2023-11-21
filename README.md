# Smart_Invest

- Clone the project from github / when it's cloned then pull it from github
- create the virtuel environment with python -m venv .venv
- start the virtuel environment with source .venv/bin/activate
- install the requirements.txt with pip install -r requirements.txt
- create the .env in your local project (where is the manage.py)
- copy the following code into the .env:

#postgresql

DB_NAME=projectx

DB_USER=[this your username for the database]

DB_PASSWORD=[this is your password for the database]

DB_HOST=localhost

DB_PORT=5432

* create the projectx in the database
* run the python manage.py makemigrations
* run the python manage.py migrate
*
