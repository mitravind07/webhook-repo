# Webhook + GitHub Actions Demo

This project contains:

- A simple webhook receiver using Flask to listen for GitHub events
- A GitHub Actions pipeline for CI/CD
- Optional: Merge detection for brownie points ✅

## 💻 Setup Instructions

### For Webhook:
1. Install dependencies:
```bash
pip install flask
```

2. Run server:
```bash
python server.py
```

3. Use ngrok to expose your localhost:
```bash
ngrok http 5000
```

4. Add the ngrok URL to your GitHub repo webhook settings.

---

## ✅ GitHub Actions (action-repo)
See `.github/workflows/main.yml` for a basic CI pipeline triggered on push.

---

## 📬 Supported Events:
- Push events
- Pull request merge events (bonus)

---

## 📂 Repos
- Action repo: [your-action-repo-link]
- Webhook repo: [your-webhook-repo-link]
