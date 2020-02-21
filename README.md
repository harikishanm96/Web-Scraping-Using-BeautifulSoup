# Web-Scraping-Using-BeautifulSoup
Web scraping of amazon website product page using beautifulsoup

**DESCRIPTION -** The problem statement is scraping of product details from amazon website(https://amazon.in). 

**INPUT -** Product to be searched and its filters. Here the product is Wrist Watches with filters such as Display- Analogue, Brand Material- Leather, Brands- Titan, Discounts- 25% or more.

**OUTPUT -** Product details such as name and price of the product in an excel sheet and to print the name and price of a single product. 

The following steps will provide you the instructions to get the desired output-  

**STEP1  -** Go to amazon website(https://amazon.in) in any browser of your choice, but here I have used Google Chrome. On the homepage search box, type Wrist Watches. After that in categories section, select the below filter-

Display- Analogue, Brand Material- Leather, Brands- Titan, Discounts- 25% or more.

**STEP2 -** After applying all the filters, the current webpage will be the desired page to scrap from which we have to get the details such as name and price of the product. Press ctrl+shift+I to inspect the webpage and access the HTML code of the particular page. 

In developer tools, select the inspect icon and move the cursor to the name of the product in the webpage. Click on it to get the HTML code. Copy and add the html tag and class in find_all function  of productSearch.py file. Similarly, repeat the same process for price of the product. 

**STEP3 -** Install all the necessary packages using pip through command line. Necessary packages include pandas, requests, beautifulsoup, lxml, regex, openpyxl.

pip installation Commands-

pip install pandas

pip install requests

pip install beautifulsoup4

pip install lxml

pip install regex

pip install openpyxl

**STEP4** - Run the productSearch python file in command line using the command-

python productSearch.py

**STEP5** - Enter the product number of your choice in command line, whose product details are required.

**OUTCOME -** Name and price of the product entered will be displayed in command line and an excel sheet containing name and price of all the products in the page will be generated.
