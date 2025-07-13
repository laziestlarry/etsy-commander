# growth_dashboard.py — Etsy Commander Money & Metrics UI

import streamlit as st
import json
import os
from datetime import datetime

LOG_DIR = os.path.join(os.path.dirname(__file__), "uploader")

def load_listings():
    listings = []
    for file in os.listdir(LOG_DIR):
        if file.endswith(".json"):
            with open(os.path.join(LOG_DIR, file), 'r') as f:
                data = json.load(f)
                listings.append(data)
    return listings

def main():
    st.set_page_config(page_title="Etsy Commander Dashboard", layout="wide")
    st.title("💰 Etsy Commander — Growth Dashboard")

    listings = load_listings()
    st.metric("Total Listings", len(listings))

    total_revenue = sum([l.get("price", 0) for l in listings])
    st.metric("Estimated Revenue", f"${total_revenue:.2f}")

    st.divider()
    for l in listings:
        st.write(f"🪙 {l['title']} — ${l['price']:.2f}")
        st.caption(f"Trend: {l['trend']} | Timestamp: {l['timestamp']}")

if __name__ == "__main__":
    main()
