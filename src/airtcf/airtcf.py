from src.pyxios import Pyxios

def short(link):
    shortLink = Pyxios('https://airt.cf/airt/short/')
    postResponse = shortLink.post(
        json={
            'link': link
            }
        )
    return postResponse.data

def shortener(link):
    shortLink = Pyxios('https://airt.cf/airt/short/')
    postResponse = shortLink.post(
        json={
            'link': link
            }
        )
    return postResponse.data

