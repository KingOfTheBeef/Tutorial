import os
import urllib3
import json
from PIL import Image
import random


class PokeGen():
    http = urllib3.PoolManager()

    def get_random_poke(self):
        poke_id = random.randint(1, 500)

        url = 'https://pokeapi.co/api/v2/pokemon/' + str(poke_id)

        resp = self.http.request('GET', url)
        di = json.loads(resp.data.decode('utf-8'))

        png_link = di["sprites"]["front_default"]

        return png_link

        #request = self.http.request('GET', png_link)

        #with open("pic.png", 'wb') as localFile:
        #        localFile.write(request.data)