from datetime import datetime, timezone

def transform_1(message):
    """
    Converts Format 1 (ISO timestamp) to unified format.
    Steps:
      1. Convert ISO timestamp to milliseconds.
      2. Map keys to unified format.
    """
    # Convert ISO timestamp to milliseconds
    iso_time = message['t']
    dt = datetime.fromisoformat(iso_time.replace('Z', '+00:00'))
    timestamp_ms = int(dt.timestamp() * 1000)

    # Return unified format
    return {
        "device": message["id"],
        "ts": timestamp_ms,
        "co": message["c"],
        "humidity": message["h"],
        "temp": message["tp"],
        "light": message["l"],
        "lpg": message["g"],
        "motion": message["m"],
        "smoke": message["s"]
    }

def transform_2(message):
    """
    Converts Format 2 (milliseconds timestamp) to unified format.
    Simple key renaming.
    """
    return {
        "device": message["device_id"],
        "ts": message["timestamp"],
        "co": message["carbon_monoxide"],
        "humidity": message["humidity"],
        "temp": message["temperature"],
        "light": message["light_detected"],
        "lpg": message["lpg"],
        "motion": message["motion_detected"],
        "smoke": message["smoke_level"]
    }
if __name__ == "__main__":
    # Example test input for transform_2
    sample_input = {
        "device_id": "device2",
        "timestamp": 1735689600000,
        "carbon_monoxide": 0.6,
        "humidity": 45.0,
        "temperature": 22.0,
        "light_detected": True,
        "lpg": 0.05,
        "motion_detected": False,
        "smoke_level": 0.02
    }
    result = transform_2(sample_input)
    print(result)
