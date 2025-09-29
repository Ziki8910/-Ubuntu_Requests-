import os
import requests
from urllib.parse import urlparse
import uuid

def fetch_image():
    # Prompt user for image URL
    url = input("Enter the image URL: ").strip()

    # Directory to store fetched images
    folder_name = "Fetched_Images"
    os.makedirs(folder_name, exist_ok=True)

    try:
        # Make HTTP GET request
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise error for bad status codes

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no filename, generate one
        if not filename:
            filename = f"image_{uuid.uuid4().hex}.jpg"

        # Full path for saving
        file_path = os.path.join(folder_name, filename)

        # Save image in binary mode
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        print(f"✅ Image successfully saved as: {file_path}")

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error fetching image: {e}")

if __name__ == "__main__":
    fetch_image()
