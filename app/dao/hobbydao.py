import datetime
from app import db
from app.model.hobbymodel import Hobby

class HobbyDao:
    @staticmethod
    def save_hobby(hobby):
        db.session.add(hobby)
        db.session.commit()
        db.session.refresh(hobby)
        return hobby

    @staticmethod
    def update_hobby(hobby):
        existing_hobby = HobbyDao.get_by_id(hobby.id)
        if hobby.name:
            existing_hobby.name = hobby.name        
            
        db.session.commit()
        db.session.refresh(existing_hobby)
        return existing_hobby   

    @staticmethod
    def get_all():
        return Hobby.query.all()

    @staticmethod
    def get_hobby_by_userid(userid):
        return Hobby.query.filter_by(user_id=userid).all()
      
