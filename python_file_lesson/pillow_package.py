from PIL import Image

img = Image.open(r"C:\Users\Owner\Desktop\python-beginner\python_file_lesson\sample.png")

print(img.size)
print(img.format)

img.show()


## crop image
area = (50,50,75,76)
cropped_img = img.crop(area)

# img.show()
# cropped_img.show()

both_guys = Image.open(r"C:\Users\Owner\Desktop\python-beginner\python_file_lesson\787.jpg")
cover = Image.open(r"C:\Users\Owner\Desktop\python-beginner\python_file_lesson\sample.png")

area = (50, 50, 100, 100)
both_guys.paste(cover, area)

both_guys.show()
