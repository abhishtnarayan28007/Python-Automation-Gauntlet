import requests

# 1. Base Endpoint (Search GitHub repositories)
url = "https://api.github.com/search/repositories"

# 2. Query Parameters (Our search filters)
# 'q': Search query (e.g., repositories containing 'python')
# 'sort': How to order results ('stars', 'forks', etc.)
# 'per_page': Limit how many results come back
query_params = {
    "q": "python",
    "sort": "stars",
    "order": "desc",
    "per_page": 3
}

# 3. Pass params dictionary into requests.get()
response = requests.get(url, params=query_params)

# 4. Check status and print full generated URL
print(f"Status Code: {response.status_code} 🚦")
print(f"Full Target URL: {response.url} 🔗\n")

# 5. Extract and print top repositories
data = response.json()
print("🔥 Top 3 Starred Python Repositories on GitHub:")

for repo in data.get("items", []):
    name = repo.get("full_name")
    stars = repo.get("stargazers_count")
    description = repo.get("description")
    print(f"⭐ {stars:,} stars | {name}")
    print(f"   📝 {description}\n")