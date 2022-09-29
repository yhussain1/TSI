# micro web framework to develop websites with python
# on cmd "pip install flask"
# import request
# import session
# import flash
#import sqlalchemy

from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # creates web application instance
app.secret_key = "Orange" # decrypt and encrypt the data
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes = 2) # stores permanent session data for a time period given

db = SQLAlchemy(app)


@app.route("/") # defines how to access the page e.g. yahya.com/
def home(): # new page needs a function
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"]) # GET - receiving/sending information to a client/website, POST - secure method of GET where info not stored on webserver
def login():
    if request.method == "POST": # when information inputted (POST) by user into the site redirects to the url
        session.permanent = True # adds permanent stay time for session
        user = request.form["nm"] # user is the input by the user on the site
        session["user"] = user # session stores the user input data, closing the browser will delete session data
        flash(f"You have been logged in!", "info") # shows message once
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash(f"Already logged in!", "info")
            return redirect(url_for("user")) # if logged in redirect to user page not go to login page
        return render_template("login.html")

@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session: # user is in session
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            flash("Email was saved")
        else:
            if "email" in session:
                email = session["email"]

        return render_template("user.html", email = email)
    else:
        flash(f"You are not logged in.", "info")
        return redirect(url_for("login")) # redirects to  login page if user not in session

@app.route("/logout")
def logout():
    flash(f"You have been logged out!", "info")
    session.pop("user", None) # remove user data from session
    session.pop("email", None)
    return redirect(url_for("login"))

if __name__ == "__main__": # will run the app
    app.run(debug=True) # no need to rerun server if there are changes as it will automatically detect the changes
