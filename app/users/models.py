from marshmallow_jsonapi import Schema, fields
from marshmallow import validate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
import datetime


db = SQLAlchemy()


class CRUD():   

    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()   

    def update(self):
        return db.session.commit()

    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()

class Users(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(250), nullable=False)
    lastname = db.Column(db.String(250), nullable=False)
    dob = db.Column(db.Date)
    zipcode = db.Column(db.Integer)

    def __init__(self,  firstname,  lastname, dob, zipcode):

        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.zipcode = zipcode
        
      
           
class UsersSchema(Schema):

    not_blank = validate.Length(min=1, error='Field cannot be blank')
    id = fields.Integer(dump_only=True)
    firstname = fields.String(validate=not_blank)    
    lastname = fields.String(validate=not_blank)
    dob = fields.Date()
    zipcode = fields.Integer()

    #self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/users/"
        else:
            self_link = "/users/{}".format(data['id'])
        return {'self': self_link}
   
    
    class Meta:
        type_ = 'users'
        