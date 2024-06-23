import sys
import os
from PIL import Image

# grab first and second argument through command line prompt (sys.argv)

# check if new/ exists, if not create directory (os)
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# loop through Pokedex,
# convert images to png
# save to the new folder
if not os.path.exists(output_folder):
    os.makedir(output_folder)

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png','png')
    print('all done!')

