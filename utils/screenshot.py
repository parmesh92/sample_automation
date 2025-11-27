import os
import datetime

def take_screenshot(driver, name="failure"):
    folder = "reports/screenshots"
    os.makedirs(folder, exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = f"{folder}/{name}_{timestamp}.png"

    try:
        driver.save_screenshot(filepath)
        print(f"[SCREENSHOT SAVED] {filepath}")
    except Exception as e:
        print(f"[SCREENSHOT FAILED] {e}")

    return filepath
