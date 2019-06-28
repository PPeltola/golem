from application import app, db

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

    attribute = db.Column(db.String(5), nullable=False)
    difficulty = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(144), nullable=False)

    def __init__(self, name, attribute, difficulty, description):
        self.name = name
        self.attribute = attribute
        self.difficulty = difficulty
        self.description = description