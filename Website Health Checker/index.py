import requests

urls = ["https://www.google.com", "https://www.github.com", "https://thisisafakesite123.com"]

print("--- Website Status Report ---")
for url in urls:
    try:
        response = requests.get(url, timeout=5)
        # 200 is the standard "Success" code
        if response.status_code == 200:
            print(f"✅ {url} is ONLINE")
        else:
            print(f"⚠️ {url} returned status code: {response.status_code}")
    except requests.exceptions.RequestException:
        print(f"❌ {url} is DOWN or Unreachable")