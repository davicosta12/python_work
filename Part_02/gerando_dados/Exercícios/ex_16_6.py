import json
import pygal
from pygal.style import LightColorizedStyle, RotateStyle
from country_codes import get_country_code

filename = 'pib_world.json'
with open(filename) as f:
    pib_date = json.load(f)

world_pib = {}
for pib_dict in pib_date:
    if pib_dict['Year'] == 2016:
        country = pib_dict['Country Name']
        code = get_country_code(country)
        pib = pib_dict['Value']
        if code:
            world_pib[code] = pib
        else:
            print("ERROR - ", country)

cc_pops_01, cc_pops_02, cc_pops_03 = {}, {}, {}
for cc, pop in world_pib.items():
    if pop < 100000000000:
        cc_pops_01[cc] = pop
    elif pop < 10000000000000:
        cc_pops_02[cc] = pop
    else:
        cc_pops_03[cc] = pop

wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World PIB in 2016, by Country'
wm.add('0-100b', cc_pops_01)
wm.add('100b-10tn', cc_pops_02)
wm.add('>10tn', cc_pops_03)


wm.render_to_file('world_pib.svg')



