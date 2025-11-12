# Deploy to Render - Step by Step Guide

## Overview
Render is the fastest way to deploy your Dash app. **No credit card required for free tier**, and your app will be live in minutes.

## Prerequisites
- GitHub account (free at github.com)
- Render account (free at render.com)
- Your code pushed to GitHub

## Step 1: Push Your Code to GitHub

### 1.1 Create a GitHub Repository

If you don't have one yet:
1. Go to github.com
2. Click "New repository"
3. Name it: `pink-morsel-dashboard`
4. Click "Create repository"

### 1.2 Push Your Code

```bash
# Initialize git if not already done
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: Pink Morsel Sales Dashboard"

# Add GitHub remote (replace YOUR_USERNAME and REPO_NAME)
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**Verify:** Go to GitHub and confirm your files are there.

---

## Step 2: Create Render Account

1. Go to **render.com**
2. Click "Sign up"
3. Sign in with GitHub (recommended for easy integration)

---

## Step 3: Deploy to Render

### 3.1 Create a New Web Service

1. Dashboard → Click **"New +"** → Select **"Web Service"**
2. Click **"Connect"** next to your GitHub repository
3. You may be asked to authorize Render to access your GitHub

### 3.2 Configure the Service

Fill in the following fields:

| Field | Value |
|-------|-------|
| **Name** | `pink-morsel-dashboard` |
| **Environment** | `Python 3` |
| **Region** | Choose closest to you |
| **Branch** | `main` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:server` |

### 3.3 Select Plan

- **Free Plan** ✅ (recommended for demo)
  - Auto-pauses after 15 minutes of inactivity
  - Restarts automatically when accessed
  - No cost

- **Paid Plan** ($7/month)
  - Keeps app always running
  - Better performance

Choose **"Free"** to start.

### 3.4 Deploy

Click **"Create Web Service"**

**Wait 2-3 minutes for build and deployment...**

---

## Step 4: Access Your App

Once deployment completes:

1. You'll see a URL like: `https://pink-morsel-dashboard.onrender.com`
2. Click the link to view your live dashboard
3. **Share this URL with anyone!** They can now view your dashboard

---

## Troubleshooting

### App Won't Start?

**Check the logs:** Dashboard → Logs tab

**Common issues:**

| Error | Solution |
|-------|----------|
| "ModuleNotFoundError" | Add missing package to `requirements.txt`, commit & push |
| "Port already in use" | App is already using `app.run()` with port - should be fixed |
| "Data file not found" | Ensure `data/processed_sales.csv` is committed to git |

### App Crashes After Deploy?

1. Check logs for error messages
2. Verify `requirements.txt` has all dependencies
3. Make sure `app:server` references are correct

### How to Update?

Simply push updates to GitHub:

```bash
git add .
git commit -m "Updated dashboard"
git push
```

Render will **automatically redeploy** within seconds.

---

## Next Steps

### Optional: Custom Domain

Upgrade to paid plan and add custom domain:
1. Dashboard → Settings
2. Add custom domain (e.g., `morsel-analytics.com`)

### Optional: Environment Variables

For production settings, add environment variables:

1. Dashboard → Environment
2. Add:
   - `DEBUG` = `false`
   - Custom API keys, database URLs, etc.

### Monitor Your App

- **Logs**: Real-time app logs
- **Metrics**: CPU, memory usage
- **Analytics**: Page views (on paid plans)

---

## Success Indicators

✅ Deployment completes without errors  
✅ URL is accessible and shows dashboard  
✅ Region filter works  
✅ Charts load and update  
✅ Hover tooltips work  

Your dashboard is now live! 🎉

---

## Need Help?

**Render Documentation**: docs.render.com  
**Dash Documentation**: dash.plotly.com  
**GitHub Docs**: docs.github.com  

Good luck! 🚀
