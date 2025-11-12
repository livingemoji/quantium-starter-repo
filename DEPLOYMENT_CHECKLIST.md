# Pre-Deployment Checklist

## ✅ Production Readiness

### Code Configuration
- [x] `app.py` updated with `server = app.server` for gunicorn
- [x] `app.py` uses `os.environ.get('PORT')` for Render compatibility
- [x] `app.py` has `host='0.0.0.0'` for external access
- [x] `app.py` debug mode set to `False` for production
- [x] Environment variable support for DEBUG and PORT

### Dependencies
- [x] `requirements.txt` includes gunicorn
- [x] `requirements.txt` includes plotly
- [x] `requirements.txt` includes dash[testing]
- [x] All required packages available

### Data
- [x] `data/processed_sales.csv` exists with Pink Morsel sales data
- [x] Data file is committed to git repository

### Tests
- [x] `test_app.py` has 4 passing tests
- [x] CI scripts verify all tests pass
- [x] Dashboard components present and functional

### Documentation
- [x] `README.md` includes deployment instructions
- [x] `DEPLOY_RENDER.md` provides step-by-step guide
- [x] `HOSTING.md` explains various hosting options
- [x] `HOSTING_QUICKSTART.md` provides quick reference

### Git Repository
- [ ] GitHub repository created
- [ ] Code pushed to GitHub
- [ ] All files committed (`.gitignore` excludes venv, __pycache__, etc.)

---

## 🚀 Render Deployment Checklist

### Before Deployment
- [ ] All changes committed and pushed to GitHub
- [ ] GitHub repository is public (or Render has access)
- [ ] Render account created

### During Deployment
- [ ] Service name: `pink-morsel-dashboard`
- [ ] Environment: `Python 3`
- [ ] Build command: `pip install -r requirements.txt`
- [ ] Start command: `gunicorn app:server`
- [ ] Plan: Free (for testing)
- [ ] Region: Selected (closer = faster)

### After Deployment
- [ ] Build completes successfully
- [ ] App URL provided by Render
- [ ] Access app and verify it loads
- [ ] Test region filter works
- [ ] Test chart displays correctly
- [ ] Test hover tooltips work
- [ ] Confirm no console errors

---

## 📋 What Gets Deployed

```
pink-morsel-dashboard/
├── app.py                      ✓ Main dashboard app
├── test_app.py                 ✓ Tests (not executed)
├── requirements.txt            ✓ Python dependencies
├── data/
│   └── processed_sales.csv     ✓ Sales data
├── scripts/
│   └── process_sales.py        ✓ Data processing
├── README.md                   ✓ Documentation
├── HOSTING.md                  ✓ Hosting guide
├── DEPLOY_RENDER.md            ✓ Render guide
├── run_tests.bat               ✓ CI script
└── run_tests.sh                ✓ CI script
```

Note: `.venv/` and `__pycache__/` are excluded via `.gitignore`

---

## 🔗 Quick Links

- **Render**: https://render.com
- **GitHub**: https://github.com
- **Dash Docs**: https://dash.plotly.com/
- **Gunicorn Docs**: https://gunicorn.org/

---

## 📊 Your Deployment Info (Save This)

After successful deployment, save:

```
App Name: pink-morsel-dashboard
Render URL: https://pink-morsel-dashboard.onrender.com
GitHub Repo: https://github.com/YOUR_USERNAME/pink-morsel-dashboard
Deployment Date: [DATE]
```

---

## ❓ Common Questions

**Q: Will my app go down?**  
A: Free tier apps pause after 15 min of inactivity. First request takes ~5 seconds to wake up.

**Q: Can I update the app?**  
A: Yes! Just `git push` and Render auto-redeploys.

**Q: What if something breaks?**  
A: Check Render logs, fix issue, commit, push, redeploy.

**Q: How much will it cost?**  
A: Free tier is completely free. $7/month gets always-on.

**Q: Can I use a custom domain?**  
A: Yes, on paid plans ($7/month+).

---

## ✨ After Deployment

Once live, you can:

1. Share the URL with colleagues/clients
2. Embed in a web page with an iframe
3. Upgrade to paid plan for always-on performance
4. Add authentication if needed
5. Monitor usage with Render analytics

---

**Ready to deploy? Follow the steps in `DEPLOY_RENDER.md` →**
