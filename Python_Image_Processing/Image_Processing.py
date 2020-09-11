from PIL import Image,ImageFilter

img=Image.open('./Images/Image_03.jpg')
#filter_img=img.filter(ImageFilter.SHARPEN)
filter_img=img.convert('L')
'''rotate_img=filter_img.rotate(90)
rotate_img.save('grey.png','png')
rotate_img.show()'''
'''resize_img=filter_img.resize((500,500))
resize_img.save('resize.png','png')
resize_img.show()'''
box=(200,200,600,600)
region_img=filter_img.crop(box)
region_img.save('crop.png','png')
region_img.show()