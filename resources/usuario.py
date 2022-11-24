from flask_restful import Resource, reqparse
from models.usuario import UsuarioModel

class User(Resource):
    
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('login', type=str, required=True, help="The field 'login' cannot be left blank.")
    argumentos.add_argument('senha', type=str, required=True, help="The field 'senha' cannot be left blank ")

    def get(self, user_id):
        user = UsuarioModel.find_user(user_id)
        if user:
            return user.json()
        return {'message': 'Unregistered user'}, 404
        
    def delete(self, user_id):
        user = UsuarioModel.find_user(user_id) 
        if user:
            try:
                user.delete_user()
            except:
                return {'message': 'An internal error ocurred trying to delete user'}, 500
            return {'message': 'User deleted.'}
        return {'message': 'Unregistered user'}, 404
    
    
    def cadastro(self):
        pass
    
    def login(self):
        pass
    
    def logout(self): 
        pass






