import pyautogui
import time

# Global constants
TIMEOUT = 0.5  # Maximum minutes to search
TRY = 2        # Time in seconds to retry

def click_icon_when_found(image_path, timeout=TIMEOUT * 60, confidence=0.9, region=None):
    """
    Parameters:
    - image_path: Path to icon image file
    - timeout: Maximum seconds to search (default 30)
    - confidence: Match accuracy (0-1, default 0.9)
    - region: Tuple (x, y, width, height) to limit search area
    """
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        try:
            # Search for the icon
            position = pyautogui.locateCenterOnScreen(
                image_path,
                confidence=confidence,
                region=region
            )
            
            if position:
                pyautogui.click(position)
                print(f"Clicked icon at {position}")
                return True  # Return after successful click
                
        except pyautogui.ImageNotFoundException:
            pass  # Icon not found in this iteration
        
        # Wait before retrying
        time.sleep(TRY)  # Reduce CPU usage
    
    print("Icon not found within timeout period")
    return False

# Usage example: Keep trying forever with 10-second timeouts
while True:
    click_icon_when_found('icon.png')
    time.sleep(TRY)  # Optional: Wait after clicking before next check

