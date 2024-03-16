from urllib.request import urlopen
import bs4 as bs
import requests
import certifi
import os.path
import shutil
import ssl

# actual page count: 1228
start_page = 1
end_page = 1228

download_path = "comic/" # Do not forget the last "/"

comic_pages = []
for x in range(start_page-1, end_page):
    file_name = f"{download_path}{x+1}.jpg"
    comic_path_to_test = file_name
    file_exists = os.path.isfile(comic_path_to_test)
    if file_exists:
        print(f"File {comic_path_to_test} already exists. Skipping.")
        comic_pages.append(None);   # Append a useless value (rest of script expects value here
                                    # as it indexed through comic_pages)
    else:
        request = f"https://twokinds.keenspot.com/comic/{x+1}/"
        source = urlopen(request, context=ssl.create_default_context(cafile=certifi.where()))
        parsed = bs.BeautifulSoup(source,"lxml")
        images = parsed.find_all("img")
        for image in images:
            image_alt = image["alt"]
            if image_alt == "Comic Page":
                comic_pages.append(image["src"])
                print("Image link: " + image["src"])
        image_request = requests.get(comic_pages[x], stream = True)
        if image_request.status_code == 200:
            with open(file_name,"wb") as f:
                shutil.copyfileobj(image_request.raw, f)
            print("Image sucessfully Downloaded as: " + file_name)
        else:
            print("Image Couldn't be retrieved")