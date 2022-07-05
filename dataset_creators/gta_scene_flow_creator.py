import os
import shutil
from tqdm import tqdm

source_folder_name = "gameplay_video_3"

source_path = f'/Users/imrankabir/Downloads/video_for_app/{source_folder_name}/img/'
dest_path = f'/Users/imrankabir/Desktop/research/semantic_seg_audio_description/rigidmask-mod/gta_scene_flow/{source_folder_name}/testing/image_2'

if not os.path.exists(dest_path):
    os.makedirs(dest_path)

source_images = [img for img in os.listdir(source_path) if '.png' in img]
source_images.sort()

skip_frames = 1
consecutive_gap = 1

copy_counter = 0
for i, img_name in tqdm(enumerate(source_images)):
    if i % skip_frames == 0:
        if i+consecutive_gap >= len(source_images):
            break
        source_image_path_0 = os.path.join(source_path, img_name)
        source_image_path_1 = os.path.join(source_path, source_images[i+consecutive_gap])
        shutil.copy(source_image_path_0, dest_path)
        shutil.copy(source_image_path_1, dest_path)

        dest_image_name_0 = f"{copy_counter}".zfill(6) + "_10.png"
        dest_image_name_1 = f"{copy_counter}".zfill(6) + "_11.png"

        dest_image_path_0 = os.path.join(dest_path, dest_image_name_0)
        dest_image_path_1 = os.path.join(dest_path, dest_image_name_1)

        dest_image_path_0_old = os.path.join(dest_path, img_name)
        dest_image_path_1_old = os.path.join(dest_path, source_images[i+consecutive_gap])

        os.rename(dest_image_path_0_old, dest_image_path_0)
        os.rename(dest_image_path_1_old, dest_image_path_1)

        copy_counter += 1
