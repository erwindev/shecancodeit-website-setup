import datetime
from app import db
from app.model.usermodel import User

class UserDao:
    @staticmethod
    def save_user(user):
        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)
        return user

    @staticmethod
    def update_user(user):
        existing_user = UserDao.get_by_id(user.id)
        if user.firstname:
            existing_user.fistname = user.firstname
        
        if user.lastname:
            existing_user.lastname = user.lastname

        if user.email:
            existing_user.email = user.email

        if user.street:
            existing_user.street = user.street

        if user.city:
            existing_user.city = user.city

        if user.state:
            existing_user.state = user.state                                                

        if user.zipcode:
            existing_user.zipcode = user.zipcode    
            
        db.session.commit()
        db.session.refresh(existing_user)
        return existing_user   

    @staticmethod
    def get_all():
        return User.query.all()

    @staticmethod
    def get_by_id(id):
        return User.query.filter_by(id=id).first()       

    @staticmethod
    def get_by_email(email_data):
        return User.query.filter_by(email=email_data).first()               
