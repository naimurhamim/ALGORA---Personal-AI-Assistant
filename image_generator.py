import requests
from PIL import Image
from io import BytesIO


def generate_image(text, save_path='generated_image.png'):
    url = 'https://api.airforce/v1/imagine2'
    params = {
        'text': text
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        print("Response Content:", response.content)
        try:
            image = Image.open(BytesIO(response.content))
            image.save(save_path)
            print(f'Image saved as {save_path}')
        except IOError:
            print("Failed to open image. The response may not be a valid image.")
    else:
        print(f'Failed to retrieve image. Status code: {response.status_code}')
