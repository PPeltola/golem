from flask import render_template, redirect, url_for
from flask_login import current_user

from application import app, login_required
from application.campaigns.models import Campaign
from application.characters.models import Character
from application.skills.models import Skill
from application.skills.forms import SkillForm

@app.route("/")
def index():
    if current_user.is_authenticated:
        return render_template("/users/index.html", 
        owned_campaigns=Campaign.find_campaigns_owned_by_user(current_user.get_id()),
        active_characters_in_campaigns=Character.find_users_characters_sorted_by_campaign_by_status(1, current_user.get_id()),
        characters_in_owned_campaigns=Campaign.count_active_characters_in_users_campaigns(current_user.get_id()))
    else:
        return render_template("index.html")

@app.route("/admin", methods=["GET"])
@login_required(role="ADMIN")
def admin():
    return render_template("admin.html", all_skills=Skill.query.all(), form=SkillForm())