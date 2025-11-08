from PIL import Image

img = Image.open(r"C:\Users\Owner\Desktop\python-beginner\python_file_lesson\IMAGE\image.png")
r, g, b = img.split()

r.show()
g.show()
b.show()