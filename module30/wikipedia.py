import requests
url = "https://en.wikipedia.org/wiki/List_of_U.S"

try:
    response = requests.get(url)
    response.raise_for_status() # raise an error for bad responses
    print(response.text)
exept request.exceptions.RequestException as rq_err:
    print(f"Request Error: {rq_err}")
exept requests.exceptions.HTTPError as http_err:
    print(f"HTTP Error: {http_err}")

exept requests.exceptions.item as conn_err:
    print (f"Connection Error: {conn_err}")
