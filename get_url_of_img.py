import requests
from bs4 import BeautifulSoup
import re

url_base = 'https://www.arthur-conan-doyle.com/'
url_story = 'index.php/The_Story_of_Spedegue%27s_Dropper'
url = url_base + url_story

# get all the links to the images from story's main website
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")  
lst_links = []
lst_links_jpg = []
for link in soup.find_all('a'):
	lst_links.append(link.get('href'))
	if not(link.get('href') is None):
		if re.search(r'.jpg', link.get('href')):
			if link.get('href') not in lst_links_jpg:
				lst_links_jpg.append(url_base + link.get('href'))

# the links obtained above end in .jpg but do not actually lead to the images
# this requires another iteration , now filtering on the word images in the url
lst_links_jpg_2 = []
for link in lst_links_jpg:
	response = requests.get(link)
	soup = BeautifulSoup(response.text, "html.parser")

	for item in soup.find_all('a'):
		if not(item.get('href') is None):
			if re.search(r'.jpg', item.get('href')):
				if re.search(r'images', item.get('href')):
					if url_base+item.get('href') not in lst_links_jpg_2:
						lst_links_jpg_2.append(url_base + item.get('href'))

# remove thumbnail images, i.e. those that contain the folder /thumb/ in their url
print(len(lst_links_jpg_2))
lst_links_jpg_3 = []
for i in lst_links_jpg_2:
	if re.search(r'/thumb/', i):
		continue
	lst_links_jpg_3.append(i)
print(len(lst_links_jpg_3))
print(lst_links_jpg_3)
