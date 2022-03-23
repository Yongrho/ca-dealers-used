import plotly.express as px
import pandas as pd

df_usedcar = pd.read_csv('ca-dealers-used.csv')
df_usedcar = df_usedcar.drop(['id', 'vin'], axis=1)

df_by_type = df_usedcar.groupby(['body_type']).size().reset_index(name='count')
fig = px.pie(df_by_type, values='count', names='body_type', title='Proportion of Body Type')

fig.update_layout(width=1000, height=800, hovermode='x unified', legend_title='Legend')
fig.show()
fig.write_html("canada_usedcar_body_type.html")