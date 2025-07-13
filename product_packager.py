# product_packager.py — Create downloadable product ZIPs

import os
import zipfile
import uuid
from datetime import datetime

def package_product(asset_dir, title, output_dir="/mnt/data/etsy_commander/delivery"):
    os.makedirs(output_dir, exist_ok=True)
    
    safe_title = title.replace(" ", "_").replace("/", "-")[:40]
    filename = f"{safe_title}_{uuid.uuid4().hex[:6]}.zip"
    filepath = os.path.join(output_dir, filename)

    with zipfile.ZipFile(filepath, 'w') as zipf:
        for root, _, files in os.walk(asset_dir):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, asset_dir)
                zipf.write(full_path, arcname)

    print(f"📦 Packaged: {filepath}")
    return filepath

# Example usage:
if __name__ == "__main__":
    sample_asset_folder = "/mnt/data/assets/sample_etsy_kit"
    package_product(sample_asset_folder, "Motivational Wall Art")
