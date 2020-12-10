import requests
from bs4 import BeautifulSoup




url = 'https://forecast.weather.gov/MapClick.php?lat=40.7146&lon=-74.0071#.X9KW_NgzbIU'
url2 ='https://forecast.weather.gov/MapClick.php?lat=34.0116&lon=-118.4923#.X9KkStgzbIU'
page = requests.get(url)
page2 =requests.get(url2)

page.status_code
page2.status_code
soup = BeautifulSoup(page.content,features='html.parser' )
soup2 = BeautifulSoup(page2.content,features='html.parser')
soup.prettify()
soup2.prettify()
def newyork():
    dayTemp =soup.find('p' ,class_="myforecast-current-lrg").text.strip()
    nightTemp =soup.find('p', class_="myforecast-current-sm").text.strip()
    description =soup.find('div' ,id="current_conditions_detail").text.strip()

    print("\nDay Tempreture : ", dayTemp)
    print("Night Tempreture : ", nightTemp)
    print(" Description : \n ", description)
def santaMonica():
    dayTemp = soup2.find('p', class_="myforecast-current-lrg").text.strip()
    nightTemp = soup2.find('p', class_="myforecast-current-sm").text.strip()
    description = soup2.find('div', id="current_conditions_detail").text.strip()

    print("\nDay Tempreture : ",dayTemp)
    print("Night Tempreture : " ,nightTemp)
    print(" Description : \n " ,description)

get = int(input("Choose whether you want : \n 1)NewYork's weather\n 2)SantaMonica's weather \n answer: "))
if(get == 1):
    newyork()
elif(get == 2):
    santaMonica()
else:
    print("please choose 1 or 2 only")










