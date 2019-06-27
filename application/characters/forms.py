from flask_wtf import FlaskForm
from wtforms import StringField, validators

class CharacterForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=1, max=30, message="Character name must be between 1 and 30 characters long.")])

    class Meta:
        csrf = False