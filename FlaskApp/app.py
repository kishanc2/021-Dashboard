from flask import Flask, render_template, session, redirect, url_for, request
from datetime import datetime, timedelta
from dateutil import parser
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, exc
import sqlalchemy
# import sqlite3 as sql
from flaskext.mysql import MySQL
import os

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

mysql = MySQL()
mysql.init_app(app)

#Replace with your own user & password 
db = create_engine('mysql+pymysql://root:Clever9SQL#Password@user:password/zero2onewebsite')

@app.route('/', methods = ['GET', 'POST'])
def home():
    session['loggedin'] = False
    return render_template('index.html')

@app.route('/dashboard.html', methods = ['GET', 'POST'])
def dashboard():
    # if not session or not session['loggedin']:
    #    return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/login.html', methods = ['GET', 'POST'])
def login():
    if session and session["loggedin"]:
        return redirect(url_for('dashboard'))
    msg = ''

    today_date = datetime.now()
    print(f"log today's date: {today_date}")

    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:

        email = request.form['email']
        password = request.form['password']

        print('Attempted email: ' + email + ' | Attempted pass: ' + password)

        with db.connect() as conn:
             
            select_statement = "SELECT email_address, activation_date FROM users WHERE email_address = %s AND user_password = %s"
            results = conn.execute(select_statement, (email, password))

            for account in results:
                print('DB Results:',account)
                if account:
                    print('parse: ', parser.parse(account['activation_date']))

                    session['loggedin'] = True
                    # session['id'] = account['username']
                    session['email_address'] = account['email_address']
                       
                    return redirect(url_for('dashboard'))
                else:
                    msg = 'Incorrect username/password!'
                    return render_template('login.html', msg=msg)
                    
    return render_template('login.html', msg=msg)

@app.route('/register.html', methods = ['GET', 'POST'])
def register():
    if session and session["loggedin"]:
        return redirect(url_for('dashboard'))
    
    msg = ''

    today_date = datetime.now()
    print(f"reg today's date: {today_date}")

    if request.method == 'POST' and 'email' in request.form and 'password' in request.form and 'firstname' in request.form and 'lastname' in request.form:

        email = request.form['email']
        password = request.form['password']
        passwordrep = request.form['password-rep']
        firstname = request.form['firstname']
        lastname = request.form['lastname']

        if password!=passwordrep:
            msg = "Passwords don't match!"
            print(f"pass: {password} | passrep: {passwordrep}")
            return render_template('login.html', msg=msg)
        
        print(f"pass: {password} | passrep: {passwordrep}")

        with db.connect() as conn:

            select_statement = "SELECT * FROM users WHERE email_address = %s"
            results = conn.execute(select_statement, (email))

            # print(results)

            insert_statement = "INSERT INTO users(email_address, user_password, first_name, last_name, activation_date) VALUES (%s, %s, %s, %s, %s)"
            conn.execute(insert_statement, (email, password, firstname, lastname, today_date))

            session['loggedin'] = True
            # session['id'] = username
            session['email_address'] = email
                            
            return redirect(url_for('dashboard'))
                    
    return render_template('register.html', msg='')



if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')


