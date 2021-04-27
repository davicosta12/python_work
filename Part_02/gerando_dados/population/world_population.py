import json

import pygal

from country_codes import get_country_code
from pygal.style import LightColorizedStyle, RotateStyle

# Carrega os dados em uma lista
filename = 'population_data.json'
with open(filename) as f:
    pop_date = json.load(f)

# Exibe a população de cada país em 2010
cc_populations = {}
for pop_dict in pop_date:
    if pop_dict['Year'] == '2010':
        country = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country)
        if code:
            cc_populations[code] = population
        else:
            print("ERROR- ", country)

# Agrupa os países em três níveis populacionais
cc_pops_01, cc_pops_02, cc_pops_03 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_01[cc] = pop
    elif pop < 1000000000:
        cc_pops_02[cc] = pop
    else:
        cc_pops_03[cc] = pop

wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_01)
wm.add('10m-1bn', cc_pops_02)
wm.add('>1bn', cc_pops_03)

wm.render_to_file('world_populations.svg')