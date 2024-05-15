import requests
from bs4 import BeautifulSoup

url = 'https://www.leagueoflegends.com/en-us/news/game-updates/'

r = requests.get( url )

soup = BeautifulSoup(r.content, 'html.parser')

patchnotes = soup.find_all( 'li' , class_ = "style__Item-sc-106zuld-3 fWsPDo" )[0]

note_url = patchnotes.find( 'a' )['href']

print(note_url)