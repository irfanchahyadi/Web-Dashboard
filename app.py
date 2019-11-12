from flask import Flask, render_template, request, session, redirect, url_for
from datetime import datetime, timedelta
import pandas as pd
import sqlite3, hashlib, os, random

app = Flask(__name__)
app.secret_key = "super secret key"
conn = sqlite3.connect('data/web.db', check_same_thread=False)

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
        cur.execute("select password from w_user where username='{}'".format(usr))
        key = cur.fetchone()
        if key:
            if hash_pwd == key[0]:
                # cur2 = conn.cursor()
                # cur2.execute("exec w_user_login '{}'".format(nip))
                # conn.commit()
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
    img = os.listdir('static/images/captcha')[random.randint(0,10)]
    if request.method == 'POST':
        nip = request.form['nip']
        icaptcha = request.form['icaptcha'].replace('.png','')
        captcha = request.form['captcha']
        cur = conn.cursor()
        if icaptcha != hashlib.sha1(captcha.encode('utf-8')).hexdigest():
            msg = "Captcha salah, mohon input captcha dengan benar"
            sts = 'NOT OK'
        elif cur.execute("select count(*) from w_user where nip='{}' and login_count>0".format(nip)).fetchone()[0] > 0:
            msg = "Nip ini sudah punya akun"
            sts = 'NOT OK'
        else:
            try:
                cur = conn.cursor()
                to = cur.execute("select fitalamat from fit where fitkode='{}'".format(nip)).fetchone()
                if to:
                    threading.Thread(target=kirimPassword_insert, args=(nip, to[0] + '@nusantara-sakti.com')).start()
                    # spwd = kirimPassword_insert(nip, to[0] + '@nusantara-sakti.com')
                    msg = "Anda telah berhasil mendaftar. Silahkan login dengan password yang sudah dikirimkan ke email anda."
                    sts = 'OK'
                else:
                    msg = "Pendaftaran gagal. Nip salah ketik atau anda belum punya email @nusantara-sakti.com."
                    sts = 'NOT OK'
            except Exception as e:
                msg = str(e)
                msg += "Pendaftaran gagal. Silahkan hubungi admin untuk keterangan lebih lanjut."
                sts = 'NOT OK'
    data = {"msg": msg, "img": img, "sts": sts}
    return render_template('signup.html', data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
