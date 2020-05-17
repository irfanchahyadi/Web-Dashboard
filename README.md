# Web-Dashboard
Dashboard for displaying company performance on web based.

<p align="center">
  <img src="demo/demo.gif"><br/>
  <i>Web-Dashboard</i>
</p>

Here are some of the features so far:
- Login page
- Dashboard overview
- Full color chart by [Chart.js](https://github.com/chartjs/Chart.js)
- Report for: Sales, Delivery, Revenue
- Photo and video Galery
- Tariff check
- Tracking Airwaybill
- Branch location by [Leaflet](https://github.com/Leaflet/Leaflet) + [OpenStreetMap](https://www.openstreetmap.org/) using mapbox api


Currently deploy on my Free Tier AWS EC2 at [here](http://13.58.205.195/).

login with username: user & password: user


## Dependences
- [Flask](https://github.com/pallets/flask), web application framework
- [Gunicorn](https://github.com/benoitc/gunicorn), WSGI HTTP server
- [Pandas](https://github.com/pandas-dev/pandas), for data sorting and filtering
- [Python-dotenv](https://github.com/theskumar/python-dotenv), for storing some secret key


## How to deploy
[Here](demo/installation.md) step by step how I deploy this web on AWS EC2.

## License
[MIT License](LICENSE)