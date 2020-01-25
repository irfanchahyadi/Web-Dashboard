# Web-Dashboard
Dashboard for displaying company performance on web based.
Here are some of the features so far:
- Login page
- Dashboard overview
- Full color chart by [Chart.js](https://github.com/chartjs/Chart.js)
- Report for: Sales, Delivery, Revenue
- Branch location by [Leaflet](https://github.com/Leaflet/Leaflet) + [OpenStreetMap](https://www.openstreetmap.org/)


Currently deploy on my Free Tier AWS EC2 at [here](http://13.58.205.195/).

login with username: user & password: user

## How to deploy
Further will be just technical stuff.

Here are step by step how i deploy this web to my Free Tier AWS EC2 (Ubuntu) machine:

Clone this repository
```
mkdir web
cd web
git clone https://github.com/irfanchahyadi/Web-Dashboard.git
```

Set up Environment
```
pip3 install virtualenv
sudo apt-get install python3-venv
cd Web-Dashboard
python3 -m venv venv
source venv/bin/activate
```

Install required tools
```
pip3 install -r requirements.txt
deactivate
```
This require :
- [Flask](https://github.com/pallets/flask), web application framework
- [Gunicorn](https://github.com/benoitc/gunicorn), WSGI HTTP server
- [Pandas](https://github.com/pandas-dev/pandas), for data sorting and filtering
- [Python-dotenv](https://github.com/theskumar/python-dotenv), for storing some secret key

Create .service file
```
sudo nano /etc/systemd/system/app.service
```
paste this code
```
[Unit]
Description=Gunicorn instance to serve app flask_test
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/web/Web-Dashboard
Environment="PATH=/home/ubuntu/web/Web-Dashboard/venv/bin"
ExecStart=/home/ubuntu/web/Web-Dashboard/venv/bin/gunicorn --workers 3 --bind unix:app.sock -m 007 wsgi:app

[Install]
WantedBy=multi-user.target
```

Start service
```
sudo systemctl start app
sudo systemctl enable app
sudo systemctl status app
```
If you do it correctly, you will get something like this
>● app.service - Gunicorn instance to serve app flask_test
>   Loaded: loaded (/etc/systemd/system/app.service; **enabled**; vendor preset: **enabled**)
>   Active: **active (running)** 



Install and configure Nginx
```
sudo apt install nginx
sudo ufw allow 'Nginx HTTP'
sudo nano /etc/nginx/sites-available/app
```
paste this code
```
server {
    listen 80;
    server_name 13.58.205.195 www.13.58.205.195;

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/web/Web-Dashboard/app.sock;
    }
}
```

Enable Nginx server block configuration
```
sudo ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

Edit Inbound Rule
- Go to your EC2 console
- Click security group on your instance
- Edit Inbound rule
- Add HTTP type in port 80 from anywhere

Restart systemctl app, every update web app
```
sudo systemctl restart app
```
