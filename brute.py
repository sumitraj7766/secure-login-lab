import requests

url = "http://127.0.0.1:5000/login"

passwords = ["123", "111", "admin", "password", "12345678"]

for p in passwords:
    res = requests.post(url, json={
        "username": "admin",
        "password": p
    })

    print("Trying:", p, "=>", res.json())