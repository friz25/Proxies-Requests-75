import requests

proxies = {
    'https': 'https://202.56.163.110:8080'
}

# response = requests.get("https://ipinfo.io/json", proxies=proxies)
response = requests.get("https://ipinfo.io/json")
print(response.json()['country'])
print(response.json()['region'])
print(response.text)