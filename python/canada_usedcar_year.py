import plotly.express as px
import pandas as pd

df_usedcar = pd.read_csv('ca-dealers-used.csv')
df_usedcar = df_usedcar.drop(['id', 'vin'], axis=1)

df_by_year = df_usedcar.groupby(['year']).size().reset_index(name='count')
#print(df_by_year)

fig = px.line(df_by_year, x='year', y='count',
                title='The sales of used cars from 1981 to 2022')

fig.update_traces(mode="markers+lines", hovertemplate=None)
fig.update_yaxes(title='The sales of used cars')
fig.update_layout(width=1000, height=500, hovermode='x unified', legend_title='Legend')
fig.show()
fig.write_html("canada_usedcar_year.html")