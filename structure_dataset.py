import os
import shutil

data_dir = "YeaZ_universal_images_and_masks"
img_dest_dir = "Datasets/images"
label_dest_dir = "Datasets/labels"

if __name__ == "__main__":
    if not os.path.isdir("Datasets"):
        os.mkdir("Datasets")
        os.mkdir("Datasets/images")
        os.mkdir("Datasets/labels")
    for dir in os.walk(data_dir):
        for f in dir[2]:
            if f[-6:] == "im.tif":
                new_f = f.replace("_im", "")
                shutil.copyfile(os.path.join(dir[0], f), os.path.join(img_dest_dir, new_f))
            elif f[-8:] == "mask.tif":
                new_f = f.replace("_mask", ".label")
                new_f = f.replace("tif", "tiff")
                shutil.copyfile(os.path.join(dir[0], f), os.path.join(label_dest_dir, new_f))