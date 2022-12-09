import requests
import pytest


trainer_id = '1247'


'''Тест первый'''

def test_status_code():
  response = requests.get('https://pokemonbattle.me:5000/trainers')
  assert response.status_code == 200


'''Тест второй'''

def test_part_body():
  response = requests.get('https://pokemonbattle.me:5000/trainers', params = {'trainer_id' : '1247'})
  assert response.json() ['trainer_name'] == 'Aleksandra_coach'


'''Тест третий'''

def test_name_body():
  response = requests.get('https://pokemonbattle.me:5000/pokemons', params = {'pokemon_id' : '1491'})
  assert response.json() ['name'] == 'заврачик-барсик'


  '''Тест четвертый'''

def test_status_body():
  response = requests.get('https://pokemonbattle.me:5000/pokemons', params = {'pokemon_id' : '1492'})
  assert response.json() ['status'] == '1'

