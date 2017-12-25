import random
import urllib.request
def download_random_image(url):
    x = random.randrange(1 , 100)
    full_name=str(x)+".jpg"
    urllib.request.urlretrieve(url,full_name)
download_random_image("https://www.dayafterindia.com/wp-content/uploads/2017/02/virat-kohli.jpg")