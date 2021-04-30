#Import Libraries

import pandas as pd
import plotly.express as px
import chart_studio 
import chart_studio.plotly as py

import config 


#Setup Mapbox Token

px.set_mapbox_access_token(config.mapbox_token)

df  = pd.read_csv('bubbleslongclean.csv') 

point = dict(lat='')

fig = px.scatter_mapbox(df, lat="LAT", lon="LONG", color="INC", size="INC",
				animation_frame = 'DATA', animation_group = 'INC',
				mapbox_style='dark',
                  #color_continuous_scale=px.colors.cyclical.Twilight, 
                  color_continuous_scale=px.colors.sequential.Inferno,
                  size_max=60, 
                  hover_name='CONCELHO', 
                  hover_data = ['DATA', 'CONCELHO', 'INC'], 
                  title = 'COVID-19 EM PORTUGAL')

fig.update_layout(font_size=16,
				  title={'xanchor': 'center','yanchor': 'top', 'y':0.2, 'x':0.5,}, 
        		  title_font_size = 54,
        		  mapbox_style = "mapbox://styles/vostpt/cko3z46ny0qm817qsgr6a516d")


fig.show()







