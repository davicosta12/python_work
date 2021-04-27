import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# preprocess labels here
def f(e):
  if e['label'] is None:
    e['label'] = ""
  return e

# Requests API
def apiRequests(languageName):
  print('\n*******', languageName, '*******')
  url = 'https://api.github.com/search/repositories?q=language:{}&sort=stars'.format(languageName)
  response = requests.get(url)
  print('Status code:',response.status_code)
  response_dict = response.json()
  total_count = response_dict["total_count"]
  repo_dicts = response_dict["items"]
  print('Total de Repositórios:', len(repo_dicts))
  print('Total count:', total_count)

  axios = createdAxios(repo_dicts)
  visualCreat(axios, '{}'.format(languageName))

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