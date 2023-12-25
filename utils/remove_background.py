import requests
import logging

# rapidapi saytidan ushbu tokenni olamiz

url = "https://background-removal.p.rapidapi.com/remove"

headers = {
    "content-type": "application/x-www-form-urlencoded",
    "X-RapidAPI-Key": "9cb3bc16d5msh98edf4f058f8c72p1aad2bjsna26e1f7d4aaa",
    "X-RapidAPI-Host": "background-removal.p.rapidapi.com"
}


# test payload
# payload = "image_url=https%3A%2F%2Fobjectcut.com%2Fassets%2Fimg%2Fraven.jpg"

async def remove_background(img_url):
    payload = f"image_url={img_url}"
    response = requests.request("POST", url, data=payload, headers=headers)
    # logging.info(response.json()['response']['image_url'])
    return response.json()['response']['image_url']

#
# print(remove_background("http://telegra.ph//file/087e49124dd4a2b916045.jpg"))
