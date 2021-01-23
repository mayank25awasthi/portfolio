import numpy as np 
import matplotlib.pyplot as plt 
from PIL import Image
pic=Image.open(r'C:\Users\tarun\Downloads\scv20191224_210302.jpeg')
#pic.show()
pic_arr=np.asarray(pic)
print(type(pic_arr))
print(pic_arr.shape)
img=plt.imshow(pic_arr)
#plt.show()
pic_red=pic_arr.copy()
#pic_red=plt.imshow(pic_red[:,:,2],cmap='gray')
pic_red[:,:,1]=0
plt.imshow(pic_red)
plt.show()