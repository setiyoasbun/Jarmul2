import os
import sys
from PIL import Image
from os.path import basename

os.chdir('uploads/')
name = sys.argv[1]
imgname = os.path.splitext(name)[0]
img = Image.open(name)
imgformat = sys.argv[2]
height = int(sys.argv[3])
width = int(sys.argv[4])

if height == 0 or width == 0:
   img.save('new-'+imgname+'.'+imgformat,imgformat)
else:
   new_img = img.resize((width,height)) 
   new_img.save('new-'+imgname+'.'+imgformat,imgformat)