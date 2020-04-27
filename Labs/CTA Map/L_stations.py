# Folium train map


# 15pts - Use folium to plot all of the L train stops in Chicago. Use an appropriate start zoom level.
# 5pts - Add the name to each stop as a popup. Add a train icon to each marker.  Save as an html page in the same folder.
# 3pts  - Color code all of the lines (make the pink line marker pink etc.)
# 2pts - Brown is not a default color name.  See if you can use the documentation for Folium to set a marker color through other means.

# Data set is in this folder, but can be found at: https://data.cityofchicago.org/api/views/8pix-ypme/rows.csv?accessType=DOWNLOAD

# Tricky parts of this one
## The location is in tuple format.  If you have trouble converting it, try this:

import folium
import csv

with open('CTA_-_System_Information_-_List_of__L__Stops (1).csv') as f:
    reader = csv.reader(f)
    data = list(reader)

cta_map = folium.Map(location=[41.8781, -87.6298], zoom_start=11, titles='Stamen Toner')

print(data.pop(0))
lat_longs = [eval(x[-1]) for x in data]
print(lat_longs[0])

for i in range(len(lat_longs)):
    folium.Marker(location=lat_longs[i], popup='<a href="http://fwparker.org">Parker</a>').add_to(cta_map)



my_string = '(41.2, -87.9)'
my_tuple = eval(my_string)
print(my_tuple)
print(type(my_tuple))


cta_map.save('train-map.html')


# If you have extra time, try to put some html into the popup.

