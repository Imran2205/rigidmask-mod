import os
import glob


def dataloader(filepath, start, end):
    # source_images = [img for img in os.listdir(filepath) if img.endswith(('.png', '.jpg'))]
    source_images = glob.glob(
        os.path.join(
            f'{filepath}',
            f'*.jpg')
    )
    source_images.sort()
    skip_frames = 1
    consecutive_gap = 1

    l0_train = []
    l1_train = []
    flow_train = []

    if end > len(source_images) or end == -1:
        end = len(source_images)

    for i, img_name in enumerate(source_images[start: end]):
        if i % skip_frames == 0:
            if start+i+consecutive_gap >= len(source_images):
                break
            source_image_path_0 = os.path.join(filepath, img_name)
            source_image_path_1 = os.path.join(filepath, source_images[start+i+consecutive_gap])

            l0_train.append(source_image_path_0)
            l1_train.append(source_image_path_1)
            flow_train.append(source_image_path_0)

    return l0_train, l1_train, flow_train


if __name__ == '__main__':
    source_folder_name = "gameplay_video_1"
    source_path = f'/Volumes/mac_ext_0/research_e/video_for_app/{source_folder_name}/img/'
    a, b, c = dataloader(source_path, 1500, 2500)
    print(a[-1])
    print(b[-1])
