import requests

# Test health check
print("Testing health check...")
response = requests.get("http://localhost:8000/")
print(response.json())

# Test analyze endpoint
print("\nTesting analyze endpoint...")
with open("data/TSLA-Q2-2025-Update.pdf", "rb") as f:
    files = {"file": f}
    data = {"query": "Analyze this financial document"}
    response = requests.post(
        "http://localhost:8000/analyze",
        files=files,
        data=data
    )
    print(f"Status: {response.status_code}")
    print(response.json())