import requests

print("+++++++++++++++++++++++++++ FIRST REQUEST ++++++++++++++++++++++++++++++++++++++","\n")

try:
    r = requests.get('http://127.0.0.1:8000/bmicalc?height=2&weight=88')
    r.raise_for_status()
    print("Http status code is: ", r.status_code)

    r_dict = r.json() # turns json answer into a dictionary
    print(r_dict["data"],"\n")
except requests.exceptions.HTTPError as errh:
    print("HTTP Error "+repr(errh))
except requests.exceptions.ConnectionError as errc:
    print("Connection to API Error "+repr(errc))
except requests.exceptions.Timeout as errt:
    print("Timeout Error "+repr(errt))
except requests.exceptions.RequestException as err:
    print("Unknown Error "+repr(err))


# ++++++++++++++++++++++++++++++++++++++++++++++++ with other payload format

print("+++++++++++++++++++++++++++ SECOND REQUEST ++++++++++++++++++++++++++++++++++++++","\n")

payload = {"height": 2, "weight" : 77}
try:
    r = requests.get('http://127.0.0.1:8000/bmicalc', params = payload)
    r.raise_for_status()
    print("Http status code is: ", r.status_code)

    r_dict = r.json() # turns json answer into a dictionary
    print(r_dict["data"],"\n")
except requests.exceptions.HTTPError as errh:
    print("HTTP Error "+repr(errh))
except requests.exceptions.ConnectionError as errc:
    print("Connection to API Error "+repr(errc))
except requests.exceptions.Timeout as errt:
    print("Timeout Error "+repr(errt))
except requests.exceptions.RequestException as err:
    print("Unknown Error "+repr(err))
