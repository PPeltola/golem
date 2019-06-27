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
    
    character = Character(form.name.data, Campaign.query.get(campaign_id).starting_points)
    character.account_id = current_user.id
    character.campaign_id = campaign_id

    db.session.add(character)
    db.session.commit()

    return redirect(url_for("characters_index", character_id=character.id))

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
    
    if current_user.get_id() != character.account_id and current_user.get_id() != Campaign.query.get(character.campaign_id).account_id:
        return render_template("characters/index.html", character=Character.query.get(character_id), error="You can't delete other players' characters!")
    
    db.session().delete(character)
    db.session().commit()

    return redirect(url_for("index"))

@app.route("/characters/<character_id>/modify/<attribute>/<way>", methods=["POST"])
@login_required
def characters_modify(character_id, attribute, way):
    character = Character.query.get(character_id)
    error = ""
    
    if current_user.get_id() != character.account_id and current_user.get_id() != Campaign.query.get(character.campaign_id).account_id:
        return render_template("characters/index.html", character=character, error="You can't modify other players' characters.")
    
    if attribute == "ST":
        if way == "1":
            if character.unspent_points < 10:
                error="Insufficient points."
            elif character.strength >= 20:
                error="You are already at maximum ST."
            else:
                character.unspent_points -= 10
                character.strength_spent += 10
                character.strength += 1
        else:
            if character.strength <= 7:
                error="You are already at minimum ST."
            else:
                character.unspent_points += 10
                character.strength_spent -= 10
                character.strength -= 1
    elif attribute == "DX":
        if way == "1":
            if character.unspent_points < 20:
                error="Insufficient points."
            elif character.dexterity >= 16:
                error="You are already at maximum DX."
            else:
                character.unspent_points -= 20
                character.dexterity_spent += 20
                character.dexterity += 1
        else:
            if character.dexterity <= 7:
                error="You are already at minimum DX."
            else:
                character.unspent_points += 20
                character.dexterity_spent -= 20
                character.dexterity -= 1
    elif attribute == "IQ":
        if way == "1":
            if character.unspent_points < 20:
                error="Insufficient points."
            elif character.intelligence >= 16:
                error="You are already at maximum IQ."
            else:
                character.unspent_points -= 20
                character.intelligence_spent += 20
                character.intelligence += 1
        else:
            if character.intelligence <= 7:
                error="You are already at minimum IQ."
            else:
                character.unspent_points += 20
                character.intelligence_spent -= 20
                character.intelligence -= 1
    elif attribute == "HT":
        if way == "1":
            if character.unspent_points < 10:
                error="Insufficient points."
            elif character.health >= 18:
                error="You are already at maximum HT."
            else:
                character.unspent_points -= 10
                character.health_spent += 10
                character.health += 1
        else:
            if character.health <= 7:
                error="You are already at minimum HT."
            else:
                character.unspent_points += 10
                character.health_spent -= 10
                character.health -= 1
    else:
        error="Invalid attribute."
    
    if len(error) > 0:
        return render_template("characters/index.html", character=character, error=error)

    db.session().add(character)
    db.session().commit()

    return render_template("characters/index.html", character=character)