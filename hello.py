#!/usr/bin/env python

import requests
import cowsay

print("hello world")

print(requests.get("https://google.com/").text)

##from cowsay import cowsay
##message = """moo""".strip()
##print(cowsay(message))
cowsay.cow("hello")