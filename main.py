import requests
import time
import json


#Help parse some of the information we are dealing with. 
from bs4 import BeautifulSoup



userInput = input("Please Enter The url you want to monitor: ")


while True:

    #This is going to extract the information in the page. 
    html = requests.get(userInput)

    #this is going to help us better find information in the request. 
    parse = BeautifulSoup(html.text,'html.parser')

    # print(parse)

    # print('THis is the parse info ending')


    finding = parse.find(name='script',
    
         id=lambda x: x and x.startswith("product-"))

    # print('now')
    # print(finding.text)

    #Convert the information into json format. (What is the difference between loads and load? )
    info = json.loads(finding.text)



    #Since our json returns a dictonary -> this is only going to print out the keys. 
    # for small in info:
    #     print(small)

    print("Size ---- Instock")
    print('\n') 

    for variant in info['variants']:
        # print(variant)
        print(variant['title'],'->', variant['available'])

    print('\n')
    #Default loop -> only checks every 5 seconds
    time.sleep(10)