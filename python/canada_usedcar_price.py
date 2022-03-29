import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

df_usedcar = pd.read_csv('ca-dealers-used.csv')
df_usedcar = df_usedcar.dropna(subset=['price'])

step = (df_usedcar['price'].max() - df_usedcar['price'].min()) / 10
#print(step)
step = 5000

df_usedcar.loc[df_usedcar['price']<= step, 'price_step']  = step
for i in range(1, 9):
#    print(i, step * i)
    df_usedcar.loc[(df_usedcar['price'] > step * i) & (df_usedcar['price'] <= step * (i + 1)), 'price_step']  = step * i
df_usedcar.loc[df_usedcar['price'] > step * 10, 'price_step']  = step * 10

df_by_maker = df_usedcar.groupby(['price_step']).size().reset_index(name='count')

fig = px.bar(df_by_maker, x='price_step', y='count',
                title="The price of used cars from 1981 to 2022", text_auto='.2s')

fig.update_xaxes(title='Price')
fig.update_yaxes(title='Count')
fig.update_layout(width=1000, height=500, hovermode='x unified', legend_title='Legend')
fig.show()
fig.write_html("canada_usedcar_price.html")