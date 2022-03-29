import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

df_usedcar = pd.read_csv('ca-dealers-used.csv')
df_usedcar = df_usedcar.drop(['id', 'vin'], axis=1)

df_by_maker = df_usedcar.groupby(['make']).size().reset_index(name='count')
df_by_maker = df_by_maker.sort_values('count', ascending=False)
#print(df_by_maker)

fig = px.bar(df_by_maker, x='make', y='count',
                title="The sales of used cars from 1981 to 2022 by maker", text_auto='.2s')

fig.update_yaxes(title='The sales of used cars')
fig.update_layout(width=1000, height=500, hovermode='x unified', legend_title='Legend')
fig.show()
fig.write_html("canada_usedcar_maker.html")