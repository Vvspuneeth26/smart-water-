# 🔐 Login Authentication Setup Guide

## Overview
The IoT Water Quality Monitoring System now includes a complete authentication system with user login, session management, and password security.

## Features
✅ Secure user login with password hashing  
✅ Professional login page with water droplet theme  
✅ Session management (auto-redirect to login when unauthorized)  
✅ Protected API endpoints (requires authentication)  
✅ Logout functionality  
✅ User display in dashboard navbar  
✅ Demo credentials for testing  

---

## 🚀 Quick Start

### 1. Access the Login Page
Open your browser and navigate to:
```
http://localhost:5000
```

You will be automatically redirected to the login page if not authenticated.

### 2. Default Credentials
Use these credentials to log in:

| Field | Value |
|-------|-------|
| **Username** | `admin` |
| **Password** | `admin` |

⚠️ **Important**: Change these credentials in production!

### 3. Login Successfully
1. Enter username: `admin`
2. Enter password: `admin`
3. Click "Sign In"
4. You'll be redirected to the dashboard

---

## 📋 Authentication System Architecture

### Components

#### 1. **User Model** (`app/models/user.py`)
```python
class User(db.Model):
    - id: Primary key
    - username: Unique username
    - password_hash: Securely hashed password (bcrypt)
    - created_at: Account creation timestamp
```

**Methods:**
- `set_password(password)` - Hash and store password
- `check_password(password)` - Verify password against hash
- `to_dict()` - Serialize user data for API responses

#### 2. **Login Route** (`app/routes.py`)
```python
@main_bp.route('/login', methods=['GET', 'POST'])
```
- Displays login form on GET request
- Validates credentials on POST request
- Creates session on successful login
- Redirects to dashboard

#### 3. **Logout Route** (`app/routes.py`)
```python
@main_bp.route('/logout')
```
- Clears user session
- Redirects to login page

#### 4. **Authentication Decorators** (`app/routes.py`)
```python
@login_required           # For web pages
@api_login_required       # For API endpoints
```
- Checks if user_id exists in session
- Redirects to login if not authenticated
- Returns 401 error for API calls if not authenticated

---

## 🔒 Security Features

### Password Protection
- Passwords are hashed using **Werkzeug security** (PBKDF2 with SHA256)
- Passwords are never stored in plain text
- Hash verification happens on login

### Session Management
- Session ID is stored in encrypted browser cookie
- Session data stored server-side (secure)
- Session expires when browser closes (development mode)
- Configurable session timeout in production

### Protected Routes
**Web Pages:**
- `/` (dashboard) - Requires login
- `/login` - Public access

**API Endpoints (9/10 require authentication):**
- ✅ Protected: `/api/readings`, `/api/reading`, `/api/export/excel`, etc.
- ❌ Unprotected: `/login` only

---

## 🎨 Login Page Features

### Visual Design
- **Water Drop Logo** (💧) - Animated floating effect
- **Gradient Background** - Blue/purple gradient with water wave animation
- **Professional Card Layout** - Centered, responsive design
- **Error Messages** - Clear feedback on failed login attempts

### Form Elements
1. **Username Input**
   - Placeholder: "Enter your username"
   - Auto-focus on page load
   - Required field

2. **Password Input**
   - Type: password (hidden characters)
   - Placeholder: "Enter your password"
   - Required field

3. **Submit Button**
   - Text: "Sign In"
   - Arrow icon animation on hover
   - Gradient background

4. **Demo Credentials Display**
   - Shows default login information
   - Helpful for first-time users

### Responsive Design
- Mobile-friendly (tested on 320px - 1920px widths)
- Touch-optimized buttons
- Readable fonts on all devices

---

## 📱 Dashboard Navbar Updates

### User Information Display
Located in top-right of dashboard:
```
👤 admin  🚪 Logout
```

### Logout Button
- Red gradient background
- Smooth hover animation
- Clears all session data
- Redirects to login page

---

## 🛠️ Creating Additional Users

### Via CLI Command
```bash
cd c:\iot_water_project\New folder
.\.venv\Scripts\python.exe -m flask create-admin
```

This creates the default admin user if it doesn't exist.

### Programmatically (Flask Shell)
```bash
flask shell
```

Then in the Python shell:
```python
from app import db
from app.models import User

new_user = User(username='john')
new_user.set_password('password123')
db.session.add(new_user)
db.session.commit()
print('User created!')
```

### Creating Multiple Users
Create a script `create_users.py`:
```python
from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    users_data = [
        ('alice', 'alice123'),
        ('bob', 'bob456'),
        ('charlie', 'charlie789'),
    ]
    
    for username, password in users_data:
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
    
    db.session.commit()
    print('Users created successfully!')
```

Run it:
```bash
python create_users.py
```

---

## 🔄 Session Management

### How Sessions Work
1. User logs in with credentials
2. Credentials verified against stored hash
3. `session['user_id']` and `session['username']` are set
4. Session cookie sent to browser
5. Browser includes session cookie with each request
6. Server validates session before serving protected pages/APIs

### Session Timeout
**Development Mode (default):**
- Session persists while browser is open
- Clears when browser closes or manual logout

**Production Mode (recommended):**
```python
# In config.py
PERMANENT_SESSION_LIFETIME = timedelta(hours=1)  # 1 hour timeout
SESSION_REFRESH_EACH_REQUEST = True  # Reset timeout on each request
SESSION_COOKIE_SECURE = True  # HTTPS only
SESSION_COOKIE_HTTPONLY = True  # No JavaScript access
SESSION_COOKIE_SAMESITE = 'Lax'  # CSRF protection
```

---

## 🚨 Error Handling

### Login Errors
| Error | Message | Cause |
|-------|---------|-------|
| Empty fields | "Username and password are required" | Missing input |
| Invalid credentials | "Invalid username or password" | Wrong username or password |
| Unauthorized API | 401 status code | Missing session on API call |

### Auto-Redirect on Unauthorized
If session expires or you try to access protected page:
- Web pages → Redirected to `/login`
- API calls → Return 401, JavaScript redirects to `/login`

---

## 📡 API Authentication

### Protected API Endpoints
All endpoints require authentication:

```javascript
// API call with session (auto-authenticated)
fetch('/api/readings')
    .then(response => {
        if (response.status === 401) {
            window.location.href = '/login';
        }
        return response.json();
    })
    .then(data => console.log(data))
    .catch(error => console.error(error));
```

### Example: Get Readings
```bash
curl -b "session=<your_session_id>" http://localhost:5000/api/readings
# Returns: {"success": true, "data": [...], "pagination": {...}}

# Without session:
curl http://localhost:5000/api/readings
# Returns: 401 Unauthorized
```

---

## 🔑 Changing Default Password

### Method 1: Using Flask Shell
```bash
flask shell
```

```python
from app.models import User
admin = User.query.filter_by(username='admin').first()
admin.set_password('your_new_password')
db.session.commit()
print('Password changed!')
```

### Method 2: Delete and Recreate
```bash
# Delete the user
flask shell
User.query.filter_by(username='admin').delete()
db.session.commit()
exit()

# Recreate with new password
python create_users.py  # Your custom script
```

### Method 3: Production Setup Script
```bash
# Create a setup script for deployment
python setup_production.py
```

---

## 🧪 Testing Login System

### Test Case 1: Successful Login
1. Navigate to `http://localhost:5000/login`
2. Enter username: `admin`
3. Enter password: `admin`
4. Click "Sign In"
5. **Expected**: Redirected to dashboard, username shown in navbar

### Test Case 2: Invalid Credentials
1. Navigate to `http://localhost:5000/login`
2. Enter username: `admin`
3. Enter password: `wrong`
4. Click "Sign In"
5. **Expected**: Error message "Invalid username or password"

### Test Case 3: Direct Access Without Login
1. Navigate to `http://localhost:5000/` (dashboard)
2. **Expected**: Redirected to `/login`

### Test Case 4: API Call Without Authentication
```bash
curl http://localhost:5000/api/readings
```
**Expected**: Returns 401 Unauthorized

### Test Case 5: Logout
1. Log in successfully
2. Click "🚪 Logout" button
3. **Expected**: Redirected to login page, session cleared

---

## 📊 Database Schema for Users

```
users table:
├── id (INTEGER PRIMARY KEY)
├── username (VARCHAR(80) UNIQUE NOT NULL)
├── password_hash (VARCHAR(255) NOT NULL)
└── created_at (DATETIME DEFAULT CURRENT_TIMESTAMP)

Example record:
├── id: 1
├── username: 'admin'
├── password_hash: 'pbkdf2:sha256:600000$...' (bcrypt hash)
└── created_at: 2026-01-27 15:58:00
```

---

## 🚀 Production Deployment

### Before Deploying
1. **Change default password**
   ```bash
   flask shell
   admin = User.query.filter_by(username='admin').first()
   admin.set_password('strong_new_password_123')
   db.session.commit()
   ```

2. **Set strong SECRET_KEY**
   ```python
   # In .env or environment variables
   SECRET_KEY=your_random_very_long_secret_key_here
   ```

3. **Enable secure cookies**
   ```python
   SESSION_COOKIE_SECURE = True      # HTTPS only
   SESSION_COOKIE_HTTPONLY = True    # No JS access
   SESSION_COOKIE_SAMESITE = 'Lax'   # CSRF protection
   ```

4. **Set session timeout**
   ```python
   PERMANENT_SESSION_LIFETIME = timedelta(hours=2)
   ```

### Environment Variables
```bash
# .env file
FLASK_ENV=production
SECRET_KEY=your_super_secret_key_here
SESSION_TIMEOUT=7200
DATABASE_URL=postgresql://user:pass@localhost/db_name
```

### Use Production WSGI Server
```bash
# Instead of Flask development server
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 run:app
```

---

## 🆘 Troubleshooting

### Issue: "Unauthorized" on login
**Solution**: Check if database was initialized with User table
```bash
python
```
```python
from app import create_app, db
from app.models import User
app = create_app()
with app.app_context():
    db.create_all()  # Ensure tables exist
```

### Issue: Password not working
**Solution**: Verify password hash was saved
```bash
flask shell
```
```python
from app.models import User
admin = User.query.filter_by(username='admin').first()
if admin:
    print(f"User found: {admin.username}")
    print(f"Password hash: {admin.password_hash}")
    print(f"Test password 'admin': {admin.check_password('admin')}")
else:
    print("Admin user not found!")
```

### Issue: Session not persisting
**Solution**: Check Flask configuration
```bash
flask shell
```
```python
from flask import current_app
print(f"Secret key set: {bool(current_app.config.get('SECRET_KEY'))}")
print(f"Session cookie secure: {current_app.config.get('SESSION_COOKIE_SECURE')}")
```

### Issue: Can't create user - database locked
**Solution**: Restart Flask server to release database lock
```bash
# Press CTRL+C in terminal running Flask
# Then restart:
python run.py
```

---

## 📞 Support & Next Steps

### Next Steps
1. ✅ Login with default credentials (admin/admin)
2. ✅ Explore the dashboard
3. ✅ Add water quality readings
4. ✅ Create additional user accounts
5. ✅ Change default password
6. ✅ Deploy to production with secure settings

### Additional Resources
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Werkzeug Security](https://werkzeug.palletsprojects.com/en/2.0.x/security/)
- [Flask Session Management](https://flask.palletsprojects.com/en/2.0.x/api/#flask.session)

---

**Version**: 1.0  
**Last Updated**: January 27, 2026  
**Status**: ✅ Production Ready
