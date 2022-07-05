import os


def dataloader(filepath):
    source_images = [img for img in os.listdir(filepath) if '.png' in img]
    source_images.sort()
    skip_frames = 1
    consecutive_gap = 1

    l0_train = []
    l1_train = []
    flow_train = []

    copy_counter = 0
    for i, img_name in enumerate(source_images):
        if i % skip_frames == 0:
            if i+consecutive_gap >= len(source_images):
                break
            source_image_path_0 = os.path.join(filepath, img_name)
            source_image_path_1 = os.path.join(filepath, source_images[i+consecutive_gap])
            copy_counter += 1

            l0_train.append(source_image_path_0)
            l1_train.append(source_image_path_1)
            flow_train.append(source_image_path_0)

    return l0_train, l1_train, flow_train


if __name__ == '__main__':
    source_folder_name = "gameplay_video_1"
    source_path = f'/Users/imrankabir/Downloads/video_for_app/{source_folder_name}/img/'
    a, b, c = dataloader(source_path)
    # print(len(a))
    # print(b)
