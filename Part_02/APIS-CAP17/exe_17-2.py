import requests
import pygal

from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
from operator import itemgetter

# Cria lista dos eixos    
def createdAxios(repo_dicts):
  names, plot_dicts = [], []
  for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
      'value': repo_dict['stargazers_count'],
      'label': repo_dict['description'],
      'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)
  return {'names': names, 'plot_dicts': plot_dicts}

# Cria a visualização
def visualCreat(axios, languageName):
  my_style = LS('#333366', base_style=LCS)
  my_config = pygal.Config()
  my_config.x_label_rotation = 45
  my_config.show_legend = False
  my_config.title_font_size = 24
  my_config.label_font_size = 14
  my_config.major_label_font_size = 18
  my_config.truncate_label = 15
  my_config.show_y_guides = False
  my_config.width = 1000

  chart = pygal.Bar(my_config, style=my_style)
  chart.title = 'Most-Starred {} Projects on GitHub'.format(languageName)
  chart.x_labels = axios['names']

  plot_dicts = list(map(f, axios['plot_dicts']))

  chart.add('', plot_dicts)
  chart.render_to_file('{}.svg'.format(languageName))

#Faz uma chamada de API e armazena a resposta
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
response = requests.get(url)
print("Status code:", response.status_code)

# Processa informações sobre cada artido submetido
submission_ids = response.json()
submission_dicts = []
titles = []

for submission_id in submission_ids[:30]:
  # Cria uma chamada de API separada para cada artido submetido 
  url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
  submission_response = requests.get(url)
  response_dict = submission_response.json()

  titles.append(response_dict['title'])
  submission_dict = {
    'label': response_dict['title'],
    'xlink': 'http://news.ycombinator.com/item?id=' + str(submission_id), 
    'value': response_dict.get('descendants', 0)
  }
  submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('value'), reverse=True)

# Cria a visualização
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Comments Hacker News article'
chart.x_labels = titles

chart.add('', submission_dicts)
chart.render_to_file('exe_17-2.svg')