import json

sept_infile = open('US_Fires_9_1.json','r')

sept_outfile = open('bsept_fire_data.json','r')

sept_data = json.load(sept_infile)

json.dump(sept_data, sept_outfile, indent= 4)

slons, slats, sbrightness = [], [], []

for x in sept_data:
    lon = x['longitude']
    lat = x['latitude']
    bright = x['brightness']
    slons.append(lon)
    slats.append(lat)
    if bright > 450:
        sbrightness.append(bright)

from plotly.graphs_objs import Scattergeo, layout
from plotly import offline


data = [{
    'type' : 'scattergeo',
    'lon' : slons,
    'lat' : slats,
    'marker' : {
        'size' : [.05 * bright for bright in sbrightness],
        'color' : sbrightness,
        'colorscale' : 'Viridis',
        'reversescale' : True,
        'colorbar' : {'title' : 'Brightness'}
    }
}]

my_layout = layout(title= 'Fires')

fig = {'data' : data, 'layout' : my_layout}

offline.plot(fig, filename = 'beg_sept_fires.html')

