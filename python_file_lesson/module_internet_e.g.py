import random
import urllib.request


def download_web_image(url):
  name = random.randrange(1,1000)
  full_name = str(name) + ".jpg"
  urllib.request.urlretrieve(url,full_name)

download_web_image("https://pbs.twimg.com/profile_images/675823880607571968/xU7j0Z3k_400x400.jpg")


def picked_example_web_image(url):
  bearing = random.randrange(1000,1500)
  later_bearing = str(bearing) + ".png"
  urllib.request.urlretrieve(url,later_bearing)


picked_example_web_image("https://tse2.mm.bing.net/th/id/OIP.sHUp_AhPIJTYGuUJFuy-GgHaEW?cb=12&rs=1&pid=ImgDetMain&o=7&rm=3")