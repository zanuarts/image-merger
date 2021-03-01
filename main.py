from PIL import Image
import glob
import random
import PIL.ImageOps 

for i in range(0, 1000):
    list_img = []
    images = glob.glob("data/train_images/*.png")

    for image in images:
        d = random.choice(images)
        list_img.append(d)
        if len(list_img) > 10:
            break

    print(list_img)

    new_img = Image.new('RGB', (500, 200))
    index = 0

    for j in range(0, 500, 100):
        for k in range(0, 200, 100):
            img = Image.open(list_img[index])
            new_img.paste(img, (j,k))
            index+=1

    new_img = PIL.ImageOps.invert(new_img)
    new_img.save("data/merge/detect_%d.png"%(i+1))