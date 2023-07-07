from PIL import Image
image = Image.open('./res/guido.jpg')
rect = 80, 20, 310, 360
image.crop(rect).show()

# 缩略图
size = 128, 128
image.thumbnail(size)
image.show()