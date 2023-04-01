# importing required modules
import urllib.request

# setting filename and image URL

urls_img = ['https://www.arthur-conan-doyle.com/images/thumb/4/4d/The-strand-magazine-1928-10-the-story-of-spedegue-s-dropper-p317.jpg/375px-The-strand-magazine-1928-10-the-story-of-spedegue-s-dropper-p317.jpg',
            'https://www.arthur-conan-doyle.com/images/thumb/b/b0/The-strand-magazine-1928-10-the-story-of-spedegue-s-dropper-p318.jpg/375px-The-strand-magazine-1928-10-the-story-of-spedegue-s-dropper-p318.jpg']

# calling urlretrieve function to get resource
for url in urls_img:
    filename = url[-8:]
    urllib.request.urlretrieve(url, filename)
