# League API
Django API to list basketball league teams, players and match fixtures

# Users
Three types of users are created in this application and all three types can login into the system

## Admin

Admin has access to all endpoints

**Sample Usernames**
- `admin`

## Coach

Coach has access to see own Team details and Player detail endpoints of their own team 

**Sample Usernames**
- `frank`
- `john`
- `dwane`
- `james`

## Player

Player has access only to Match detail endpoint

**Sample Usernames**
- `christopher.holt`
- `michael.perkins`
- `corey.mendoza`
- `todd.kim`
- `michael.higgins`

## How to Run

## Python Version

Make sure your Python version is not below than given version
>`Python 3.9.6`

### Setup Environment

Create a virtual environment in any directory which belongs to own user

- Create Virtual Environment and Activate 
> `python -m venv league-env`
> 
> `source ./league-env/bin/activate`

### Install Dependency Libs

Checkout and navigate to the root directory of the project. Here we install all the dependency libs that we need to install the Virtual Environment that is created.

> `pip install -r requirements.txt`

### Configure DB

Here we migrate and configure the SQLite DB

> `python manage.py makemigrations`

> `python manage.py migrate`

### Generate Fake data
Now we need to import the fake data into the DB using fixtures. **Note that running order is important** 
>`python3 manage.py loaddata --format=yaml teams.yaml`
> 
>`python3 manage.py loaddata --format=yaml admins.yaml`
> 
> `python3 manage.py loaddata --format=yaml coaches.yaml`
> 
>`python3 manage.py loaddata --format=yaml players.yaml`
> 
>`python3 manage.py loaddata --format=yaml matches.yaml`
> 
>`python3 manage.py loaddata --format=yaml master_data.yaml`

### Run Application

Run the Django development server to test the application. The Default DRF Web app will be available on `localhost:8000`

> `python manage.py runserver`

## APIs

Following API Endpoints are accessible with basic username and password authentication provided.

### Authentication

Application uses basic username and password. The password `supunviraj` is commonly configured for all users generated for convenience in testing the API

### Endpoints

Teams
>`GET http://localhost:8000/teams/`

>`GET http://localhost:8000/teams/:id/`

>`GET http://localhost:8000/teams/:id/players?percentile=:value`
---
Players
> `GET http://localhost:8000/players/`

> `GET http://localhost:8000/players/:id/`
---
Matches
> `GET http://localhost:8000/matches/`

> `GET http://localhost:8000/matches/:id/`
---
Statistics
> `GET http://localhost:8000/statistics/`