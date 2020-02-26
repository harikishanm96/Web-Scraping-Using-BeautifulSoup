#Importing all the necessary packages
import requests
from bs4 import BeautifulSoup
from openpyxl.workbook import Workbook
import pandas as pd
import re

#To set the working directory to store the output excel file
import os
os.chdir(".\Desktop")

#User agent for http request
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}

#Sending the request to desired amazon product(Wrist watches) page
url = 'https://www.amazon.in/s?k=wrist+watches&i=watches&bbn=1350387031&rh=n%3A1350387031%2Cp_n_feature_seven_browse-bin%3A1480900031%2Cp_n_material_browse%3A1480907031%2Cp_89%3ATitan%2Cp_n_pct-off-with-tax%3A2665400031&dc&qid=1581835207&rnid=2665398031&ref=sr_nr_p_n_pct-off-with-tax_2'
response = requests.get(url,headers=headers)

#Loading the scraped HTML markup into BeautifulSoup
soup = BeautifulSoup(response.text, "lxml")

#Finding the name of the product using find_all function of BeautifulSoup
#Name is stored in span tag with class="a-size-base-plus a-color-base a-text-normal"
name1 = soup.find_all('span', class_="a-size-base-plus a-color-base a-text-normal")
name2 = str(name1) #Casting to a string to use regular expression  

#Finding the final price of the product using find_all function of BeautifulSoup
#Final price is stored in span tag with class="a-price-whole"
price1 = soup.find_all('span', class_ = "a-price-whole")
price2 = str(price1)

#Regular expression function to remove tags
def cleanhtml(html_input):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', html_input)
    return cleantext

#Calling the regular expression function
name3 = cleanhtml(name2)
name = name3.split(',') #Splitting the string into a list of strings 

price3 = cleanhtml(price2)
price = price3.split(' ')

jsonObject = {'name': name, 'price': price}

#Creating an array of objects with name as key and price as value
pairs = {}
newArr = []
for i in range(0, len(name)):
    pairs[name[i]] = price[i]
    newArr.append(pairs)
    pairs={}

#Using pandas, the json output is converted to a pandas DataFrame and fed to a excel sheet
df = pd.DataFrame(data=jsonObject, columns=["name", "price"])
df.to_excel("name_and_price.xlsx") 



#Method to print n-th product

#Enter the product number whose name and title is needed
product = int(input('Enter the product number: '))

#Will output the name and price of product, if within range of total number of products available
if(product < len(newArr)):
    print(newArr[product])
else:
    print('Product not Found')



