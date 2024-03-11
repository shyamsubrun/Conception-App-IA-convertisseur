import openai 
import requests
from requests.structures import CaseInsensitiveDict
import json


openai.api_key = "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"
# stocke phrase que lon veut generer
description = "image of water and flor "
# envoie requete Api pour la generer
response = openai.Image.create(
    prompt=description, 
    n=1,
    size="512x512"
)
# stocke limage recuperer
image_url = response['data'][0]['url']
# Telechargement de limage
headers = CaseInsensitiveDict()
headers["Accept"] = "image/jpeg"
resp = requests. get (image_url, headers=headers)
with open("generated_image.jpg", "wb") as f:
    f.write(resp.content)