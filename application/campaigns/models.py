from application import db
from sqlalchemy.sql import text

class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    related_charaters = db.relationship("Character", backref="campaign", lazy=True)

    starting_points = db.Column(db.Integer, nullable=False)

    def __init__(self, name, starting_points):
        self.name = name
        self.starting_points = starting_points
    
    @staticmethod
    def find_campaigns_owned_by_user(user_id):
        stmt = text("SELECT * FROM Campaign"
                    " WHERE account_id = :id").params(id=user_id)

        res = db.engine.execute(stmt)

        ret = []

        for row in res:
            ret.append({"id":row[0], "name":row[1]})
        
        return ret
    
    @staticmethod
    def count_active_characters_in_users_campaigns(user_id):
        stmt = text("SELECT Campaign.id, COUNT(Character.id) FROM Campaign"
                    " LEFT JOIN Character ON Character.campaign_id = Campaign.id"
                    " WHERE Campaign.account_id = :id"
                    " GROUP BY Campaign.id").params(id=user_id)

        res = db.engine.execute(stmt)

        ret = {}

        for row in res:
            ret[row[0]] = row[1]
        
        return ret