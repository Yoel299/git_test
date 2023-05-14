import requests
from bs4 import BeautifulSoup

url = 'https://www.geeksforgeeks.org/python-programming-language/'

r = requests.get( url )

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

""" finding elements by class """
# s = soup.find('div', class_='entry-content')

# p_content = s.find_all('p')

# # Removing tags from content
# for line in p_content:
#     print(line.text)

""" finding elements by id """
# s = soup.find('div', id= 'main')
 
# # Getting the leftbar
# leftbar = s.find('ul', class_='leftBarList')
 
# # All the li under the above ul
# li_content = leftbar.find_all('li')

# # Removing tags from content
# for line in li_content:
#     print(line.text)

""" find all the anchor tags with 'href' """
# for link in soup.find_all('a'):
#     print(link.get('href'))