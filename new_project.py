import requests
from bs4 import BeautifulSoup

url = 'https://www.x-rates.com/table/?from=USD&amount=1'

r = requests.get( url )

soup = BeautifulSoup(r.content, 'html.parser')

# Extract data from table
table = soup.find('table', class_ = "tablesorter ratesTable")

elements = table.find_all('td')

# Find currency names
nameList = []
usd = []
invusd = []
count = 3
for i in elements:
    if count%3 == 0:
        nameList.append(i)
    elif count%3 == 1:
        usd.append(i)
    elif count%3 == 2:
        invusd.append(i)
    count += 1
    
currencyNames = [ name.text.strip() for name in nameList ]
fromUSD = [ cost.text.strip() for cost in usd ]
toUSD = [ cost.text.strip() for cost in invusd ]

print(currencyNames)
print(fromUSD)
print(toUSD)

