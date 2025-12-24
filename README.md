# Nephrosense

# Chronic Kidney Disease (CKD) Detection Using Breath VOC Analysis

## Project Overview
Chronic Kidney Disease (CKD) often remains undiagnosed in its early stages due to the lack of noticeable symptoms. This project focuses on **early detection of CKD using breath analysis**, which is a **non-invasive and low-cost approach**.

The system detects **volatile organic compounds (VOCs)** present in human breath using gas sensors interfaced with an **ESP32 microcontroller**.

---

## Objectives
- Detect CKD-related VOCs from human breath
- Develop a non-invasive screening system
- Interface gas sensors with ESP32
- Monitor and analyze breath VOC levels
- Enable future machine learning integration

---

## VOC Biomarkers Used

| VOC Component | Role in CKD Detection |
|--------------|----------------------|
| Ammonia (NH₃) 
| Trimethylamine (TMA) 
| Acetone 
|Ethanol

---

## System Architecture
1. User exhales breath near the sensor chamber  
2. Sensors detect VOC concentration changes  
3. ESP32 reads analog sensor values  
4. Data is processed and displayed/logged  
5. Abnormal VOC patterns indicate CKD risk  

---

## Software & Tools
- Arduino IDE
- ESP32 Board Package
- Serial Monitor / OLED Display
-  Python for data analysis
-  Machine Learning models

---

## Working Principle
- Sensors change resistance based on gas concentration
- ESP32 converts sensor output into digital values
- Values are compared with calibrated thresholds
- System indicates **Normal / Abnormal VOC levels**

---

## Features
- Non-invasive breath-based screening
- Low-cost sensor setup
- ESP32 compatible
- Expandable to mobile application
- Suitable for early CKD screening
---

## 🔮 Future Enhancements
- Machine learning-based classification
- Mobile app integration
- Cloud data storage
- More selective sensors
- Clinical validation

---

## 📌 Applications
- Early CKD screening
- Healthcare monitoring
- Academic research
- Portable diagnostic systems

---

## 📜 Disclaimer
This project is intended **only for educational and research purposes**.  


---

## 👩‍💻 Developed By
**Shanmathi S**  
Computer Science Engineering  
Project: CKD Detection Using Breath VOC Analysis
