import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.arthur-conan-doyle.com/index.php/The_Story_of_Spedegue%27s_Dropper'
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")  
lst_links = []
lst_links_jpg = []
for link in soup.find_all('a'):
	lst_links.append(link.get('href'))
	#if '.jpg' in link.get('href'):
	#	lst_links_jpg.append(link.get('href'))

print(len(lst_links_jpg))