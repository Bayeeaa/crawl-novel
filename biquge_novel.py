import requests
url = "https://www.xzmncy.com/list/5418/2610707.html"
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0"
}
response = requests.get(url,headers)
print(response)