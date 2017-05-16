from lxml import html
import requests

page = requests.get('https://www.ica.se/butiker/maxi/uppsala/maxi-ica-stormarknad-uppsala-9699/erbjudanden/')
tree = html.fromstring(page.content)

#This will create a list of buyers:
item-name = tree.xpath('//div[@class="item-name"]/text()')
brand = tree.xpath('//div[@class="item-info"]/text()')
price = tree.xpath('//span[@class="item-price"]/text()')



