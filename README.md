# IoT Water Quality Monitoring System

A comprehensive Flask-based web application for real-time water quality monitoring with automatic GPS-based location detection, data storage, visualization, and Excel export capabilities.

## 🔐 Authentication System

This application now includes a **secure login authentication system**:

- **Secure Login Page** - Professional water-themed login interface
- **Password Protection** - Bcrypt hashing with PBKDF2-SHA256
- **Session Management** - Server-side session storage
- **Protected API Endpoints** - All API calls require authentication
- **User Dashboard** - Display logged-in user with logout button

### Quick Login
```
URL: http://localhost:5000
Username: admin
Password: admin
```

⚠️ **Change default password in production!**

For detailed authentication documentation, see [LOGIN_SETUP.md](LOGIN_SETUP.md) or [AUTHENTICATION_SUMMARY.md](AUTHENTICATION_SUMMARY.md)

---

## Features

### Core Features
✅ **Real-Time Data Acquisition** - Receive water quality parameters from IoT sensor nodes
✅ **Secure Authentication** - Login system with password protection
✅ **Automatic GPS Detection** - Browser-based geolocation API for automatic latitude/longitude capture
✅ **Database Storage** - SQLite database with efficient data management
✅ **Data Visualization** - Real-time tabular display with live updates
✅ **Excel Export** - Download data in .xlsx format with professional formatting
✅ **Advanced Filtering** - Filter by water type, date range, and location
✅ **Responsive Design** - Mobile-friendly interface for field deployment

### Water Quality Parameters
- **Chlorophyll Concentration** (mg/L) - Primary photosynthetic pigment indicator
- **Pigments** (mg/L) - Supporting photosynthetic pigments
- **Total Alkalinity** (mg/L as CaCO₃) - Water hardness indicator
- **Dissolved Inorganic Carbon (DIC)** (mmol/L) - Carbon cycling indicator
- **Temperature** (°C) - Environmental parameter

### Water Sources
- Drinking Water
- Groundwater
- Ocean Water

## Project Structure

```
.
├── run.py                 # Application entry point
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
└── app/
    ├── __init__.py       # Flask app factory
    ├── routes.py         # API and web routes
    ├── models/
    │   ├── __init__.py
    │   ├── water_reading.py  # Water quality data model
    │   └── user.py           # User authentication model (NEW)
    ├── templates/
    │   ├── login.html    # Login page (NEW)
    │   └── index.html    # Main dashboard
    └── static/
        ├── css/
        │   ├── style.css     # Dashboard styling
        │   └── login.css     # Login page styling (NEW)
        └── js/
            └── app.js       # Frontend logic
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone or Extract Project**
   ```bash
   cd iot_water_project
   ```

2. **Create Virtual Environment** (Recommended)
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize Database**
   ```bash
   flask --app run init-db
   ```

5. **Seed Sample Data** (Optional)
   ```bash
   flask --app run seed-db
   ```

6. **Run Application**
   ```bash
   python run.py
   ```

7. **Access Web Interface**
   - Open browser: `http://localhost:5000`

## Usage Guide

### Adding Water Quality Readings

1. **Detect GPS Location**
   - Click the "🔍 Detect Location" button
   - Grant browser permission for geolocation
   - Latitude and longitude will auto-populate

2. **Select Water Type**
   - Choose from: Drinking Water, Groundwater, or Ocean Water

3. **Enter Parameters**
   - Input water quality measurements from IoT sensors
   - All sensor readings are optional except location

4. **Submit Data**
   - Click "Submit Reading"
   - Data is stored with automatic timestamp

### Viewing and Filtering Data

1. **Real-Time Dashboard**
   - View all submitted readings in table format
   - Statistics show average values and record count

2. **Apply Filters**
   - Filter by water type
   - Select date range (start and end dates)
   - Sort by different parameters
   - Click "Apply Filters" to update view

3. **Pagination**
   - Navigate through records using pagination controls
   - 20 records per page

### Exporting Data

1. **Excel Export**
   - Click "📊 Download Excel (.xlsx)"
   - Export includes all filtered data
   - Professional formatting with headers and column widths

2. **File Information**
   - Filename: `water_quality_data_YYYYMMDD_HHMMSS.xlsx`
   - All columns included with units

### Viewing Locations

1. **Measurement Points**
   - See all GPS-detected measurement locations
   - Organized by water type
   - Can be integrated with mapping libraries (Leaflet.js, Google Maps)

## API Endpoints

### Reading Management
- `GET /api/readings` - Get all readings with filtering/sorting
- `POST /api/reading` - Create new reading
- `GET /api/reading/<id>` - Get specific reading
- `PUT /api/reading/<id>` - Update reading
- `DELETE /api/reading/<id>` - Delete reading

### Data Export
- `GET /api/export/excel` - Export data to Excel

### Statistics & Info
- `GET /api/stats` - Get system statistics
- `GET /api/locations` - Get all measurement locations

### Request/Response Format

**Create Reading (POST /api/reading)**
```json
{
  "timestamp": "2024-01-27T10:30:00",
  "latitude": 40.7128,
  "longitude": -74.0060,
  "water_type": "drinking",
  "chlorophyll": 25.5,
  "pigments": 12.3,
  "total_alkalinity": 150.0,
  "dic": 2.5,
  "temperature": 22.5,
  "sensor_id": "SENSOR-001"
}
```

**Response (Success)**
```json
{
  "success": true,
  "message": "Reading created successfully",
  "data": {
    "id": 1,
    "timestamp": "2024-01-27T10:30:00",
    "date": "2024-01-27",
    "time": "10:30:00",
    ...
  }
}
```

## Browser Compatibility

✅ Chrome/Edge (Full support)
✅ Firefox (Full support)
✅ Safari (Full support)
✅ Mobile browsers (Responsive design)

**Note:** Geolocation requires HTTPS in production or localhost in development

## Technologies Used

- **Backend**: Flask 2.3.0, SQLAlchemy
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Database**: SQLite
- **Export**: OpenPyXL (Excel generation)
- **APIs**: Browser Geolocation API, RESTful API

## Configuration

Edit `config.py` to modify settings:

```python
# Database
SQLALCHEMY_DATABASE_URI = 'sqlite:///water_quality.db'

# Environment
DEBUG = True/False

# Security
SECRET_KEY = 'your-secret-key'
```

## Advanced Features

### Optional Enhancements

1. **Map Integration** (Leaflet.js)
   - Add to `index.html`
   - Interactive map with marker clustering

2. **Real-time WebSocket** (Flask-SocketIO)
   - Live data updates without refresh
   - Real-time notifications

3. **Authentication** (Flask-Login)
   - User accounts and roles
   - Data access control

4. **Analytics** (Plotly/Chart.js)
   - Trend visualization
   - Parameter correlation analysis

5. **Mobile App** (React Native/Flutter)
   - Native mobile application
   - Offline data sync

## Troubleshooting

### GPS Not Working
- Ensure browser has geolocation permission
- HTTPS required in production
- Check browser console for errors

### Database Issues
- Delete `instance/water_quality.db` and reinitialize
- Check file permissions in project directory
- Verify SQLite installation

### Port Already in Use
- Change port in `run.py`: `app.run(port=5001)`
- Or kill process using port 5000

## Performance Tips

- Database indexes on `timestamp` and `water_type` for fast queries
- Pagination (20 records) for optimal table performance
- Static file caching headers configured
- Efficient AJAX requests for real-time updates

## Security Considerations

- Validate all user inputs
- Use environment variables for sensitive config
- Implement CORS for production API access
- Add authentication for production deployment
- Use HTTPS in production

## Future Roadmap

- [ ] User authentication and authorization
- [ ] Advanced data analytics dashboard
- [ ] Real-time WebSocket updates
- [ ] Mobile native application
- [ ] Cloud deployment (AWS, Heroku, Azure)
- [ ] IoT device management panel
- [ ] Automated alerts and notifications
- [ ] Multi-language support

## Support & Documentation

For issues, questions, or feature requests:
- Check browser console (F12) for errors
- Review Flask logs in terminal
- Test API endpoints with Postman
- Verify database integrity with SQLite Browser

## License

This project is open-source. Use freely for educational and research purposes.

## Version

**v1.0.0** - Initial Release (January 2026)

---

Built with ❤️ for environmental monitoring
