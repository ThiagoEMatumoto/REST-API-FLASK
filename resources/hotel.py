from flask_restful import Resource, reqparse
from models.hotel import HotelModel

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
        return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]}

class Hotel(Resource):
    
    #selecionar os argumentos passados no json e colocar em uma variavel
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True, help="The field 'nome' cannot bt left blank.")
    argumentos.add_argument('estrelas', type=float, required=True, help="The field 'estrelas' cannot bt left blank.")
    argumentos.add_argument('diaria', type=float, required=True, help="The field 'diaria' cannot bt left blank.")
    argumentos.add_argument('cidade', type=str, required=True, help="The field 'cidade' cannot bt left blank.")
    
    
    
    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()
        return {'message': 'Hotel not found.'}, 404 
    
    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {'message': "Hotel id '{}' already exists".format(hotel_id)}, 400
        dados = Hotel.argumentos.parse_args()
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except:
            return {'message': 'An internal error ocurred trying to save hotel'}, 500
        return hotel.json()
        
        
    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        hotel_encontrado = HotelModel.find_hotel(hotel_id)
        if hotel_encontrado:
            hotel_encontrado.update_hotel(**dados)
            hotel_encontrado.save_hotel()
            return hotel_encontrado.json(), 200
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except:
            return {'message': 'An internal error ocurred trying to save hotel'}, 500
        return hotel.json(), 201
    
    
    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            try:
                hotel.delete_hotel()
            except:
                return {'message': 'An internal error ocurred trying to delete hotel'}, 500
            return {'message': 'Hotel deleted.'}
        return {'message': 'Hotel not found'}, 404
    
    