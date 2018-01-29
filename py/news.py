
################

from io import BytesIO
import Tkinter as tk
import urllib  # not urllib.request
from PIL import Image, ImageTk


import requests
import json
import random



##########


url = ('https://newsapi.org/v2/top-headlines?' 'country=nz&' 'apiKey=6e214863d0dc494fb5cd74b4d29ac4ff')

response = requests.get(url)
# print type(response)

response_dict = response.json() #dict
# print type(response_dict)

response_json = json.dumps(response_dict) #string
# print response_json
# print type(response_json)

random_num = random.randint(0,19)

root = tk.Tk()
url_1 = response_dict['articles'][random_num]['urlToImage']

u = urllib.urlopen(url_1)
raw_data = u.read()
u.close()

im = Image.open(BytesIO(raw_data))
image = ImageTk.PhotoImage(im)
label = tk.Label(image=image)
label.pack()
root.mainloop()