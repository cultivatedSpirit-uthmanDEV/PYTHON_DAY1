from PIL import Image
from PIL import ImageFilter

musk = Image.open(r"C:\Users\Owner\Desktop\python-beginner\python_file_lesson\IMAGE\image.png")
musk_blur = musk.filter(ImageFilter.BLUR )
detail = musk.filter(ImageFilter.DETAIL )
edges = musk.filter(ImageFilter.FIND_EDGES )

musk_blur.show()
detail.show()
edges .show()
