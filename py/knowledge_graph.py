
################################################################################################
################################################################################################
###                                                                                     ########
###                                                                                     ########
###                                   DATA FETCH FROM DBPEDIA                           ########
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
import urlfetch
import json
import random


# Function Extract and return data
def getData(a):
    u = "http://dbpedia.org/data/" + user_input + ".json"
    # print u
    data = urlfetch.fetch(url=u)
    json_data = json.loads(data.content)
    u_resource = "http://dbpedia.org/resource/" + user_input
    # print u_resource
    u_searchKey_1 = "http://dbpedia.org/ontology/thumbnail"
    u_searchKey_2 = "http://www.w3.org/2000/01/rdf-schema#label"
    u_searchKey_3 = "http://www.w3.org/2000/01/rdf-schema#comment"
    # print json_data
    u_thumbnail = None
    u_name = None
    u_bio = None
    
    for j in json_data[u_resource]:

        if(j == u_searchKey_1):
            u_thumbnail = [abstract["value"] for abstract in json_data[u_resource][j] if abstract["type"] == "uri"]

        if(j == u_searchKey_2):
            u_name = [abstract["value"]
                      for abstract in json_data[u_resource][j] if abstract["lang"] == "en"]

            # print "\n" + "NAME: " + u_name[0]

        if(j == u_searchKey_3):
            u_bio = [abstract["value"]
                     for abstract in json_data[u_resource][j] if abstract["type"] == "literal" and abstract["lang"] == "en"]
            # print "RESULT: " + u_bio[0]

    return [u_thumbnail[0], u_name[0], u_bio[0]]

user_input = raw_input("About whom you wanna get Data?: ")


x = getData(user_input) #getting raw_data from dbpedia

###   TKinter UI    ###

root = tk.Tk()  # window
root.title("@dzenvikas") #title

img = urllib.urlopen(x[0])  # open image url
raw_data = img.read()  # read image data
img.close()  # finish image read

im = Image.open(BytesIO(raw_data))  # converts raw data to image
thumbnail = ImageTk.PhotoImage(im)  # image set to variable thumbnail
label_1 = tk.Label(image=thumbnail)  # set logo to Tkinter label
label_2 = tk.Label(text='NAME: ' + x[1])  # similar to above
label_3 = tk.Label(text='BIO: ' + x[2], wraplength=600)  # similar to above

label_1.pack(pady=10)  # output
label_2.pack(pady=10)  # output
label_3.pack(pady=10)  # output
# label_4.pack()  # output
root.mainloop()



