import requests
import json
import os
from playsound import playsound

Base_URL="http://api.alquran.cloud/v1"

def list_surah():
    response=requests.get(f"{Base_URL}/surah")
    if response.status_code==200:
        surahs=response.json()["data"]
        for surah in surahs:
            print(f"{surah['number']}.{surah['name']}.{surah['englishName']})")


    else:
        print("Fetching Error")


list_surah()