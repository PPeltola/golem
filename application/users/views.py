from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.users.models import User
from application.users.forms import LoginForm, RegisterForm

@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("users/login.html", form=LoginForm())

    form = LoginForm(request.form)
    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()

    if not user:
        return render_template("users/login.html", form=form, error="Invalid password or username")
    
    login_user(user)

    return redirect(url_for("campaigns_list"))

@app.route("/logout/")
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route("/register/", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("users/register.html", form=RegisterForm())
    
    form = RegisterForm(request.form)

    if not form.validate():
        return render_template("users/register.html", form=form)
    
    if (User.query.filter_by(username=form.username.data).first() != None):
        return render_template("users/register.html", form=form, error="Username is already taken")

    user = User(form.username.data, form.password.data)

    db.session().add(user)
    db.session().commit()

    login_user(user)

    return redirect(url_for("campaigns_list"))