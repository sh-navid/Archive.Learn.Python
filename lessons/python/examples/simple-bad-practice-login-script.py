## pip install requests


import requests

res = requests.post(
    "http://127.0.0.1:3000/auth",
    json={"user": "David", "password": "898989"},
)
print(res.text)
