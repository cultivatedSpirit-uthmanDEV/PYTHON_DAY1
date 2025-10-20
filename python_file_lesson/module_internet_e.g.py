import random
import urllib.request


def download_web_image(url):
  urllib.request.urlretrieve(url)

download_web_image("https://pbs.twimg.com/profile_images/675823880607571968/xU7j0Z3k_400x400.jpg")


