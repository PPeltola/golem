from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required

from application import app, db
from application.campaigns.models import Campaign
from application.campaigns.forms import CampaignForm
from application.characters.models import Character

@app.route("/campaigns/")
def campaigns_list():
    return render_template("campaigns/list.html", campaigns=Campaign.query.all())

@app.route("/campaigns/<campaign_id>", methods=["GET"])
def campaigns_index(campaign_id):
    if Campaign.query.get(campaign_id).account_id == current_user.get_id():
        return render_template("campaigns/gm_index.html",
         campaign=Campaign.query.get(campaign_id),
         active_characters=Character.find_all_characters_in_campaign_by_status(status=1, campaign_id=campaign_id),
         inactive_characters=Character.find_all_characters_in_campaign_by_status(status=0, campaign_id=campaign_id))
    elif (current_user.is_authenticated):
        return render_template("campaigns/player_index.html",
         campaign=Campaign.query.get(campaign_id),
         owned_active_characters=Character.find_users_characters_in_campaign_by_status(status=1, user_id=current_user.get_id(), campaign_id=campaign_id), 
         owned_inactive_characters=Character.find_users_characters_in_campaign_by_status(status=0, user_id=current_user.get_id(), campaign_id=campaign_id))
    else:
        return render_template("campaigns/index.html", campaign=Campaign.query.get(campaign_id))

@app.route("/campaigns/new", methods=["GET", "POST"])
@login_required
def campaigns_create():
    if request.method == "GET":
        return render_template("campaigns/new.html", form=CampaignForm())

    form = CampaignForm(request.form)
    
    if not form.validate():
        return render_template("campaigns/new.html", form=form)

    if Campaign.query.filter_by(name=form.name.data).first() != None:
        return render_template("campaigns/new.html", form=form, error="Campaign name is already taken")
    
    campaign = Campaign(form.name.data)

    campaign.account_id = current_user.id
    
    db.session().add(campaign)
    db.session().commit()

    return redirect(url_for("campaigns_index", campaign_id=campaign.id))