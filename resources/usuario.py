from flask_restful import Resource, reqparse
from models.usuario import UserModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from werkzeug.security import hmac
from blacklist import BLACKLIST

argumentos = reqparse.RequestParser()
argumentos.add_argument('login', type=str, required=True, help="The field 'login' cannot be left blank.")
argumentos.add_argument('senha', type=str, required=True, help="The field 'senha' cannot be left blank ")

class User(Resource):
    

    # http://127.0.0.1:5000/usuarios/{user_id}
    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json()
        return {'message': 'Unregistered user'}, 404
    
    # http://127.0.0.1:5000/usuarios/{user_id}
    @jwt_required()
    def delete(self, user_id):
        user = UserModel.find_user(user_id) 
        if user:
            try:
                user.delete_user()
            except:
                return {'message': 'An internal error ocurred trying to delete user'}, 500
            return {'message': 'User deleted.'}
        return {'message': 'Unregistered user'}, 404
    
class UserRegister(Resource):
    #/cadastro
    def post(self):
        dados_usuario = argumentos.parse_args()
        
        if UserModel.find_by_login(dados_usuario['login']):
            return {'message': "The login '{}' already exists".format(dados_usuario['login'])}
        
        user = UserModel(**dados_usuario)
        user.save_user()
        return {'message': "User creaded successfully!"}, 201
        


class UserLogin(Resource):
    
    @classmethod
    def post(cls):
        dados_usuario = argumentos.parse_args()

        user = UserModel.find_by_login(dados_usuario['login'])

        if user and hmac.compare_digest(user.senha, dados_usuario['senha']):
            token_access = create_access_token(identity=user.user_id)
            return {'access_token': token_access}, 200
        return {'message': 'The login or password is incorrect'}, 401
            
            
class UserLogout(Resource):
    
    @jwt_required()
    def post(self):
        jwt_id = get_jwt()['jti']
        BLACKLIST.add(jwt_id)
        return{'message': 'Logged out successfully'}, 200
    
    