import requests
from dotenv import load_dotenv
import os
load_dotenv()

class Rail:

    def __init__(self) -> None:
        self.check_rail()

    def check_rail(self):
        train = input("Enter train number or name/n")
        data = {"search": train}
        api_key = os.getenv("api-key")
        url = "https://trains.p.rapidapi.com/"
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": "trains.p.rapidapi.com"
        }


        response = requests.post(url, json=data, headers=headers)
        data = response.json()
        print(data[0]['train_num'])


a = Rail()