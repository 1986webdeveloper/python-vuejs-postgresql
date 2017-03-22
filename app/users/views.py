from flask import Blueprint, request, jsonify, make_response
from app.users.models import Users, UsersSchema, db
from flask_restful import Api, Resource

 
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import ValidationError

users = Blueprint('users', __name__)

schema = UsersSchema()
api = Api(users)

# Users
class UsersList(Resource):
    
    def get(self):
        users_query = Users.query.all()
        results = schema.dump(users_query, many=True).data
        return results
    
    def post(self):
        raw_dict = request.get_json(force=True)
        try:
                schema.validate(raw_dict)
                user_dict = raw_dict['data']['attributes']
                user = Users(user_dict['firstname'], user_dict['lastname'], user_dict['dob'], user_dict['zipcode'])
                user.add(user)            
                query = Users.query.get(user.id)
                results = schema.dump(query).data                
                return results, 201
            
        except ValidationError as err:
                resp = jsonify({"error": err.messages})
                resp.status_code = 403
                return resp               
                
        except SQLAlchemyError as e:
                db.session.rollback()
                resp = jsonify({"error": str(e)})
                resp.status_code = 403
                return resp



class UsersUpdate(Resource):
    
    
    def get(self, id):
        user_query = Users.query.get_or_404(id)
        result = schema.dump(user_query).data
        return result
        
    
    def put(self, id):
        user = Users.query.get_or_404(id)
        raw_dict = request.get_json(force=True)
        
        try:
            schema.validate(raw_dict)
            user_dict = raw_dict['data']['attributes']
            for key, value in user_dict.items():
                
                setattr(user, key, value)
          
            user.update()            
            return self.get(id)
            
        except ValidationError as err:
                resp = jsonify({"error": err.messages})
                resp.status_code = 401
                return resp               
                
        except SQLAlchemyError as e:
                db.session.rollback()
                resp = jsonify({"error": str(e)})
                resp.status_code = 401
                return resp
         
    def delete(self, id):
        user = Users.query.get_or_404(id)
        try:
            delete = user.delete(user)
            response = make_response()
            response.status_code = 204
            return response
            
        except SQLAlchemyError as e:
                db.session.rollback()
                resp = jsonify({"error": str(e)})
                resp.status_code = 401
                return resp
        

api.add_resource(UsersList, '.json')
api.add_resource(UsersUpdate, '/<int:id>.json')