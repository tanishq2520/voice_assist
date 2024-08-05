import requests
from ss import *

api_address="http://newsapi.org/v2/top-headlines?country=in&apiKey="+key
json_data=requests.get(api_address).json()

arr=[]

def news():
    for i in range(3):
        arr.append("Number "+str(i+1)+"--> " + json_data['articles'][i]['title']+".")

    return arr


