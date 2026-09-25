import httpx

# response = httpx.get("https://httpbin.org/get")

# print(response.status_code)
# print(response.headers)
# print(response.text)

data = {
    "name": "Anurag",
    "role": "developer"
}

response = httpx.post(
    "https://httpbin.org/post",
    json=data
)

print(response.status_code)
print(response.json())

# Error handling

try:
    response = httpx.get("https://httpbin.org/get")

    response.raise_for_status()

    data = response.json()
    print(data)

except httpx.HTTPError as e:
    print(f"API request failed: {e}")