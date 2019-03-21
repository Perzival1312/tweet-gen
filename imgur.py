import base64
from base64 import b64encode
import json, os
import requests
from PIL import Image, ImageDraw
from io import BytesIO
import textwrap

access_token = os.environ['IMGUR_ACCESS_TOKEN']
client_id = os.environ['IMGUR_ID']
api_key = os.environ['IMGUR_API_KEY']
headers = {"Authorization": "Bearer "+access_token}

url = "https://api.imgur.com/3/upload"

def post(img):
    j1 = requests.post(
        url, 
        headers = headers,
        data = {
            'key': api_key, 
            'image': img,
            'type': 'base64',
            'name': '1.jpg',
            'title': 'Title'
        }
    )
    data = json.loads(j1.text)['data']
    print(data)
    print(data['link'], data['id'], data['deletehash'])

def prepare(sentence):
    buffered = BytesIO()
    blank_image = Image.new('RGB', (400, 300), 'black')
    img_draw = ImageDraw.Draw(blank_image)
    split_txt = textwrap.wrap(sentence, width=50)
    split_txt = '\n'.join(split_txt)
    img_draw.multiline_text((70, 70), split_txt, fill='green')
    blank_image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())
    return img_str
