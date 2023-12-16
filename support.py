import imageio

def split_stack(input_file, output_folder):
    img = imageio.mimread(input_file)
    for i, frame in enumerate(img):
        imageio.imwrite(f"{output_folder}/frame_{i}.png", frame)
    