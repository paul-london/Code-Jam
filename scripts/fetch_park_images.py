import pandas as pd
import requests
from pathlib import Path
from urllib.parse import urlparse
import os

# Load CSV
df = pd.read_csv("parks.csv")  # replace with your full path if needed

# Output directory for images
output_dir = Path("park_images")
output_dir.mkdir(exist_ok=True)

def sanitize_filename(name):
    return "".join(c for c in name if c.isalnum() or c in (' ', '.', '_')).rstrip()

# Download images
for _, row in df.iterrows():
    name = sanitize_filename(row['name']).replace(" ", "_")
    image_url = row['image_url']

    if pd.isna(image_url):
        continue

    # Get extension
    ext = os.path.splitext(urlparse(image_url).path)[-1]
    if not ext or len(ext) > 5:
        ext = ".jpg"  # fallback

    filename = output_dir / f"{name}{ext}"

    try:
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")
    except Exception as e:
        print(f"Failed to download {name}: {e}")