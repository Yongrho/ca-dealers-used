import plotly.express as px
import pandas as pd

df_usedcar = pd.read_csv('ca-dealers-used.csv')
df_usedcar = df_usedcar.drop(['id', 'vin'], axis=1)

#df_usedcar["engine_size"] = pd.to_numeric(df_usedcar["engine_size"])

df_usedcar.loc[df_usedcar['engine_size'] <= 2, 'engine_range'] = 2
df_usedcar.loc[(df_usedcar['engine_size'] > 2) & (df_usedcar['engine_size'] <= 4), 'engine_range'] = 4
df_usedcar.loc[(df_usedcar['engine_size'] > 4) & (df_usedcar['engine_size'] <= 6), 'engine_range'] = 6
df_usedcar.loc[(df_usedcar['engine_size'] > 6) & (df_usedcar['engine_size'] <= 8), 'engine_range'] = 8
df_usedcar.loc[df_usedcar['engine_size'] > 8, 'engine_range'] = 10
print(df_usedcar['engine_size'])
print(df_usedcar['engine_range'])


df_by_type = df_usedcar.groupby(['engine_range']).size().reset_index(name='count')
fig = px.pie(df_by_type, values='count', names='engine_range', title='Proportion of Engine Size')

fig.update_layout(width=1000, height=500, hovermode='x unified', legend_title='Legend')
fig.show()
fig.write_html("canada_usedcar_engine_size.html")