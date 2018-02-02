import urlfetch
import json

# Function Extract and return data
def getData(a):
    u = "http://dbpedia.org/data/" + user_input + ".json"
    print u
    data = urlfetch.fetch(url=u)
    json_data = json.loads(data.content)
    u_resource = "http://dbpedia.org/resource/" + user_input
    print u_resource
    u_searchKey_1 = "http://www.w3.org/2000/01/rdf-schema#comment"
    # u_searchKey_2 = "http://www.w3.org/2000/01/rdf-schema#label"
    # print json_data

    for j in json_data[u_resource]:
        if(j == u_searchKey_1):
            # print "it's here"
            result = [abstract["value"] for abstract in json_data[u_resource][j] if abstract["lang"] == "en"]
            print result[0]
            # print "success"
            

user_input = raw_input ("About whom you wanna get Data?: ")

getData(user_input)

