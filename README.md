# Web-Dashboard
Dashboard for displaying KPI on web based

## How to deploy
This is just note for myself, step by step how to deploy it on any linux machine.

Clone this repository
```
git clone https://github.com/irfanchahyadi/Web-Dashboard.git
```

Set up Environment
```
pip install virtualenv
cd Web-Dashboard
virtualenv venv
venv\Scripts\activate
```

Install required tools
```
pip install -r requirements.txt
```
This require :
- [Flask](https://github.com/pallets/flask)
- [Gunicorn](https://github.com/benoitc/gunicorn)
- [Pandas](https://github.com/pandas-dev/pandas)
