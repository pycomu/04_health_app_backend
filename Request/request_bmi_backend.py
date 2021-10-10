import requests

r = requests.get('http://127.0.0.1:8000/bmicalc?height=2&weight=88')
r_dict = r.json() # turns json answer into a dictionary
print(r_dict["data"],"\n")


payload = {"height": 2, "weight" : 77}
r = requests.get('http://127.0.0.1:8000/bmicalc', params = payload)
r_dict = r.json() # turns json answer into a dictionary
print(r_dict["data"],"\n")