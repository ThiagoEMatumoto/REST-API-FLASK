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
        return {'hoteis': hoteis}

class Hotel(Resource):
    
    #selecionar os argumentos passados no json e colocar em uma variavel
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return False

    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel
        return {'message': 'Hotel not found.'}, 404 

    def post(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        obj_hotel = HotelModel(hotel_id, **dados)
        hoteis.append(obj_hotel.json())
        return obj_hotel.json(), 201 

    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        obj_hotel = HotelModel(hotel_id, **dados)
        new_hotel = obj_hotel.json()
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hotel.update(obj_hotel.json())
            return hotel, 200
        hoteis.append(obj_hotel.json())
        return obj_hotel.json(), 201

    def delete(self, hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        return {'message': 'Hotel deleted.'}