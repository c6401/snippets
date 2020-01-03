import folium

m = folium.Map(location=[55.75, 37.61])
folium.Marker([55.75, 37.61], popup='...', tooltip='...').add_to(m)
