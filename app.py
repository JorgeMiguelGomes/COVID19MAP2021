#Import Libraries

import pandas as pd
import plotly.express as px
import plotly.io as pio 

# Import Configuration File with your mapbox access token


import config 


#Setup Mapbox Token

px.set_mapbox_access_token(config.mapbox_token)

# Import CSV file 

df  = pd.read_csv('bubbleslongclean.csv') 

# Plot the map 

fig = px.scatter_mapbox(df, lat="LAT", lon="LONG", color="INC", size="INC",
                        animation_frame = 'DATA', animation_group = 'INC',
                        mapbox_style='dark',
                        color_continuous_scale=px.colors.sequential.Inferno,
                        range_color =(0,9000), # closed issue #1 
                        size_max=60, 
                        hover_name='CONCELHO', 
                        hover_data = ['DATA', 'CONCELHO', 'INC'], 
                        title = 'COVID-19 EM PORTUGAL')

# Update the layout 

fig.update_layout(font_size=16,
    				      title={'xanchor': 'center','yanchor': 'top', 'y':0.2, 'x':0.5,}, 
            		  title_font_size = 54,
            		  mapbox_style = "mapbox://styles/vostpt/cko3z46ny0qm817qsgr6a516d")

# Write to HTML file 

pio.write_html(fig, file="index.html", auto_open=True)









