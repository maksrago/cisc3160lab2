import sys
import requests

# Test JSON API call
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
jsonResponse = response.json()

# Upon successful 200 response, print output in the form of JSON
if response.ok:
    print("OK! -", response.status_code)
    print("\nRETURNED JSON:")
    print(jsonResponse)

else:
    print("Connection Error! -", response.status_code)
