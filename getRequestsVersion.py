import requests

# Virtualenv: Question 4
# print(requests.__version__)

# Curl: Question 5
# res = requests.get("http://www.google.com/")
# print(res.text)

# Curl: Question 10
rawURL = "https://raw.githubusercontent.com/urvi-p/CMPUT404-Labs/main/getRequestsVersion.py"

res = requests.get(rawURL)
print(res.text)
