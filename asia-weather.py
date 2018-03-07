import pandas
df=pandas.read_csv("simplemaps-worldcities-basic.csv")
lat=list(df["lat"])
long=list(df["lng"])
city=list(df["city"])

import requests
from bs4 import BeautifulSoup
res=requests.get("https://www.timeanddate.com/weather/?continent=asia")
con=res.content
soup=BeautifulSoup(con,"html.parser")
all=soup.find_all("table",{"class":"zebra fw tb-wt va-m"})
data=all[0].find_all("td",{"class":"rbi"})
j=0
for item in data:
    item.text
res=requests.get("https://www.timeanddate.com/weather/?continent=asia")
con=res.content
soup=BeautifulSoup(con,"html.parser")
all=soup.find_all("table",{"class":"zebra fw tb-wt va-m"})
data2=all[0].find_all("tr")
l=[]
t=0
for item in data2:
    if t==0:
        t+=1
        pass
    else:
        d=item.find_all("td")
        l.append(d[0].text)
        l.append(d[4].text)
states=[]
for i in range(0,len(l)):
    if l[i] in city:
        d={}
        d["city"]=l[i]
        d["lat"]=lat[city.index(l[i])]
        d["long"]=long[city.index(l[i])]
        d["weather"]=data[i].text
    states.append(d)
tf=pandas.DataFrame(states)
tf.to_csv("results.csv",index=False)

bf=pandas.read_csv("results.csv",encoding = "ISO-8859-1")
lat=list(bf["lat"])
lon=list(bf["long"])
w=list(bf["weather"])


import folium

map=folium.Map(location=[38,-99],zoom_start=6,tiles="stamen terrain")

fg=folium.FeatureGroup(name="map")
for lt,ln,el in zip(lat,lon,w): 
    #fg.add_child(folium.Marker(location=[lt,ln],popup=str(w),icon=folium.Icon(color="blue")))
    fg.add_child(folium.Marker(location=[lt,ln],popup=str(el),icon=folium.Icon(color="green",icon='cloud')))
map.add_child(fg)

map.save("asia-weather.html")