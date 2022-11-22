from flask_restful import Resource, reqparse

hoteis = [
    {
        'hotel_id': 'alpha',
        'nome': 'Alpha Hotel',
        'estrelas': 4.7,
        'diaria': 150,
        'cidade': 'Mogi das Cruzes'
    },
    {
        'hotel_id': 'beta',
        'nome': 'Beta Hotel',
        'estrelas': 3.5,
        'diaria': 30,
        'cidade': 'Rio de Janeiro' 
    },
    {
        'hotel_id': 'gama',
        'nome': 'Gama Hotel',
        'estrelas': 6.5,
        'diaria': 270,
        'cidade': 'São Paulo'
    }
]
class Hoteis(Resource): 
    def get(self):
        return {'hoteis': hoteis}

class Hotel(Resource):
    
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return {'message': 'Hotel not found.'}, 404 
    
    def post(self, hotel_id):
        
        #selecionar os argumentos passados no json e colocar em uma variavel
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('nome')
        argumentos.add_argument('estrelas')
        argumentos.add_argument('diaria')
        argumentos.add_argument('cidade')
        
        #passando os valores para outra variável
        dados = argumentos.parse_args()
        
        #formando um novo hotel
        new_hotel = {
            'hotel_id': hotel_id,
            'nome': dados['nome'],
            'estrelas': dados['estrelas'],
            'diaria': dados['diaria'],
            'cidade': dados['cidade']
        }
        
        #adicionando o hotel na lista de hoteis
        hoteis.append(new_hotel)
        
        #devolve o novo hotel caso de 200
        return new_hotel, 200
        
    def put(self, hotel_id):
        pass
    
    def delete(self, hotel_id):
        pass
    
    
    