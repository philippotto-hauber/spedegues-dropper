import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.arthur-conan-doyle.com/index.php/The_Story_of_Spedegue%27s_Dropper'
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")  
lst_img = []
lst_img_p315 = []
for item in soup.find_all('img'):
	lst_img.append(item['src'])
	if re.search('p315', item['src']):
	    lst_img_p315.append(item['src'])
	#print(item['src'])

#print (item)
#print(lst_img[0:10])

#shutil.copyfileobj(res.raw, f)

#https://www.arthur-conan-doyle.com/images/thumb/b/bd/The-strand-magazine-1928-10-the-story-of-spedegue-s-dropper-p315.jpg/624px-The-strand-magazine-1928-10-the-story-of-spedegue-s-dropper-p315.jpg
#https://www.arthur-conan-doyle.com/images/thumb/4/4d/The-strand-magazine-1928-10-the-story-of-spedegue-s-dropper-p317.jpg/375px-The-strand-magazine-1928-10-the-story-of-spedegue-s-dropper-p317.jpg