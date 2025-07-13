# etsy_uploader.py — Commander Deployment Module

import os
import json
import requests

def load_listing_data(listing_path):
    with open(listing_path, 'r') as f:
        return json.load(f)

def simulate_upload_to_etsy(title, description, image_url, price):
    print("🚀 Uploading to Etsy...")
    print(f"Title: {title}")
    print(f"Description: {description[:80]}...")
    print(f"Image: {image_url}")
    print(f"Price: ${price:.2f}")
    print("✅ Simulated Etsy listing successful!")

def run_batch_upload(directory="/mnt/data/etsy_commander/uploader"):
    files = [f for f in os.listdir(directory) if f.endswith(".json")]
    for file in files:
        listing = load_listing_data(os.path.join(directory, file))
        simulate_upload_to_etsy(
            listing["title"],
            listing["description"],
            listing["image_url"],
            listing["price"]
        )

if __name__ == "__main__":
    run_batch_upload()
