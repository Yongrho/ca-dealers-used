from matplotlib.pyplot import sca
import plotly.graph_objects as go
import pandas as pd
from geopy.geocoders import Nominatim
import os

if os.path.isfile('canada_usedcar_city.csv'):
    df_city = pd.read_csv('canada_usedcar_city.csv')
else:
    df_usedcar = pd.read_csv('ca-dealers-used.csv')
    df_usedcar = df_usedcar.drop(['id', 'vin'], axis=1)
    df_usedcar["city"].replace({"Atholeville": "Atholville", 
                                "Bcancour":"Becancour", 
                                "Chteau-richer":"Chateau-Richer",
                                "Chteauguay":"Chateauguay",
                                "Grande-rivire":"Grande-Riviere",
                                "Hrouxville":"Herouxville",
                                "L'piphanie":"L'Epiphanie",
                                "L'tang-du-nord":"L'Etang-du-nord",
                                "Lac-mgantic":"Lac-Megantic",
                                "Llevis":"Levis",
                                "Lvis":"Levis",
                                "Mmontreal":"Montreal",
                                "Mmontreal-est":"Montreal-est",
                                "Mont-jo":"Mont-joli",
                                "Montral":"Montreal",
                                "Montral Nord":"Montreal Nord",
                                "Montral-est":"Montreal-est",
                                "Montral-ouest":"Montreal-ouest",
                                "Montr�al":"Montreal",
                                "Mtabetchouan-lac--la-croix":"Metabetchouan-lac--la-croix",
                                "Paspbiac":"Paspebiac",
                                "Prvost":"Provost",
                                "Qquebec":"Quebec",
                                "Qubec":"Quebec",
                                "Rivire-du-loup":"Riviere-du-loup",
                                "Rivi�re-du-loup":"Riviere-du-loup",
                                "Saint-barthlemy":"Saint-barthelemy",
                                "Saint-csaire":"Saint-cesaire",
                                "Saint-flicien":"Saint-felicien",
                                "Saint-flix-de-kingsey":"Saint-felix-de-kingsey",
                                "Saint-franois-du-lac":"Saint-francois-du-lac",
                                "Saint-jrme":"Saint-jerome",
                                "Saint-laurent-de-l'le-d'orlans":"Saint-Laurent-de-l'Île-d'Orléans",
                                "Saint-lonard-d'aston":"Saint-Léonard-d'Aston",
                                "Saint-phrem-de-beauce":"Saint-Éphrem-de-Beauce",
                                "Saint-rmi":"Saint-Rémi",
                                "Sainte-anne-de-beaupr":"Sainte-Anne-de-Beaupré",
                                "Sainte-anne-de-la-prade":"Sainte-Anne-de-la-Pérade",
                                "Sainte-thrse":"Sainte-Thérèse",
                                "St-jrme":"St-jerome",
                                "St-rmi":"Saint-Rémi",
                                "Ste Thrse":"Sainte-Thérèse",
                                "Tmiscouata Sur Le Lac":"Témiscouata-sur-le-Lac",
                                "Trois-rivires":"Trois-Rivières",
                                "Ttrois-rivieres":"Trois-Rivières",
                                "Unit A14":"Scarborough",
                                "Val Gagn":"Val Gagné",
                                "Valle-jonction":"Vallée-Jonction",
                                "Vancover":"Vancouver",
                                "Greater Lakeburn":"Melanson Settlement",
                                }, 
                                inplace=True)
    df_usedcar.dropna()
    geolocator = Nominatim(user_agent="my_user_agent")
    country ="Canada"

    df_city_size = df_usedcar.groupby(['city']).size()
    df_city = pd.DataFrame(df_city_size, columns=['count'])
    df_city.reset_index(level=0, inplace=True)

    df_city['latitude'] = str(0)
    df_city['longitude'] = str(0)

    for i in range(0, len(df_city)):
        print(i, df_city['city'].iloc[i] + "," + country)
        location = geolocator.geocode(df_city['city'].iloc[i] + "," + country)
        df_city.loc[i, 'latitude'] = str(location.latitude)
        df_city.loc[i, 'longitude'] = str(location.longitude)

#print(df_city.head())
df_city = df_city.sort_values('count', ascending=False)

df_city['text'] = df_city['city'] + '<br>Volume ' + (df_city['count']).astype(str)+' sales'
limits = [(0,2),(3,10),(11,20),(21,100),(100,760)]
colors = ["royalblue","crimson","lightseagreen","orange","deepskyblue"]
cities = []
scale = 20

fig = go.Figure()

for i in range(len(limits)):
    lim = limits[i]
    df_sub = df_city[lim[0]:lim[1]]
    fig.add_trace(go.Scattergeo(
        locationmode = 'country names',
        lon = df_sub['longitude'],
        lat = df_sub['latitude'],
        text = df_sub['text'],
                marker = dict(
            size = df_sub['count']/scale,
            color = colors[i],
            line_color='rgb(40,40,40)',
            line_width=0.5,
            sizemode = 'area'
        ),
        name = '{0} - {1}'.format(lim[0],lim[1])))

fig.update_layout(
        title_text = '1981-2022 Canada used car volume by city <br>(Click legend to toggle traces)',
        geo = dict(
            scope = 'north america',
            landcolor = 'rgb(217, 217, 217)',
            projection = dict(
                scale = 2.3,
            ),
            center = dict(
                lat = 59.132663, 
                lon = -93.309541
            )
        ),
        width=1000,
        height=700
    )

fig.show()
fig.write_html('canada_usedcar_city.html')