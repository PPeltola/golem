from flask_wtf import FlaskForm
from wtforms import StringField

class CampaignForm(FlaskForm):
    name = StringField("Name")

    class Meta:
        csrf = False