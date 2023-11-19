from flask import Flask, redirect, request, session, render_template
from flask import url_for
from flask_assets import Environment, Bundle
from init_db import get_cursor
import psycopg2
import config
import time

app = Flask(__name__, static_url_path="/static", static_folder="static")
app.config.from_object(config)

assets = Environment(app)

scss = Bundle("scss/style.css", filters="scss", output="static/style.css")
assets.register("scss_all", scss)

app.secret_key = "wesleylewis123456"
db_conn = psycopg2.connect(
    host="localhost",
    database="users",
    user="postgres",
    password="gobank"
  )
db_cursor = db_conn.cursor();
db_cursor.execute("select version()")
print(db_cursor.fetchone())

db_cursor.execute("select version()")
print(db_cursor.fetchone())

app.secret_key = "wesleylewis123456"
id = int(time.time())


@app.route("/register", methods=["GET", "POST"])
def register():
    global id
    if request.method == "POST" and "username" in request.form and "password" in request.form:
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]

        db_cursor.execute("select * from user_data where username = %s", (username, ))
        user = db_cursor.fetchone()
        print("user:", user)
        if user:
            msg = "Account already exists"
        else:
            db_cursor.execute("insert into user_data(id, username, password, email) values( %s, %s, %s, %s)", (id, username, password, email))
            id = id + 1
            db_conn.commit()
            return render_template("index.html")
    elif request.method == "POST":
        print("Register")
    print("render template")
    return render_template("index.html" ) 

@app.route("/")
@app.route("/login", methods = ["GET", "POST"])
def login():
    print("in login api")
    msg = ""
    if request.method == "POST" and "username" in request.form and "password" in request.form:
        print("Debug: inside login if condn")
        username = request.form["username"]
        password = request.form["password"]

        print(username, password)

        db_cursor.execute("select * from user_data where username = %s and password = %s", (username, password, ))
        user = db_cursor.fetchone()
        print(user)
        db_conn.commit()
        if user: 
            # Create session for user 
            print("Debug: User logged in")
            session["loggedin"] = True 
            session["id"] = user[0] 
            session["username"] = user[1]
            msg = "Logged in successfully"
            return render_template("dashboard.html")

        else:
            return "invalid credentials"
    return render_template("register.html")

@app.route("/google")
def google():
    return redirect("www.google.com")

@app.route("/logout")
def logout():
    session.pop("loggedin", None)
    session.pop("id", None)
    session.pop("username", None)
    return render_template("index.html")
