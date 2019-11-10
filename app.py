from flask import Flask, render_template
from datetime import datetime, timedelta
import pandas as pd
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect('data/web.db', check_same_thread=False)

@app.route('/')
@app.route('/dashboard/')
def dashboard():
    w_all = pd.read_sql("select * from w_all", conn)
    w_sales_history = pd.read_sql("select * from w_sales_history", conn)
    data = {"all": w_all, "sales_history": w_sales_history}
    yesterday = datetime.now() - timedelta(days=1)
    return render_template('dashboard.html', date=yesterday.strftime("%d %b %Y"), data=data)

@app.route('/jual/')
def jual():
    w_jual = pd.read_sql("select * from w_jual", conn)
    w_jual_hari = pd.read_sql("select * from w_jual_hari", conn)
    data = {"jual": w_jual, "hari": w_jual_hari}
    kemarin = datetime.now() - timedelta(days=1)
    return render_template('jual.html', date=kemarin.strftime("%d %b %Y"), data=data)

@app.route('/pod/')
def pod():
    w_pod = pd.read_sql("select * from w_pod", conn)
    w_kurir = pd.read_sql("select * from w_kurir", conn)
    data = {"pod": w_pod, "kurir": w_kurir}
    kemarin = datetime.now() - timedelta(days=1)
    return render_template('pod.html', date=kemarin.strftime("%d %b %Y"), data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
