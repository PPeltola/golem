from application import db
from sqlalchemy.sql import text

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False)
    active = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'), nullable=False)

    def __init__(self, name):
        self.name = name
        self.active = True
    
    @staticmethod
    def find_users_characters_sorted_by_campaign_by_status(status, user_id):
        stmt = text("SELECT Campaign.id, Campaign.name, Character.id, Character.name FROM Character"
                    " LEFT JOIN Campaign ON Campaign.id = Character.campaign_id"
                    " WHERE (Character.active = :status AND Character.account_id = :id)").params(status=status, id=user_id)
        
        res = db.engine.execute(stmt)

        ret = {}

        for row in res:
            if (row[0], row[1]) in ret:
                ret[(row[0], row[1])][row[2]] = row[3]
            else:
                ret[(row[0], row[1])] = {row[2]: row[3]}
        
        return ret
    
    @staticmethod
    def find_users_characters_in_campaign_by_status(status, user_id, campaign_id):
        stmt = text("SELECT Character.id, Character.name FROM Character"
                    " WHERE (Character.active = :status AND Character.account_id = :userid AND Character.campaign_id = :campaignid)").params(status=status, userid=user_id, campaignid = campaign_id)
        
        res = db.engine.execute(stmt)

        ret = {}

        for row in res:
            ret[row[0]] = row[1]
        
        return ret
    
    @staticmethod
    def find_all_characters_in_campaign_by_status(status, campaign_id):
        stmt = text("SELECT Character.id, Character.name FROM Character"
                    " WHERE (Character.active = :status AND Character.campaign_id = :campaignid)").params(status=status, campaignid=campaign_id)
        
        res = db.engine.execute(stmt)

        ret = {}

        for row in res:
            ret[row[0]] = row[1]
        
        return ret