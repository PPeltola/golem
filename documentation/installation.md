#Installation instructions

GOLEM is developed on and currently only supporting Linux. I have no idea if and how it will work on other operating systems.

## Requirements

	- Python 3, python3-pip and python virtual environment (venv).
	- SQLite3
	- Heroku, if you want to install the application to Heroku

## Local installation

1. Clone the git project by running:
```
git clone git@github.com:PPeltola/golem.git
```

2. Create the python virtual environment:
```
python3 -m venv venv
```

3. Activate it:
```
source venv/bin/activate
```

4. Install the requirements:
```
pip install -r requirements.txt
```

5. Run the application:
```
python3 run.py
```

The app is now running at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Heroku installation

1. Install and activate the app and the venv locally as instructed above

2. Create the app in Heroku:

```
heroku create [put app name here]
```

3. Add the Heroku remote to git:

```
git remote add heroku 
```

4. Push the app to Heroku:
```
git add .
git commit -m "Initial commit."
git push heroku master
```

5. Set the app to Heroku mode:
```
heroku confic:set HEROKU=1
```

6. Add a database to Heroku:
```
heroku addons:add heroku-postgresql:hobby-dev
```

The app should now be running in Heroku.
