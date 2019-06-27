from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class CampaignForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=3, max=40, message="Campaign name must be between 3 and 40 characters long.")])
    starting_points = IntegerField("Starting points", [validators.NumberRange(min=0, max=300, message="Starting point amount must be 0-300.")])

    class Meta:
        csrf = False