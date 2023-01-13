import os
import shutil
from PIL import Image
from tqdm import tqdm

source_folder = './gallery_full_resolution'
destination_folder = './gallery'

# 5472 x 3648 (3:2)
# 720p: 1280 x 853.33
# 1080p: 1920 x 1280
# 2k: 2560 x 1706.66

size = (1920, 1280)
# size = (1280, 854)

if os.path.exists(destination_folder):
    shutil.rmtree(destination_folder)
    print('clean old version, build new version')
os.makedirs(destination_folder)

filelist = os.listdir(source_folder)
pbar = tqdm(total=len(filelist))
for file in filelist:
    image = Image.open(os.path.join(source_folder, file))
    image = image.resize(size)
    
    file = file.replace("JPG", "jpeg").replace(" ", "_")
    image.save(os.path.join(destination_folder, file))
    pbar.update(1)