from matplotlib.pyplot import sca
import plotly.graph_objects as go
import pandas as pd

df_usedcar = pd.read_csv('ca-dealers-used.csv')
df_usedcar = df_usedcar.drop(['id', 'vin'], axis=1)
#print(df.head())
df_state_longlat = pd.read_csv('canada_states_longlat.csv')

df_state_size = df_usedcar.groupby(['state']).size()
df_s = pd.DataFrame(df_state_size, columns=['count'])
df_s.reset_index(level=0, inplace=True)
df = pd.merge(df_state_longlat, df_s, how='inner', on='state')
df = df.sort_values('count', ascending=False)
#print(df)

df['text'] = df['States'] + '<br>Volume ' + (df['count']).astype(str)+' sales'
limits = [(0,1),(1,3),(3,6),(6,9),(9,13)]
colors = ["royalblue","crimson","lightseagreen","orange","deepskyblue"]
cities = []
scale = 20

fig = go.Figure()

for i in range(len(limits)):
    lim = limits[i]
    df_sub = df[lim[0]:lim[1]]
    fig.add_trace(go.Scattergeo(
        locationmode = 'country names',
        lon = df_sub['Longitude'],
        lat = df_sub['Latitude'],
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
        title_text = '1981-2022 Canada used car volume<br>(Click legend to toggle traces)',
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
fig.write_html('canada_usedcar_state.html')