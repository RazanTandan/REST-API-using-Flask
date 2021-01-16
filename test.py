import requests 

BASE_URL = "http://127.0.0.1:5000/"

data = [
    {
        "name" : "How to make momos?", "views" : 6000, "likes" : 500
    },
    {
        "name" : "Create new gmail account", "views" : 7000, "likes" : 300
    },
    {
        "name" : "We are hiring python developers", "views" : 9000, "likes" : 980
    }
]


#PUTTING DATA
# for i in range(0, len(data)):
#     response = requests.put(BASE_URL+"video/"+str(i), data[i])
#     print(response.json())

# response = requests.put(BASE_URL+"video/0", {"name" : "volg 1", "views" : 4000, "likes" : 500})


#GETTING DATA
# response = requests.get(BASE_URL+'video/0')
# print(response.json())


#PATCHING DATA
# response = requests.patch(BASE_URL+'video/0', {"name" : "Who is Rajan?","views" : 66000, "likes" : 9010})
# print(response.json())


#DELETING DATA
# response = requests.delete(BASE_URL+'video/0')
# print(response)