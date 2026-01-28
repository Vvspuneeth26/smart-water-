## IoT Water Quality Monitoring System - Quick Start Guide

### 🚀 Getting Started (5 minutes)

#### 1. **Verify Server is Running**
- Flask server running on `http://localhost:5000`
- Check terminal for "Running on http://127.0.0.1:5000"

#### 2. **Open Web Interface**
- Open browser to `http://localhost:5000`
- You should see the "IoT Water Quality Monitor" dashboard

#### 3. **Detect Your Location**
- Click the **"🔍 Detect Location"** button
- Grant browser permission for location access
- System displays:
  - ✅ Detected Latitude
  - ✅ Detected Longitude
  - ✅ GPS Accuracy (meters)
  - ✅ Last Updated time

#### 4. **Add Water Quality Reading**
- **Select Water Type**: Drinking / Groundwater / Ocean
- **Enter Parameters** (all optional except location):
  - Chlorophyll (mg/L): 0-50
  - Pigments (mg/L): 0-30
  - Total Alkalinity (mg/L): 50-200
  - DIC (mmol/L): 1-5
  - Temperature (°C): -10 to 40
  - Sensor ID: Optional tracking identifier
- Click **"Submit Reading"** button
- ✅ Confirmation message appears

#### 5. **View Data**
- Data appears in **"Water Quality Data"** table
- Shows all parameters with date, time, location
- Statistics update automatically

#### 6. **Filter & Search**
- Select **Water Type**: Filter by drinking/groundwater/ocean
- Set **Date Range**: Choose start and end dates
- **Sort By**: Choose sorting column
- Click **"Apply Filters"** to update table

#### 7. **Download Data**
- Click **"📊 Download Excel (.xlsx)"** button
- File downloads with professional formatting
- Includes headers, styling, auto-sized columns

---

### 📊 Dashboard Sections

#### Top Statistics
- **Total Readings**: Number of stored measurements
- **Avg Temperature**: Average water temperature
- **Avg Chlorophyll**: Average chlorophyll concentration
- **Water Type Sources**: Number of different water types

#### Water Quality Data Table
Columns: Date | Time | Lat | Lon | Type | Chlorophyll | Pigments | Alkalinity | DIC | Temperature | Sensor ID | Actions

#### Features
- **Pagination**: 20 rows per page
- **Delete**: Remove individual readings
- **Auto-refresh**: Updates every 30 seconds
- **Search**: Filter by multiple criteria

#### Map Section
- Shows all measurement locations
- Water type classification
- Plan future measurement points

---

### 🔌 API Usage (For IoT Devices)

#### Create Reading via HTTP POST
```bash
curl -X POST http://localhost:5000/api/reading \
  -H "Content-Type: application/json" \
  -d '{
    "timestamp": "2026-01-27T10:30:00",
    "latitude": 40.7128,
    "longitude": -74.0060,
    "water_type": "drinking",
    "chlorophyll": 2.5,
    "pigments": 1.2,
    "total_alkalinity": 120.5,
    "dic": 2.3,
    "temperature": 22.5,
    "sensor_id": "SENSOR-001"
  }'
```

#### Get Readings with Filters
```bash
curl "http://localhost:5000/api/readings?page=1&per_page=20&water_type=ocean"
```

#### Export Data
```bash
curl "http://localhost:5000/api/export/excel" -o water_data.xlsx
```

---

### 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| **GPS not detecting** | Check browser location permission in settings |
| **Port 5000 in use** | Close other apps or change port in run.py |
| **No data showing** | Click "Apply Filters" or refresh page |
| **Excel download fails** | Check internet, try smaller date range |
| **Server not responding** | Restart: Stop and run `python run.py` again |

---

### 📚 Additional Resources

- **Full Documentation**: See [README.md](README.md)
- **API Documentation**: Available in [app/routes.py](app/routes.py)
- **Configuration**: Edit [config.py](config.py)
- **Database**: `water_quality.db` (auto-created)

---

### 🔑 Key Features

✅ **Automatic GPS** - No manual location entry needed
✅ **Real-time Data** - Instant updates and statistics  
✅ **Mobile Friendly** - Works on phones and tablets
✅ **Excel Export** - Professional formatted downloads
✅ **RESTful API** - Easy IoT device integration
✅ **Advanced Filtering** - Find specific readings quickly
✅ **Error Messages** - Clear feedback on all actions

---

### 💡 Pro Tips

1. **For Field Work**: Ensure browser has GPS/location enabled before deployment
2. **Sample Data**: Run `flask --app run seed-db` to load 50 test readings
3. **Accuracy**: GPS accuracy depends on device and outdoor conditions
4. **Bulk Import**: Use API endpoint to upload data from IoT devices
5. **Backup**: Regularly download Excel exports for backup
6. **Testing**: Use different water types to test filtering

---

### ⚡ Server Commands

```bash
# Start server (already running)
python run.py

# Initialize empty database
flask --app run init-db

# Seed 50 sample readings
flask --app run seed-db

# Stop server
Press Ctrl+C in terminal
```

---

**Ready to monitor water quality?** Start adding readings now! 💧
