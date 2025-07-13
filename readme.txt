# 🧠 Etsy Commander 205 — AI-Powered Digital Product Engine

Welcome to **Etsy Commander 205**: a fully autonomous, multi-agent system designed to launch, manage, and scale digital product stores on Etsy and beyond.

Built to support ethical, humanlike automation using AI teams, competitive pricing, customer service, and growth management — all integrated with Google Cloud and GitHub.

---

## 🚀 Features

- 🤖 AI Agent Team: CEO, CMO, CTO, CX, CFO, GrowthHub, and CUA (Compliance)
- 🎨 Automated listing generation (title, image, description)
- 💵 Competitor-beating pricing strategy
- 📦 Digital product ZIP packager
- 🧾 Etsy Browser Bot (via Playwright, no API required)
- 📊 Streamlit Dashboard (growth counter, revenue estimates)
- 🌐 Cloud deployable via Docker + Google Cloud Run

---

## 📂 Directory Structure

```
etsy_commander/
├── uploader/             # JSON listings for upload
├── delivery/             # ZIP product bundles
├── store_profiles/       # Store configuration files
├── etsy_browser_bot.py   # Playwright upload bot
├── growth_dashboard.py   # Streamlit dashboard
├── product_packager.py   # ZIP file builder
├── Dockerfile            # Container config
└── launch_cloud_run.sh   # Full deploy script
```

---

## 🧪 Local Preview

```bash
pip install streamlit playwright
playwright install chromium
streamlit run growth_dashboard.py
```

> Visit http://localhost:8501 to view dashboard

---

## 🐳 Cloud Deployment (Google Cloud)

```bash
chmod +x launch_cloud_run.sh
./launch_cloud_run.sh
```

Requires:
- Google Cloud SDK
- Logged-in account with billing + deploy rights
- GitHub repo access

---

## 🛠 Future Enhancements

- 🔁 Etsy API fallback mode
- 🛒 Amazon/eBay/Gumroad sync
- 📬 Email delivery + PDF watermarks
- 🧾 Invoicing & payout automation (Payoneer, Wise)

---

## 👑 License & Credits

Built with ❤️ by [laziestlarry](https://github.com/laziestlarry) & ChatGPT (OpenAI). Ethical automation only.

MIT License.
