
################################################################################################
################################################################################################
###                                                                                     ########
###                                                                                     ########
###                               NEWS FETCH FROM API CALLING                           ########
###               -----------------------------------------------------------           ########
###                                                                                     ########
###                            AUTHOR:    VIKAS KUMAR (@dzenvikas)                      ########
###                            GITHUB:    https://dzenvikas.github.io/                  ########
###                            ANGELLIST: https://angel.co/dzenvikas                    ########
###                                                                                     ########
################################################################################################
################################################################################################


#------------------
# SOUCE CODE
#------------------


from io import BytesIO
import Tkinter as tk
import urllib
from PIL import Image, ImageTk


import requests
import json
import random


# ----  getting response from API call ----

url = ('https://newsapi.org/v2/top-headlines?' 'country=nz&' 'apiKey=6e214863d0dc494fb5cd74b4d29ac4ff') #API call

response = requests.get(url)
# print type(response)                                                  #log

response_dict = response.json() #dict
# print type(response_dict)                                             #log

response_json = json.dumps(response_dict) #string
# print response_json                                                   #log
# print type(response_json)                                             #log

random_num = random.randint(0,19)   #generate random integer in range(0 to 19)

root = tk.Tk()                                                          #window
news_image_url = response_dict['articles'][random_num]['urlToImage']    #fetch image link
news_source = response_dict['articles'][random_num]['source']['name']   #fetch source name
news_title = response_dict['articles'][random_num]['title']             #fetch news title
news_desc = response_dict['articles'][random_num]['description']        #fetch news description
news_link = response_dict['articles'][random_num]['url']                #fetch news url

img = urllib.urlopen(news_image_url)                                    #open image url
raw_data = img.read()                                                   #read image data
img.close()                                                             #finish image read

im = Image.open(BytesIO(raw_data))                                      #converts raw data to image
news_image = ImageTk.PhotoImage(im)                                     #image set to variable news_image
label = tk.Label(image=news_image)                                      #set image to Tkinter label
label_1 = tk.Label(text='SOURCE: ' + news_source)                       #similar to above
label_2 = tk.Label(text='TITLE: ' + news_title)                         #similar to above
label_3 = tk.Label(text='DESCRIPTION: ' + news_desc)                    #similar to above
label_4 = tk.Label(text='LINK: ' + news_link)                           #similar to above

label_1.pack()                                                          #output
label_2.pack()                                                          #output
label_3.pack()                                                          #output
label_4.pack()                                                          #output
label.pack()                                                            #output
root.mainloop()                                                         #prevents window from closing