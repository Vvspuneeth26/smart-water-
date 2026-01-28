# 🔧 QUICK REFERENCE - Hardware Integration

## 📡 Send Data from Your IoT Hardware

### **Endpoint**
```
POST http://localhost:5000/api/sensor/data
```

### **Required Fields**
- `latitude` (float: -90 to 90)
- `longitude` (float: -180 to 180)  
- `water_type` (string: "drinking", "groundwater", or "ocean")

### **Optional Fields**
- `timestamp` (ISO 8601, auto-generated if missing)
- `chlorophyll` (float, mg/L)
- `pigments` (float, mg/L)
- `total_alkalinity` (float, mg/L)
- `dic` (float, mmol/L)
- `temperature` (float, °C)
- `sensor_id` (string, auto-generated if missing)

---

## 💻 **Code Examples**

### **Python**
```python
import requests

data = {
    "latitude": 40.7128,
    "longitude": -74.0060,
    "water_type": "drinking",
    "temperature": 22.5,
    "chlorophyll": 2.5,
    "sensor_id": "SENSOR-001"
}

r = requests.post('http://localhost:5000/api/sensor/data', json=data)
print(r.json())
```

### **cURL**
```bash
curl -X POST http://localhost:5000/api/sensor/data \
  -H "Content-Type: application/json" \
  -d '{
    "latitude": 40.7128,
    "longitude": -74.0060,
    "water_type": "drinking",
    "temperature": 22.5,
    "chlorophyll": 2.5,
    "sensor_id": "SENSOR-001"
  }'
```

### **JavaScript/Node.js**
```javascript
fetch('http://localhost:5000/api/sensor/data', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    latitude: 40.7128,
    longitude: -74.0060,
    water_type: "drinking",
    temperature: 22.5,
    chlorophyll: 2.5,
    sensor_id: "SENSOR-001"
  })
}).then(r => r.json()).then(console.log);
```

### **Arduino/C++**
```cpp
// Uses WiFi and ArduinoJson libraries
StaticJsonDocument<200> doc;
doc["latitude"] = 40.7128;
doc["longitude"] = -74.0060;
doc["water_type"] = "drinking";
doc["temperature"] = 22.5;
doc["chlorophyll"] = 2.5;
doc["sensor_id"] = "SENSOR-001";

String payload;
serializeJson(doc, payload);

HTTPClient http;
http.begin("http://192.168.1.100:5000/api/sensor/data");
http.addHeader("Content-Type", "application/json");
http.POST(payload);
```

---

## 🌐 **What Happens When Data Arrives**

1. ✅ Data received and validated
2. ✅ Stored in database
3. ✅ Website fetches new data (every 10 seconds)
4. ✅ Form fields auto-populate
5. ✅ Notification shows "📡 New sensor data received"
6. ✅ User can review and submit

---

## 📋 **Response Examples**

### **Success (201)**
```json
{
  "success": true,
  "message": "Sensor data received and stored",
  "data": {
    "id": 42,
    "timestamp": "2026-01-27T14:30:00",
    "latitude": 40.7128,
    "longitude": -74.0060,
    "water_type": "drinking",
    "temperature": 22.5,
    "sensor_id": "SENSOR-001"
  }
}
```

### **Error (400)**
```json
{
  "success": false,
  "error": "Missing required field: latitude"
}
```

---

## 🔗 **Server Addresses**

| Use Case | Address |
|----------|---------|
| **Local Machine** | http://localhost:5000 |
| **Same Network** | http://192.168.1.100:5000 |
| **Remote** | http://your-ip:5000 |
| **Production** | https://your-domain.com |

---

## 🆘 **Common Issues**

| Problem | Solution |
|---------|----------|
| Connection refused | Check server is running, verify IP/port |
| 400 Bad Request | Verify JSON syntax, check required fields |
| Data not appearing | Check network connectivity, verify content-type header |
| Form not updating | Check browser console, verify endpoint is `/api/sensor/data` |

---

## 📞 **Test Your Integration**

```bash
# Send test data
curl -X POST http://localhost:5000/api/sensor/data \
  -H "Content-Type: application/json" \
  -d '{
    "latitude": 40.7128,
    "longitude": -74.0060,
    "water_type": "drinking",
    "temperature": 22.5,
    "sensor_id": "TEST-001"
  }'

# Get latest sensor data
curl http://localhost:5000/api/sensor/latest

# View all readings
curl http://localhost:5000/api/readings
```

---

## 📊 **Full API Reference**

See `IOT_HARDWARE_INTEGRATION.md` for complete documentation including:
- Hardware setup examples
- Network configuration
- Security settings
- Advanced features
- Troubleshooting

---

**Ready to connect your hardware!** 🚀
