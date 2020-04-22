import folium
import pandas as pd
data=pd.read_csv("/Users/gopalkrishnashukla/Downloads/Volcanoes.txt")
print(data)
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])
def color(elevation):
    if elevation<=1000:
        return 'green'
    elif elevation>1000 and elevation<3000:
        return 'orange'
    else:
        return 'red'
map=folium.Map(location=[27,81],zoom_start=6,tiles="Stamen Terrain")
fgv=folium.FeatureGroup("Volcanoes")
for lt,ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup="The Elevation Level is: "+str(el)+" meters.", 
    icon=folium.Icon(color=color(el)), fill_color=color(el), color='gray', fill=True, fill_opacity=0.7))
fgp=folium.FeatureGroup("Population")
fgp.add_child(folium.GeoJson(data=open("/Users/gopalkrishnashukla/Downloads/world.json", "r", encoding="utf-8-sig").read(),
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005'] <=10000000
else 'orange' if 10000000<x['properties']['POP2005']<20000000 else 'red'}))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map.html")
