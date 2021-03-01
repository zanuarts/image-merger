from PIL import Image
import glob
import random
import PIL.ImageOps 

TOTAL_MERGED_IMAGE = 10
TRAIN_IMAGE_DIRECTORY = "data/train_images"
TRAIN_IMAGE_FILETYPE = ".png"

TOTAL_LETTER = 10
LETTER_SIZE = 100
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 200


print('Generating merged images...')
images_path = glob.glob(f'{TRAIN_IMAGE_DIRECTORY}/*{TRAIN_IMAGE_FILETYPE}')

for i in range(0, TOTAL_MERGED_IMAGE):
    random.shuffle(images_path)
    images = images_path[:TOTAL_LETTER]

    canvas = Image.new('RGB', (CANVAS_WIDTH, CANVAS_HEIGHT))
    for j in range(0, CANVAS_WIDTH, LETTER_SIZE):
        for k in range(0, CANVAS_HEIGHT, LETTER_SIZE):
            img = Image.open(images.pop())
            canvas.paste(img, (j,k))

    canvas = PIL.ImageOps.invert(canvas)
    canvas.save(f'data/merge/detect_{i+1}.png')

print(f'{TOTAL_MERGED_IMAGE} merged image(s) has succefully generated')