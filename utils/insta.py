import requests
import json


def downloader(link):
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url": link}

    headers = {
        "X-RapidAPI-Key": "28d0d114c8msh5b9ad1427ffbd16p1c86a9jsn15d5cd9c4ddc",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    result = json.loads(response.text)
    # print(result)
    dict = {}
    if "error" in result:
        return "error"
    else:
        if result["Type"] == "Post-Image":
            dict['type'] = "image"
            dict["media"] = result["media"]
            return dict
        elif result["Type"] == "Post-Video":
            dict["type"] = "video"
            dict["media"] = result["media"]
            return dict
        elif result["Type"] == "Carousel":
            dict["type"] = "carousel"
            dict["media"] = result["media"]
            return dict
        else:
            return "error"


# print(downloader(link="https://www.instagram.com/p/CqUfk0mtpBW/?utm_source=ig_web_copy_link&igshid=MzRlODBiNWFlZA=="))
