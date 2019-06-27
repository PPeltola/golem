from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required

from application import app, db
from application.characters.models import Character
from application.characters.forms import CharacterForm
from application.campaigns.models import Campaign

@app.route("/campaigns/<campaign_id>/characters/new", methods=["GET", "POST"])
@login_required
def characters_create(campaign_id):
    if request.method == "GET":
        return render_template("characters/new.html", campaign=Campaign.query.get(campaign_id), form=CharacterForm())
    
    form = CharacterForm(request.form)

    if not form.validate():
        return render_template("characters/new.html", campaign=Campaign.query.get(campaign_id), form=CharacterForm())
    
    character = Character(form.name.data)
    character.account_id = current_user.id
    character.campaign_id = campaign_id

    db.session.add(character)
    db.session.commit()

    return redirect(url_for("campaigns_index", campaign_id=campaign_id))

@app.route("/characters/<character_id>", methods=["GET"])
@login_required
def characters_index(character_id):
    character=Character.query.get(character_id)

    if not character:
        return redirect(url_for("characters_list", user_id=current_user.id))

    return render_template("characters/index.html", character=character)

@app.route("/<user_id>/characters/", methods=["GET"])
@login_required
def characters_list(user_id):
    return render_template("characters/list.html",
     active_characters=Character.find_users_characters_sorted_by_campaign_by_status(status=1, user_id=user_id),
     inactive_characters=Character.find_users_characters_sorted_by_campaign_by_status(status=0, user_id=user_id))

@app.route("/characters/<character_id>/deactivate", methods=["POST"])
@login_required
def characters_deactivate(character_id):
    character = Character.query.get(character_id)

    if current_user.get_id() != character.account_id and current_user.get_id() != Campaign.query.get(character.campaign_id).account_id:
        return render_template("characters/index.html", character=Character.query.get(character_id), error="You can't deactivate other players' characters.")

    character.active = False

    db.session().add(character)
    db.session().commit()

    return redirect(url_for("characters_index", character_id=character.id))

@app.route("/characters/<character_id>/activate", methods=["POST"])
@login_required
def characters_activate(character_id):
    character = Character.query.get(character_id)

    if current_user.get_id() != character.account_id and current_user.get_id() != Campaign.query.get(character.campaign_id).account_id:
        return render_template("characters/index.html", character=Character.query.get(character_id), error="You can't activate other players' characters.")

    character.active = True

    db.session().add(character)
    db.session().commit()

    return redirect(url_for("characters_index", character_id=character.id))

@app.route("/characters/<character_id>/delete", methods=["POST"])
@login_required
def characters_delete(character_id):
    character = Character.query.get(character_id)
    print("lol")
    if current_user.get_id() != character.account_id and current_user.get_id() != Campaign.query.get(character.campaign_id).account_id:
        return render_template("characters/index.html", character=Character.query.get(character_id), error="You can't delete other players' characters!")
    
    db.session().delete(character)
    db.session().commit()

    return redirect(url_for("index"))