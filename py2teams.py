import config
import requests
from sys import stdin

input  = stdin.read()

msg = str(input.replace("\n", "</br>"))

payload = {'text' : msg }

requests.post(url=config.webhook, json=payload)