# Quick Start: Host Your Dashboard

## TL;DR - Hosting in 3 Steps

### Step 1: Prepare for Production
```bash
pip install gunicorn
pip freeze > requirements.txt
```

### Step 2: Update `app.py` (last 2 lines)
```python
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
```

### Step 3: Deploy to Render
1. Push code to GitHub
2. Go to render.com
3. Click "New Web Service"
4. Select your repo
5. Set start command: `gunicorn app:server`
6. Deploy!

**Your app is live in ~5 minutes**

## Platform Comparison

| Platform | Setup Time | Cost | Best For |
|----------|-----------|------|----------|
| **Render** ⭐ | 5 min | Free | Quick demos |
| Heroku | 10 min | $7/mo | Learners |
| PythonAnywhere | 5 min | $5/mo | Simplicity |
| Google Cloud Run | 20 min | Free tier | Scale |
| AWS Beanstalk | 30 min | Free tier | Enterprise |

## Environment Variable for Port

Hosting platforms assign dynamic ports. Use this in `app.py`:

```python
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=False, host='0.0.0.0', port=port)
```

## Common Issues & Solutions

**Q: App crashes on startup?**  
A: Missing dependencies. Run `pip freeze > requirements.txt`

**Q: Can't access app after deploying?**  
A: Check it's using `host='0.0.0.0'` not `localhost`

**Q: Slow performance?**  
A: Scale up plan or switch to Google Cloud Run for auto-scaling

## Files Needed for Hosting

```
your-app/
├── app.py              ✓ (exists)
├── requirements.txt    ✓ (exists)
├── data/
│   └── processed_sales.csv  ✓ (exists)
├── Procfile            ← Create for Heroku only
└── Dockerfile          ← Create for Google Cloud Run only
```

For **Render**: No extra files needed!

---

**Ready to go live?** See detailed instructions in [`HOSTING.md`](HOSTING.md)
