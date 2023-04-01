import img2pdf
lst_img = ['p317.jpg', 'p318.jpg']

with open("test.pdf","wb") as f:
	f.write(img2pdf.convert(lst_img))