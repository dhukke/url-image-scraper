# download all images from a given url

# import libraries
import os.path
import requests
from bs4 import BeautifulSoup

directory = './images/'

if not os.path.isdir(directory):
    os.mkdir(directory)

site_url = "https://github.com/dhukke"

# get the html from the url as a string
html_string = requests.get(site_url).text

# from html string, create a BeautifulSoup object
soup = BeautifulSoup(html_string, "html.parser")

# get all image tags
image_tags = soup.find_all("img")

# donwload all images to disk
for image_tag in image_tags:
    try:
        # get the image url
        image_url = image_tag.get("src")

        if image_url:

            # download the image
            image_content = requests.get(image_url).content

            filename = image_url.split("?")[0].split("/")[-1]

            # save the image to disk
            with open(os.path.join(directory, filename), "wb") as handler:
                handler.write(image_content)
                print("Image saved: " + image_url.split("/")[-1])
    except Exception as e:
        print("Error downloading image: " + image_url + ". Error: " + str(e))
        pass
