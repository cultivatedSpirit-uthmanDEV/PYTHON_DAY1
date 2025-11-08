from PIL import Image

musk = Image.open(r"C:\Users\Owner\Desktop\python-beginner\python_file_lesson\IMAGE\image.png")
resize_musk = musk.resize((250, 250))
flip_image = musk.transpose(Image.FLIP_LEFT_RIGHT)
spin_musk = musk.transpose(Image.ROTATE_90)




resize_musk.show()
flip_image.show()
spin_musk.show()


