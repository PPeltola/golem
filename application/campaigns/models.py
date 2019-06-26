from application import db
from sqlalchemy.sql import text

class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    related_charaters = db.relationship("Character", backref="campaign", lazy=True)

    def __init__(self, name):
        self.name = name
    
    @staticmethod
    def find_campaigns_owned_by_user(user_id):
        stmt = text("SELECT * FROM Campaign"
                    " WHERE account_id = :id").params(id=user_id)

        res = db.engine.execute(stmt)

        ret = []

        for row in res:
            ret.append({"id":row[0], "name":row[1]})
        
        return ret