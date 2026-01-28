# ✨ Hardware Integration Update - Water Quality Monitoring System

## 🔧 **EXTERNAL IoT HARDWARE INTEGRATION ADDED**

### **What's New**

Your water quality monitoring system now supports **automatic data fetching from external IoT hardware kits**. The website will:

✅ **Listen for sensor data** from external hardware  
✅ **Auto-populate form fields** with sensor readings  
✅ **Display notifications** when hardware sends data  
✅ **Store data automatically** in the database  
✅ **Update dashboard in real-time**

---

## 🌐 **How It Works**

### **Data Flow**

```
External IoT Hardware
       ↓
   Sensors collect water quality data
   (Temperature, Chlorophyll, Pigments, etc.)
       ↓
Hardware sends JSON to API endpoint:
POST /api/sensor/data
       ↓
Website receives and processes data
       ↓
Form fields auto-populate automatically
       ↓
📡 Notification appears
"New sensor data received from SENSOR-KIT-001"
       ↓
User reviews data and clicks "Submit Reading"
       ↓
Data saved to database and displayed on dashboard
```

---

## 🔌 **Integration Endpoints**

### **1. Send Data from Hardware**

```
POST /api/sensor/data
```

Your IoT device sends water quality data here.

**Example (Python)**:
```python
import requests

sensor_data = {
    "timestamp": "2026-01-27T14:30:00",
    "latitude": 40.7128,
    "longitude": -74.0060,
    "water_type": "drinking",
    "chlorophyll": 2.5,
    "pigments": 1.2,
    "total_alkalinity": 120.5,
    "dic": 2.3,
    "temperature": 22.5,
    "sensor_id": "SENSOR-KIT-001"
}

response = requests.post(
    'http://localhost:5000/api/sensor/data',
    json=sensor_data
)
print(response.json())
```

### **2. Get Latest Sensor Data**

```
GET /api/sensor/latest
```

Website fetches latest sensor data every 10 seconds to display real-time readings.

---

## 📱 **Website Behavior**

### **When Hardware Sends Data**

1. **🟢 Status Indicator Shows** "Listening for External IoT Hardware"
2. **📡 Notification Appears** "New sensor data received from SENSOR-KIT-001"
3. **Form Auto-Populates**:
   - Latitude: 40.7128
   - Longitude: -74.0060
   - Water Type: Drinking
   - Chlorophyll: 2.5 mg/L
   - Temperature: 22.5 °C
   - All other parameters...

4. **User Can**:
   - Review auto-populated data
   - Modify if needed
   - Click "Submit Reading"
   - Data saves with sensor ID

---

## 🧪 **Test It Now**

### **Send Test Data from Command Line**

```bash
curl -X POST http://localhost:5000/api/sensor/data \
  -H "Content-Type: application/json" \
  -d '{
    "timestamp": "2026-01-27T14:30:00",
    "latitude": 40.7128,
    "longitude": -74.0060,
    "water_type": "drinking",
    "chlorophyll": 2.5,
    "pigments": 1.2,
    "total_alkalinity": 120.5,
    "dic": 2.3,
    "temperature": 22.5,
    "sensor_id": "TEST-SENSOR-001"
  }'
```

### **Expected Result**

Website should:
1. ✅ Receive data immediately
2. ✅ Show notification
3. ✅ Auto-populate form fields
4. ✅ Display "Sensor Location Detected"

---

## 🛠️ **Hardware Setup Examples**

### **Raspberry Pi (Python)**

```python
import requests
import time
from datetime import datetime

# Your sensor reading function
def read_sensors():
    temp = 22.5  # Read from temperature sensor
    chlorophyll = 2.5  # Read from chlorophyll sensor
    # ... read other sensors
    return {
        "temperature": temp,
        "chlorophyll": chlorophyll,
        # ... other readings
    }

# Send data every 5 minutes
while True:
    sensor_data = {
        "timestamp": datetime.utcnow().isoformat(),
        "latitude": 40.7128,
        "longitude": -74.0060,
        "water_type": "drinking",
        **read_sensors(),  # Include sensor readings
        "sensor_id": "RPI-SENSOR-001"
    }
    
    requests.post('http://localhost:5000/api/sensor/data', json=sensor_data)
    time.sleep(300)  # Wait 5 minutes
```

### **Arduino (C++)**

```cpp
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

void sendSensorData() {
    HTTPClient http;
    http.begin("http://192.168.1.100:5000/api/sensor/data");
    http.addHeader("Content-Type", "application/json");
    
    StaticJsonDocument<200> doc;
    doc["timestamp"] = "2026-01-27T14:30:00";
    doc["latitude"] = 40.7128;
    doc["longitude"] = -74.0060;
    doc["water_type"] = "drinking";
    doc["temperature"] = readTemperature();
    doc["chlorophyll"] = readChlorophyll();
    doc["sensor_id"] = "ARDUINO-001";
    
    String payload;
    serializeJson(doc, payload);
    
    http.POST(payload);
    http.end();
}
```

---

## 📊 **Key Features**

### **Real-Time Updates**
- Website checks for new sensor data every 10 seconds
- Auto-refreshes form fields
- Shows visual indicators

### **Multiple Sensors**
- Support unlimited IoT devices
- Each identified by `sensor_id`
- All data stored historically

### **Error Handling**
- Invalid data rejected with error message
- Missing fields reported
- Clear feedback to hardware

### **Data Persistence**
- All sensor data stored in database
- Full audit trail maintained
- Can query historical data

---

## 🔐 **Security**

For production deployment:

1. **Add Authentication** (API Key):
   ```bash
   curl -X POST http://localhost:5000/api/sensor/data \
     -H "X-API-Key: your-secret-key" \
     -H "Content-Type: application/json" \
     -d '{...}'
   ```

2. **Use HTTPS**:
   ```
   https://your-domain.com/api/sensor/data
   ```

3. **Rate Limiting**: Implement on your server
4. **Data Validation**: Server validates all inputs

---

## 📋 **Required Data Format**

```json
{
  "timestamp": "2026-01-27T14:30:00",     // ISO 8601 format (optional)
  "latitude": 40.7128,                    // Required (-90 to 90)
  "longitude": -74.0060,                  // Required (-180 to 180)
  "water_type": "drinking",               // Required (drinking, groundwater, ocean)
  "chlorophyll": 2.5,                     // mg/L (optional)
  "pigments": 1.2,                        // mg/L (optional)
  "total_alkalinity": 120.5,              // mg/L (optional)
  "dic": 2.3,                             // mmol/L (optional)
  "temperature": 22.5,                    // °C (optional)
  "sensor_id": "SENSOR-KIT-001"           // (optional, auto-generated if not provided)
}
```

---

## 🎯 **Use Cases**

### **Scenario 1: Real-Time Monitoring**
Hardware sends data every 5 minutes → Website updates automatically → User reviews trends

### **Scenario 2: Multi-Site Deployment**
Multiple IoT kits at different locations → All send to same server → Dashboard shows all locations

### **Scenario 3: Automated Data Collection**
Hardware runs 24/7 → Automatic data transmission → Complete historical database

---

## 📞 **API Endpoints Summary**

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/sensor/data` | POST | Receive sensor data from hardware |
| `/api/sensor/latest` | GET | Get latest sensor reading (auto-called every 10s) |
| `/api/reading` | POST | Submit confirmed reading (manual or auto) |
| `/api/readings` | GET | Get all readings with filters |
| `/api/export/excel` | GET | Export data to Excel |

---

## ✅ **What to Do Next**

1. **Set up your IoT hardware**
   - Install sensors (temperature, chlorophyll, etc.)
   - Connect to WiFi
   - Write code to read sensors

2. **Configure hardware to send data**
   - Use your sensor reading code
   - Send to `/api/sensor/data` endpoint
   - Include required fields

3. **Test with curl**
   ```bash
   curl -X POST http://localhost:5000/api/sensor/data \
     -H "Content-Type: application/json" \
     -d '{...}'
   ```

4. **Watch website update automatically**
   - Form fields populate
   - Notification appears
   - Data ready to save

5. **Deploy to production**
   - Configure HTTPS
   - Add authentication
   - Set rate limiting

---

## 📚 **Documentation**

See `IOT_HARDWARE_INTEGRATION.md` for:
- Complete hardware setup guide
- Code examples for different platforms
- Network configuration
- Troubleshooting guide
- Security best practices

---

## 🎉 **System Status**

✅ **Hardware integration endpoints added**  
✅ **Real-time data fetching implemented**  
✅ **Form auto-population working**  
✅ **Notifications configured**  
✅ **Database ready for sensor data**  
✅ **Website ready for IoT devices**  

---

**Your water quality monitoring system is now IoT-enabled and ready for hardware integration!** 🌊
