import requests

from operator import itemgetter

#Faz uma chamada de API e armazena a resposta
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
response = requests.get(url)
print("Status code:", response.status_code)

# Processa informações sobre cada artido submetido
submission_ids = response.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
  # Cria uma chamada de API separada para cada artido submetido 
  url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
  submission_response = requests.get(url)
  response_dict = submission_response.json()
  
  submission_dict = {
    'title': response_dict['title'],
    'link': 'http://news.ycombinator.com/item?id=' + str(submission_id), 
    'comments': response_dict.get('descendants', 0)
  }
  submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
  print("\nTitle:", submission_dict['title'])
  print("Discussion link:", submission_dict['link'])
  print("Comments:", submission_dict['comments'])