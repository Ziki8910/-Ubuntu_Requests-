import os
import requests
from urllib.parse import urlparse
import uuid

def fetch_image():
    url = input("Enter the image URL: ").strip()
    folder_name = "Fetched_Images"
    os.makedirs(folder_name, exist_ok=True)

    try:
        # Spoof headers to look like a real browser
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
                      "image/avif,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://upload.wikimedia.org/"
        }

        response = requests.get(url, stream=True, headers=headers, timeout=15)
        response.raise_for_status()

        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename:
            filename = f"image_{uuid.uuid4().hex}.jpg"

        file_path = os.path.join(folder_name, filename)

        with open(file_path, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        print(f"✅ Image successfully saved as: {file_path}")

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error fetching image: {e}")

if __name__ == "__main__":
    fetch_image()
