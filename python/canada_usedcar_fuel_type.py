import plotly.express as px
import pandas as pd

df_usedcar = pd.read_csv('ca-dealers-used.csv')
df_usedcar = df_usedcar.drop(['id', 'vin'], axis=1)

df_by_type = df_usedcar.groupby(['fuel_type']).size().reset_index(name='count')
fig = px.pie(df_by_type, values='count', names='fuel_type', title='Proportion of Fuel Type')

fig.update_layout(width=1000, height=700, hovermode='x unified', legend_title='Legend')
fig.show()
fig.write_html("canada_usedcar_fuel_type.html")