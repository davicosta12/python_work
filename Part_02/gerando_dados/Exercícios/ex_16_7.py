import csv
import pygal
from pygal.style import LightColorizedStyle, RotateStyle
from country_codes import get_country_code


pop_rural_porcent = {}
filename = 'pop_rural.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        country = row[0]
        porcent = float(row[-1])
        code = get_country_code(country)

        if code == None or porcent == '':
            print(country + " missing data!")
        else:
            pop_rural_porcent[code] = porcent


cc_pops_01, cc_pops_02, cc_pops_03, cc_pops_04, cc_pops_05 = {}, {}, {}, {}, {}
for cc, porcent in pop_rural_porcent.items():
    if porcent < 14.56:
        cc_pops_01[cc] = porcent
    elif porcent < 26.81:
        cc_pops_02[cc] = porcent
    elif porcent < 38.77:
        cc_pops_03[cc] = porcent
    elif porcent < 52.85:
        cc_pops_04[cc] = porcent
    else:
        cc_pops_05[cc] = porcent

wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Rural Population in 2019, by Country'
wm.add('< 14.56', cc_pops_01)
wm.add('14.56-26.81', cc_pops_02)
wm.add('26.81-38.77', cc_pops_03)
wm.add('38.77-52.85', cc_pops_03)
wm.add('>52.85', cc_pops_03)


wm.render_to_file('world_rural_porcent.svg')


