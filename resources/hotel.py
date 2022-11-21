from flask_restful import Resource

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
        