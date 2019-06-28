from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application import app, db, login_required
from application.skills.forms import SkillForm
from application.skills.models import Skill

@app.route("/skills/new", methods=["POST"])
@login_required(role="ADMIN")
def skills_create():
    form = SkillForm(request.form)
    
    if not form.validate():
        return redirect(url_for("admin", form=form, all_skills=Skill.query.all()))
    
    skill = Skill(form.name.data, form.attribute.data, form.difficulty.data, form.description.data)
    
    db.session().add(skill)
    db.session().commit()

    return redirect(url_for("admin", all_skills=Skill.query.all()))