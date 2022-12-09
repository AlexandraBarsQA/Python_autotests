
import requests
import json


token_insurance = 'a3f1f7e29076fc6ecc4f3b49c7ee8e71c605a37c'


'''Получение токена'''

response_post = requests.post('https://partner.agentapp.ru/v1/users/obtain-token', json={
  
    "username": "qa@qa.qa",
    "password": "111"
})

print(response_post.text)


'''Создание водителя'''

response_driver = requests.post('https://partner.agentapp.ru/v1/insured_objects/drivers', headers={'Authorization' : f'Token {token_insurance}'}, json={
  
  "first_name": "Алексей",
  "last_name": "Алексеев",
  "patronymic": "Алексеевич",
  "birth_date": "1990-01-01",
  "driving_experience_started": "2010-10-10",
  "driver_licenses": [
    {
      "credential_type": "DRIVER_LICENSE",
      "number": "012345",
      "series": "9767",
      "issue_date": "2010-10-10"
    }
  ]
})

print(response_driver.text)