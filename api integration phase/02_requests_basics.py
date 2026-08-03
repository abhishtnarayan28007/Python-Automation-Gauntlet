import requests

# 1. Endpoint setup
url = "https://api.github.com/users/octocat"

# 2. Make the HTTP GET request
response = requests.get(url)

# 3. Automatically parse the JSON response into a Python dictionary
data = response.json()

# 4. Access data using standard dictionary methods
print(f"Status Code: {response.status_code}")
print(f"Username: {data.get('login')}")
print(f"Name: {data.get('name')}")
print(f"Public Repos: {data.get('public_repos')}")