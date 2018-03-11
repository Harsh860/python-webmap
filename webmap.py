import  folium
import pandas
content=pandas.read_csv("cities.csv")
print(content)
city=content["city"]
lat=content["lat"]
lon=content["lng"]
population=content["pop"]

featuregroup=folium.FeatureGroup(name="population of cities")
i=0
for a,b,c,d in zip(city,lat,lon,population):
    featuregroup.add_child(folium.CircleMarker(location=[b,c],radius = 1,popup=str(d),color='red'))
    

map1 = folium.Map(zoom_start=10, tiles="Mapbox Bright")
map1.add_child(featuregroup)
map1.save("Map1.html")
