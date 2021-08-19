import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd

st.set_page_config(layout="wide")
json1= f'nigeria_lga.json'
DATA_URL= f'Night_low.csv'
DATA_URL1= f'Night_moderately_low.csv'
DATA_URL2= f'Nigh_medium_intensity.csv'
DATA_URL3= f'Nigh_moderate_high_intensity.csv'
DATA_URL4= f'Night_high_intensity.csv'


#choice=
select_maps = st.sidebar.selectbox(
    "How do you want to see the map ?",
    ("OpenStreetMap", "Stamen Terrain","Stamen Toner")

)
add_selectbox = st.sidebar.selectbox(
    "How would you like to view the map?",
    ("Low", "moderately low","medium intensity","moderate high intensity","high intensity"))
if add_selectbox == 'Low':
    data = pd.read_csv(DATA_URL)
    st.title('Map of Nigeria')
    def map_g():
        map = folium.Map(location=[data['Latitude'].mean(), data['Longitude'].mean()],tiles=select_maps,attr='My data attribution', zoom_start=6, control_scale=True,)
        tooltip = "Liberty Bell"
        folium.Choropleth(geo_data=json1,name="choropleth",data=data,columns=['NAME_2','Night Light Class'],key_on="feature.properties.NAME_2", fill_color='YlOrRd',
                           fill_opacity=0.7,
                           line_opacity=0.2,
                           legend_name='Night Light Class').add_to(map)
        folium.LayerControl().add_to(map)
        folium.Marker(
    location=[data['Latitude'].mean(), data['Longitude'].mean()],
    popup="Mt. Hood Meadows",
    icon=folium.Icon(icon="cloud"),
).add_to(map)
    #folium.features.GeoJson('nigeria_geojson.geojson',name='States',tooltip =tooltip).add_to(map)
    # Add hover functionality.

    #for index, c in data.iterrows():
        #folium.Marker([c['Latitude'], c['Longitude']], popup=c["LGA"]).add_to(map)
        folium_static(map,width=800, height=500)
    map_g()
if add_selectbox == 'moderately low':
    data1 = pd.read_csv(DATA_URL1)
    st.title('Map of Nigeria')
    def map_g1():
        map = folium.Map(location=[data1['Latitude'].mean(), data1['Longitude'].mean()],tiles=select_maps,attr='My data attribution', zoom_start=6, control_scale=True,)
        tooltip = "Liberty Bell"
        folium.Choropleth(geo_data=json1,name="choropleth",data=data1,columns=['NAME_2','Night Light Class'],key_on="feature.properties.NAME_2", fill_color='YlGnBu',
                           fill_opacity=0.7,
                           line_opacity=0.2,
                           legend_name='Night Light Class').add_to(map)
        folium.LayerControl().add_to(map)
    #folium.features.GeoJson('nigeria_geojson.geojson',name='States',tooltip =tooltip).add_to(map)
    # Add hover functionality.

    #for index, c in data.iterrows():
        #folium.Marker([c['Latitude'], c['Longitude']], popup=c["LGA"]).add_to(map)
        folium_static(map,width=800, height=500)
    map_g1()
if add_selectbox == 'medium intensity':
    data2 = pd.read_csv(DATA_URL2)
    st.title('Map of Nigeria')
    def map_g2():
        map = folium.Map(location=[data2['Latitude'].mean(), data2['Longitude'].mean()],tiles=select_maps,attr='My data attribution', zoom_start=6, control_scale=True,)
        fortooltip = "Liberty Bell"
        folium.Choropleth(geo_data=json1,name="choropleth",data=data2,columns=['NAME_2','Night Light Class'],key_on="feature.properties.NAME_2", fill_color='YlOrRd',
                           fill_opacity=0.7,
                           line_opacity=0.2,
                           legend_name='Night Light Class').add_to(map)
        folium.LayerControl().add_to(map)
    #folium.features.GeoJson('nigeria_geojson.geojson',name='States',tooltip =tooltip).add_to(map)
    # Add hover functionality.

    #for index, c in data.iterrows():
        #folium.Marker([c['Latitude'], c['Longitude']], popup=c["LGA"]).add_to(map)
        folium_static(map,width=800, height=500)
    map_g2()
if add_selectbox == 'moderate high intensity':
    data3 = pd.read_csv(DATA_URL3)
    st.title('Map of Nigeria')
    def map_g3():
        map = folium.Map(location=[data3['Latitude'].mean(), data3['Longitude'].mean()],tiles=select_maps,attr='My data attribution', zoom_start=6, control_scale=True,)
        tooltip = "Liberty Bell"
        folium.Choropleth(geo_data=json1,name="choropleth",data=data3,columns=['NAME_2','Night Light Class'],key_on="feature.properties.NAME_2", fill_color='YlOrRd',
                           fill_opacity=0.7,
                           line_opacity=0.2,
                           legend_name='Night Light Class').add_to(map)
        folium.LayerControl().add_to(map)
    #folium.features.GeoJson('nigeria_geojson.geojson',name='States',tooltip =tooltip).add_to(map)
    # Add hover functionality.

    #for index, c in data.iterrows():
        #folium.Marker([c['Latitude'], c['Longitude']], popup=c["LGA"]).add_to(map)
        folium_static(map,width=800, height=500)
    map_g3()
if add_selectbox == 'high intensity':
    data4 = pd.read_csv(DATA_URL4)
    st.title('Map of Nigeria')
    def map_g4():
        map = folium.Map(location=[data4['Latitude'].mean(), data4['Longitude'].mean()],tiles=select_maps,attr='My data attribution', zoom_start=6, control_scale=True,)
        tooltip = "Liberty Bell"
        folium.Choropleth(geo_data=json1,name="choropleth",data=data4,columns=['NAME_2','Night Light Class'],key_on="feature.properties.NAME_2", fill_color='YlOrRd',
                           fill_opacity=0.7,
                           line_opacity=0.2,
                           legend_name='Night Light Class').add_to(map)
        folium.LayerControl().add_to(map)
    #folium.features.GeoJson('nigeria_geojson.geojson',name='States',tooltip =tooltip).add_to(map)
    # Add hover functionality.

    #for index, c in data.iterrows():
        #folium.Marker([c['Latitude'], c['Longitude']], popup=c["LGA"]).add_to(map)
        folium_static(map,width=800, height=500)
    map_g4()

