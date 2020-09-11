from PIL import Image
img=Image.open('./Images/Girl.jpg')
img.thumbnail((400,400))
img.save('./Images/thumbnail.jpg')