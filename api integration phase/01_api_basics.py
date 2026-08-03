import json
import urllib.request

# The API Endpoint for GitHub's public API
url = "https://api.github.com/users/octocat"

# Sending an HTTP GET request
req = urllib.request.Request(url, headers={"User-Agent": "Python-Script"})

with urllib.request.urlopen(req) as response:
    # 1. Read raw bytes from the HTTP response
    raw_data = response.read().decode("utf-8")

    # 2. Convert JSON string into a Python Dictionary
    data = json.loads(raw_data)

    # 3. Print extracted info
    print(f"Username: {data.get('login')}")
    print(f"Name: {data.get('name')}")
    print(f"Public Repos: {data.get('public_repos')}")