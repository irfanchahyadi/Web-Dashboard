from flask import Flask, render_template, request, session, redirect, url_for
from datetime import datetime, timedelta
import pandas as pd
import sqlite3, hashlib, os, random, os, dotenv

app = Flask(__name__)
app.secret_key = "super secret key"
dotenv.load_dotenv()
MAPBOX_TOKEN = os.getenv('MAPBOX_TOKEN')
conn = sqlite3.connect('data/web.db', check_same_thread=False)

@app.route('/dashboard/')
def dashboard():
    w_all = pd.read_sql("select * from w_all", conn)
    w_sales_history = pd.read_sql("select * from w_sales_history", conn)
    data = {"all": w_all, "sales_history": w_sales_history}
    yesterday = datetime.now() - timedelta(days=1)
    return render_template('dashboard.html', date=yesterday.strftime("%d %b %Y"), data=data)

@app.route('/sales/')
def sales():
    w_sales = pd.read_sql("select * from w_sales", conn)
    w_sales_days = pd.read_sql("select * from w_sales_days", conn)
    data = {"sales": w_sales, "days": w_sales_days}
    yesterday = datetime.now() - timedelta(days=1)
    return render_template('sales.html', date=yesterday.strftime("%d %b %Y"), data=data)

@app.route('/delivery/')
def pod():
    w_delivery = pd.read_sql("select * from w_delivery", conn)
    w_courier = pd.read_sql("select * from w_courier", conn)
    data = {"delivery": w_delivery, "courier": w_courier}
    yesterday = datetime.now() - timedelta(days=1)
    return render_template('delivery.html', date=yesterday.strftime("%d %b %Y"), data=data)

@app.route('/', methods=['GET','POST'])
@app.route('/login/', methods=['GET','POST'])
def login():
    msg = ''
    sts = ''
    if request.method == 'POST':
        usr = request.form['username']
        pwd = request.form['password']
        hash_pwd = hashlib.sha1(pwd.encode('utf-8')).hexdigest()
        cur = conn.cursor()
        cur.execute("SELECT password FROM w_user WHERE username='{}'".format(usr))
        key = cur.fetchone()
        if key:
            if hash_pwd == key[0]:
                cur2 = conn.cursor()
                login = cur2.execute("SELECT count_login FROM w_user where username='{}'".format(usr)).fetchone()[0]
                cur2.execute("UPDATE w_user SET count_login={}, datetime_register='{}' WHERE username='{}'".format(login+1, datetime.now(), usr))
                conn.commit()
                session['username'] = usr
                return redirect(url_for('dashboard'))
            else:
                msg = 'Username or password invalid'
                sts = 'NOT OK'
        else:
            msg = 'Username or password invalid'
            sts = 'NOT OK'
    return render_template('login.html', data=msg)

@app.route("/logout/")
def logout():
    session['username'] = None
    return login()

@app.route('/signup/', methods=['GET','POST'])
def signup():
    msg = ''
    sts = ''
    img = os.listdir('static/images/captcha')[random.randint(0,9)]
    if request.method == 'POST':
        usr = request.form['username']
        pwd = request.form['password']
        repwd = request.form['repassword']
        icaptcha = request.form['icaptcha'].replace('.png','')
        captcha = request.form['captcha']
        cur = conn.cursor()
        if pwd != repwd:
            msg = "Your password is not same"
            sts = 'NOT OK'
        elif len(usr)<5:
            msg = "Username too short"
            sts = 'NOT OK'
        elif len(pwd)<5:
            msg = "Password too short"
            sts = 'NOT OK'
        elif icaptcha != hashlib.sha1(captcha.encode('utf-8')).hexdigest():
            msg = "You type captcha wrong"
            sts = 'NOT OK'
        elif cur.execute("SELECT count(*) FROM w_user WHERE username='{}'".format(usr)).fetchone()[0] > 0:
            msg = "This username is not available"
            sts = 'NOT OK'
        else:
            try:
                hash_pwd = hashlib.sha1(pwd.encode('utf-8')).hexdigest()
                sql_insert = """
                    INSERT INTO w_user VALUES ('{}', '{}', '{}', null, 0);""".format(usr, hash_pwd, datetime.now())
                cur.execute(sql_insert)
                conn.commit()
                msg = "Thanks for Register. You can now login with your username."
                sts = 'OK'
            except Exception as e:
                msg = str(e)
                msg += "Registration failed. Contact our support for more information."
                sts = 'NOT OK'
    data = {"msg": msg, "img": img, "sts": sts}
    return render_template('signup.html', data=data)

@app.route('/location/')
def location():
    w_branch = pd.read_sql("select * from w_branch", conn)
    data = {"branch": w_branch, "mapbox_token": MAPBOX_TOKEN}
    yesterday = datetime.now() - timedelta(days=1)
    return render_template('location.html', date=yesterday.strftime("%d %b %Y"), data=data)

@app.route('/galery/')
def galery():
    w_galery = pd.read_sql("select * from w_galery", conn)
    data = {"galery": w_galery}
    yesterday = datetime.now() - timedelta(days=1)
    return render_template('galery.html', date=yesterday.strftime("%d %b %Y"), data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
