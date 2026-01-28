# 🔧 External IoT Hardware Integration Guide

## Connect Your Sensor Hardware to the Water Quality Monitoring System

The system now supports real-time data from external IoT hardware kits and sensors. Here's how to integrate your hardware:

---

## 📡 **API Endpoint for Hardware**

### **Receive Data from IoT Sensors**

**Endpoint**: `POST /api/sensor/data`

Your hardware should send water quality data to this endpoint in JSON format.

### **Request Format**

```json
{
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
```

### **Response**

**Success (201)**:
```json
{
  "success": true,
  "message": "Sensor data received and stored",
  "data": {
    "id": 1,
    "timestamp": "2026-01-27T14:30:00",
    "latitude": 40.7128,
    "longitude": -74.0060,
    "water_type": "drinking",
    ...
  }
}
```

**Error (400)**:
```json
{
  "success": false,
  "error": "Missing required field: latitude"
}
```

---

## 🔗 **Integration Examples**

### **Python - Raspberry Pi / Arduino**

```python
import requests
import json
from datetime import datetime

# Hardware sensor data
sensor_data = {
    "timestamp": datetime.utcnow().isoformat(),
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

# Send to website
response = requests.post(
    'http://localhost:5000/api/sensor/data',
    json=sensor_data,
    headers={'Content-Type': 'application/json'}
)

print(response.json())
```

### **cURL - Command Line**

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
    "sensor_id": "SENSOR-KIT-001"
  }'
```

### **Node.js / JavaScript**

```javascript
const sensorData = {
  timestamp: new Date().toISOString(),
  latitude: 40.7128,
  longitude: -74.0060,
  water_type: "drinking",
  chlorophyll: 2.5,
  pigments: 1.2,
  total_alkalinity: 120.5,
  dic: 2.3,
  temperature: 22.5,
  sensor_id: "SENSOR-KIT-001"
};

fetch('http://localhost:5000/api/sensor/data', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(sensorData)
})
.then(res => res.json())
.then(data => console.log(data));
```

### **Arduino C++**

```cpp
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

// WiFi credentials
const char* ssid = "YOUR_SSID";
const char* password = "YOUR_PASSWORD";
const char* serverUrl = "http://192.168.1.100:5000/api/sensor/data";

void sendSensorData(float temp, float chlorophyll, float lat, float lon) {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverUrl);
    http.addHeader("Content-Type", "application/json");
    
    // Create JSON
    StaticJsonDocument<200> doc;
    doc["timestamp"] = "2026-01-27T14:30:00";
    doc["latitude"] = lat;
    doc["longitude"] = lon;
    doc["water_type"] = "drinking";
    doc["temperature"] = temp;
    doc["chlorophyll"] = chlorophyll;
    doc["sensor_id"] = "SENSOR-KIT-001";
    
    String payload;
    serializeJson(doc, payload);
    
    int httpCode = http.POST(payload);
    String response = http.getString();
    
    Serial.println(response);
    http.end();
  }
}
```

---

## 🔌 **Hardware Setup**

### **Required Components**
- ✅ IoT Device (Raspberry Pi, Arduino, ESP32, etc.)
- ✅ Water Quality Sensors:
  - Chlorophyll sensor
  - pH/Alkalinity sensor
  - Temperature sensor
  - Conductivity sensor (optional)
- ✅ GPS Module (if location auto-detection needed)
- ✅ WiFi/Network Connection

### **Connection Diagram**

```
┌─────────────────────────────────┐
│  IoT Sensor Hardware            │
│  (Raspberry Pi/Arduino/ESP32)   │
│                                 │
│  ├─ Chlorophyll Sensor          │
│  ├─ Pigments Sensor             │
│  ├─ Alkalinity Sensor           │
│  ├─ DIC Sensor                  │
│  ├─ Temperature Sensor          │
│  └─ GPS Module                  │
└─────────────────────────────────┘
            │
            │ (WiFi/Ethernet)
            │
            ▼
┌─────────────────────────────────┐
│  Web Server (Flask)             │
│  http://localhost:5000          │
│                                 │
│  POST /api/sensor/data          │
│  GET /api/sensor/latest         │
│  POST /api/reading              │
└─────────────────────────────────┘
            │
            │ (Database Storage)
            │
            ▼
┌─────────────────────────────────┐
│  SQLite Database                │
│  Water Quality Readings         │
└─────────────────────────────────┘
            │
            │ (Display)
            │
            ▼
┌─────────────────────────────────┐
│  Web Browser                    │
│  http://localhost:5000          │
│  Real-Time Dashboard            │
└─────────────────────────────────┘
```

---

## 📊 **Real-Time Data Flow**

1. **Hardware Collects Data**
   - Sensors measure water quality parameters
   - GPS captures location coordinates

2. **Hardware Sends to Server**
   - POST request to `/api/sensor/data`
   - Includes timestamp and all parameters

3. **Server Stores Data**
   - Validates received data
   - Stores in SQLite database
   - Returns confirmation

4. **Website Updates Automatically**
   - JavaScript fetches latest sensor data every 10 seconds
   - Auto-populates form fields
   - Shows status notification
   - Updates dashboard in real-time

5. **User Reviews Data**
   - Form shows sensor values
   - User can modify if needed
   - Click "Submit Reading" to save
   - Data appears in table

---

## 🌍 **IP Address Configuration**

### **Local Network (Same WiFi)**

Replace `localhost:5000` with your server's local IP:

```
http://192.168.1.100:5000/api/sensor/data
```

Find your server IP:
```bash
# Windows
ipconfig

# macOS/Linux
ifconfig
```

### **Remote Access (Outside Network)**

1. Set up port forwarding on router
2. Use your public IP:
   ```
   http://YOUR_PUBLIC_IP:5000/api/sensor/data
   ```
3. Or use ngrok for tunneling:
   ```bash
   ngrok http 5000
   ```

---

## 🧪 **Testing the Integration**

### **Test with Sample Data**

```bash
# Send test data
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

# Check latest sensor data
curl http://localhost:5000/api/sensor/latest
```

### **Expected Behavior**

1. ✅ Form fields auto-populate with sensor data
2. ✅ Status shows "Sensor Location Detected"
3. ✅ Notification appears: "📡 New sensor data received"
4. ✅ Data appears in table after submission
5. ✅ Statistics update automatically

---

## 🔐 **Security Considerations**

### **For Production**
- ✅ Use HTTPS instead of HTTP
- ✅ Add API authentication tokens
- ✅ Implement rate limiting
- ✅ Validate sensor data ranges
- ✅ Use firewall rules

### **Example with Authentication**

```python
# Add API key to header
headers = {
    'Content-Type': 'application/json',
    'X-API-Key': 'your-secret-api-key'
}

response = requests.post(
    'http://localhost:5000/api/sensor/data',
    json=sensor_data,
    headers=headers
)
```

---

## 📈 **Data Parameters**

| Parameter | Type | Range | Unit | Required |
|-----------|------|-------|------|----------|
| timestamp | string | ISO 8601 | datetime | No |
| latitude | float | -90 to 90 | degrees | Yes |
| longitude | float | -180 to 180 | degrees | Yes |
| water_type | string | drinking, groundwater, ocean | - | Yes |
| chlorophyll | float | 0-50 | mg/L | No |
| pigments | float | 0-30 | mg/L | No |
| total_alkalinity | float | 0-500 | mg/L | No |
| dic | float | 0-10 | mmol/L | No |
| temperature | float | -20 to 50 | °C | No |
| sensor_id | string | any text | - | No |

---

## 🆘 **Troubleshooting**

| Problem | Solution |
|---------|----------|
| Connection refused | Check if server is running on correct IP/port |
| 400 Bad Request | Verify JSON format and required fields |
| Data not appearing | Check network connectivity and firewall |
| Form not auto-populating | Check browser console for errors |
| GPS not detecting | Ensure latitude/longitude in valid range |

---

## 📞 **Support**

- Check logs in terminal: `python run.py`
- Verify API with curl before hardware
- Test locally first, then network

---

## ✨ **Next Steps**

1. Set up your IoT hardware
2. Configure sensor connections
3. Write code to read sensors
4. Send data to `/api/sensor/data` endpoint
5. Watch data update on website in real-time
6. Export data for analysis

---

**Your water quality monitoring system is now IoT-enabled!** 🌊
