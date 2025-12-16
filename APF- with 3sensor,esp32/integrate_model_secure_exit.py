import serial
import json
import joblib
import time
import warnings

warnings.filterwarnings("ignore")

MODEL_FILE = "kidney_voc_model.pkl"
COM_PORT = "COM11"     # Change to your correct COM port
BAUD = 115200

# ---------------- LOAD MODEL -----------------
try:
    model = joblib.load(MODEL_FILE)
    print("[OK] Model loaded:", MODEL_FILE)
except Exception as e:
    print("[ERROR] Cannot load model:", e)
    exit()

ser = None

def connect_serial():
    """Keeps trying to connect until successful."""
    global ser
    while True:
        try:
            ser = serial.Serial(COM_PORT, BAUD, timeout=1)
            time.sleep(2)
            print("[OK] Connected to ESP32 on", COM_PORT)
            return
        except Exception:
            print("[WAIT] ESP32 not found. Retrying...")
            time.sleep(2)

# Initial connection
connect_serial()

# ---------------- MAIN LOOP -------------------
while True:
    try:
        raw = ser.readline().decode(errors="ignore").strip()

        if not raw:
            continue

        # Only accept JSON lines
        if not raw.startswith("{"):
            continue

        try:
            data = json.loads(raw)
        except:
            print("[WARN] JSON parse failed:", raw)
            continue

        nh3     = float(data.get("NH3", 0.0))
        acetone = float(data.get("Acetone", 0.0))
        tma     = float(data.get("TMA", 0.0))

        features = [[nh3, acetone, tma]]
        pred = model.predict(features)[0]

        status = "Normal" if int(pred) == 0 else "Abnormal"

        # Send prediction to ESP32
        ser.write((status + "\n").encode())

        # Display values
        print(f"NH3(ppm):     {nh3:.4f}")
        print(f"Acetone(ppm): {acetone:.4f}")
        print(f"TMA(ppm):     {tma:.4f}")
        print("Prediction:   ", status)
        print("-" * 30)

        time.sleep(0.1)

    except serial.SerialException:
        print("[ERROR] Serial connection lost! Reconnecting...")
        try:
            ser.close()
        except:
            pass
        connect_serial()

    except KeyboardInterrupt:
        print("\n[STOP] User stopped the script.")
        break

# Cleanup
if ser:
    ser.close()
print("Serial closed.")
