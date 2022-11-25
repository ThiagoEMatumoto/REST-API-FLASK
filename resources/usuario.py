from flask_restful import Resource, reqparse
from models.usuario import UserModel

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
        






