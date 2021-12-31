import requests
from bs4 import BeautifulSoup as bs
import pandas

url = 'https://www.nykaa.com/brands/the-face-shop/c/4290?ptype=brand&id=4290&root=brand_menu,top_brands,The%20Face%20Shop'

req = requests.get(url)
content = req.content
soup = bs(content, 'html.parser')

products = soup.find_all('div', {'class': 'css-d5z3ro'})

product_info = []

for product in products:
    product_dict = {}

    product_dict['Product Name'] = product.find('div', {'class' : 'css-10zjw4o'}).text
    
    product_dict['Product Price'] = product.find('span', {'class' : 'css-18tn768'}).text
    
    try:
      product_dict['Featured Product'] = product.find('li', {'class' : 'custom-tag css-yihg79'}).text
    except AttributeError:
        pass
    
    product_dict['Product Rating'] = product.find('span', {'class' : 'css-c7bg29'}).text

    product_info.append(product_dict)

data = pandas.DataFrame(product_info)
data.to_csv('Products.csv')
