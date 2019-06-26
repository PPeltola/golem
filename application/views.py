from flask import render_template, redirect, url_for
from flask_login import current_user
from application import app
from application.campaigns.models import Campaign
from application.characters.models import Character

@app.route("/")
def index():
    if current_user.is_authenticated:
        return render_template("/users/index.html", 
        owned_campaigns=Campaign.find_campaigns_owned_by_user(current_user.get_id()),
        characters_in_campaigns=Character.find_active_characters_owned_by_user_by_campaign(current_user.get_id()))
    else:
        return render_template("index.html")