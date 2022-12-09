import requests
import json


token = '84531164dd4b745c244efa5c1c27f349'


'''Запрос первый'''

response = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
  "name": "барс-1",
  "photo": "https://avatanplus.com/files/resources/mid/582613409029415854bb344e.png"
})

print(response.text)


'''Запрос второй'''

response_put = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "pokemon_id": 1491,
    "name": "заврачик-барсик",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
})

print(response_put.text)


'''Запрос третий'''

response = requests.post('https://pokemonbattle.me:5000/trainers/addPokebol', headers={'trainer_token' : token}, json={
  "pokemon_id": "1491"
}) 

print(response.text)

