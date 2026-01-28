# 🔐 LOGIN QUICK REFERENCE

## In 10 Seconds

### Open Website
```
http://localhost:5000
```

### You'll See
```
🔐 Water Quality Monitor Login Page
💧 Water drop logo (animated)
```

### Enter Credentials
```
Username: admin
Password: admin
```

### Click "Sign In"
```
✓ You're logged in!
✓ See "👤 admin" in top-right
✓ Click "🚪 Logout" to sign out
```

---

## 📝 Creating New Users

### Via Python
```python
flask shell
from app.models import User
from app import db

user = User(username='john')
user.set_password('password123')
db.session.add(user)
db.session.commit()
```

### Via CLI
```bash
python -m flask create-admin  # For admin user
```

---

## 🔑 Default Login

| Field | Value |
|-------|-------|
| Username | `admin` |
| Password | `admin` |

⚠️ **Change in production!**

---

## 🎯 Main Features

| Feature | Where |
|---------|-------|
| Login | http://localhost:5000/login |
| Dashboard | http://localhost:5000/ |
| Logout | Top-right "🚪 Logout" button |
| User Info | Top-right "👤 admin" |

---

## ❓ Common Issues

| Issue | Fix |
|-------|-----|
| "Can't login" | Make sure you enter admin/admin |
| "Unauthorized" | Refresh page and login again |
| "Dashboard blank" | Check browser console (F12) |
| "Forgot password" | Delete user and create new one |

---

## 📚 Full Guide

See **LOGIN_SETUP.md** for:
- Detailed setup instructions
- API authentication
- Password security
- Production deployment
- Troubleshooting

---

**Status**: ✅ Ready to Use
