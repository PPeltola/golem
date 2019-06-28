from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class SkillForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=3, max=30, message="Skill name must be between 3 and 30 characters long.")])
    attribute = StringField("Attribute")
    difficulty = IntegerField("Difficulty", [validators.NumberRange(min=1, max=8, message="Difficulty must be between 1 and 8.")])
    description = StringField("Description", [validators.Length(min=0, max=144, message="Description must be between 0 and 144 characters long.")])
    
    class Meta:
        csrf = False