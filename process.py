import requests

url = "https://eu1.unwiredlabs.com/v2/process.php"

payload = "{\"token\": \"98aaaf71906b29\",\"radio\": \"gsm\",\"mcc\": 255,\"mnc\": 6,\"cells\": [{\"lac\": 7033,\"cid\": 17811}],\"wifi\": [{\"bssid\": \"00:17:c5:cd:ca:aa\",\"channel\": 11,\"frequency\": 2412,\"signal\": -51}, {\"bssid\": \"d8:97:ba:c2:f0:5a\"}],\"address\": 1}"
response = requests.request("POST", url, data=payload)

print(response.text)
