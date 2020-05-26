from app import db
from datetime import datetime

class Hobby(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    user = db.relationship("User")

    def __repr__(self):
        return '<User {}>'.format(self.email)

    def to_json(self):
        json_result = {
            'id': self.id,
            'name': self.name,    
            'user_id': self.user_id,                                        
            'create_date': self.create_date
        }
        return json_result        
