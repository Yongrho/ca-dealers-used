import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

df_usedcar = pd.read_csv('ca-dealers-used.csv')
df_usedcar = df_usedcar.dropna(subset=['miles'])

step = (df_usedcar['miles'].max() - df_usedcar['miles'].min()) / 10
#print(step)
step = 20000

df_usedcar.loc[df_usedcar['miles']<= step, 'miles_step']  = step
for i in range(1, 9):
#    print(i, step * i)
    df_usedcar.loc[(df_usedcar['miles'] > step * i) & (df_usedcar['miles'] <= step * (i + 1)), 'miles_step']  = step * i
df_usedcar.loc[df_usedcar['miles'] > step * 10, 'miles_step']  = step * 10

df_by_maker = df_usedcar.groupby(['miles_step']).size().reset_index(name='count')

fig = px.bar(df_by_maker, x='miles_step', y='count',
                title="The miles of used cars from 1981 to 2022", text_auto='.2s')

fig.update_xaxes(title='Miles')
fig.update_yaxes(title='Count')
fig.update_layout(width=1000, height=500, hovermode='x unified', legend_title='Legend')
fig.show()
fig.write_html("canada_usedcar_miles.html")