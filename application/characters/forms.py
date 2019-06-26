from flask_wtf import FlaskForm
from wtforms import StringField, validators

class CharacterForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=1)])

    class Meta:
        csrf = False