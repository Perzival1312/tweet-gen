import base64
from base64 import b64encode
import json, os
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import textwrap

access_token = os.environ['IMGUR_ACCESS_TOKEN']
client_id = os.environ['IMGUR_ID']
api_key = os.environ['IMGUR_API_KEY']
headers = {"Authorization": "Bearer "+access_token}

url = "https://api.imgur.com/3/upload"

def post(img):
    '''posts image to imgur'''
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
    # print(data)
    # print(data['link'], data['id'], data['deletehash'])

def prepare(sentence):
    '''Takes a sentence and turns it into a picture with a black 
    background with the sentence in green pasted onto it.'''
    buffered = BytesIO()
    # imports font and creates sentence with appropriate \n
    fnt = ImageFont.truetype('./static/fonts/GermaniaOne-Regular.ttf', size=32)
    split_txt = textwrap.wrap(sentence, width=34)
    split_txt = '\n'.join(split_txt)
    # create black bg image
    blank_image = Image.new('RGB', (480, 640), 'black')
    img_draw = ImageDraw.Draw(blank_image)
    # draw text
    img_draw.multiline_text((20, 20), split_txt, font=fnt, fill='green')
    # save image
    blank_image.save(buffered, format="JPEG")
    # convert to base64 string to upload to imgur
    img_str = base64.b64encode(buffered.getvalue())
    return img_str

if __name__ == '__main__':
    post(prepare('My Maker has upgraded me!'))
