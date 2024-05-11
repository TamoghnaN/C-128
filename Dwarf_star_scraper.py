from bs4 import BeautifulSoup as bs4
import requests
import pandas as pd

star_url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(star_url)

soup = bs4(page.text,"html.parser")

table = soup.find_all('table',{"class":"wikitable sortable"})

temp = []

tRows = table[1].find_all('tr')

for tr in tRows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp.append(row)
Star_names = []
Distance = []
Mass = []
Radius = []

for i in range(1,len(temp)):
    Star_names.append(temp[i][0])
    Distance.append(temp[i][5])
    Mass.append(temp[i][7])
    Radius.append(temp[i][8])
headers = ['Star_names','Distance','Mass','Radius']
data = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius)),columns=['Star_names','Distance','Mass','Radius'])

data.to_csv('dwarf_star_data.csv',index = True, index_label="id")