from flask import render_template, request, redirect, url_for
from flask_login import login_required

from application import app, db
from application.campaigns.models import Campaign
from application.campaigns.forms import CampaignForm

@app.route("/campaigns/")
def campaigns_list():
    return render_template("campaigns/list.html", campaigns=Campaign.query.all())

@app.route("/campaigns/new", methods=["GET", "POST"])
@login_required
def campaigns_create():
    if request.method == "GET":
        return render_template("campaigns/new.html", form=CampaignForm())

    form = CampaignForm(request.form)
    
    if not form.validate():
        return render_template("campaigns/new.html", form=form)

    if (Campaign.query.filter_by(name=form.name.data).first() != None):
        return render_template("campaigns/new.html", form=form, error="Campaign name is already taken")
    
    campaign = Campaign(form.name.data)
    
    db.session().add(campaign)
    db.session().commit()

    return redirect(url_for("campaigns_list"))