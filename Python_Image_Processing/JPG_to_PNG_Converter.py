import os
import sys
from PIL import Image

# from sys module , we grab two argument

jpg_folder=sys.argv[1]
png_folder=sys.argv[2]
#print(jpg_folder,png_folder)
# check if new folder is exists or not , if not then create it
if not os.path.exists(png_folder):
	os.makedirs(png_folder)
for filename in os.listdir(jpg_folder):
	#filename=filename.strip('.jpg')
	img=Image.open(f'{jpg_folder}{filename}')	
	filename=filename.strip('.jpg')
	img.save(f'{png_folder}{filename}.png','png' )
print('done')
#loop through folder
#convert images to png
#save the new folder.
