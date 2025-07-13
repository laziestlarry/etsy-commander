# etsy_browser_bot.py — Live Etsy Lister via Playwright (No API)

import json
import os
import asyncio
from playwright.async_api import async_playwright

LISTINGS_DIR = "/mnt/data/etsy_commander/uploader"

async def upload_listing(page, listing):
    print(f"🚀 Uploading: {listing['title']}")
    await page.goto("https://www.etsy.com/your/shops/me/listings/create")
    await page.wait_for_timeout(4000)  # Wait for page to settle

    await page.fill("[placeholder='Title']", listing['title'][:139])
    await page.fill("textarea[name='description']", listing['description'])
    await page.fill("input[name='price']", str(listing['price']))

    # Handle image upload
    image_path = listing.get("image_path")
    if image_path and os.path.exists(image_path):
        input_file = await page.query_selector("input[type='file']")
        await input_file.set_input_files(image_path)
        await page.wait_for_timeout(3000)

    # Mark as digital product manually (no selector guaranteed)
    print("✅ Listing ready for review — manually complete any category/tags")
    await page.wait_for_timeout(12000)  # Pause for user input if needed

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=70)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://www.etsy.com/signin")
        print("🔐 Please login to Etsy manually once in the browser window...")
        await page.wait_for_timeout(45000)  # Manual login

        for file in os.listdir(LISTINGS_DIR):
            if file.endswith(".json"):
                with open(os.path.join(LISTINGS_DIR, file), 'r') as f:
                    listing = json.load(f)
                    await upload_listing(page, listing)

        print("🎉 All listings processed.")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
