import requests
import os

os.mkdir('book_images')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}
script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, "image_links.txt")

with open(filename, 'r') as f:
    links_text = f.read()
    links_list = links_text.split('\n')
    print(links_list)

for i, image_url in enumerate(links_list):
    response = requests.get(image_url, headers=headers)
    with open(f'book_images/{i+1}.jpg','wb') as imagefile:
        imagefile.write(response.content)