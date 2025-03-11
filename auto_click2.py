import pyautogui
import time
import subprocess

# Global constants
TIMEOUT = 0.5  # Maximum minutes to search
TRY = 2        # Time in seconds to retry

def get_browser_window_name():
    """
    Get the name of the first visible web browser window.
    """
    browser_names = ["Firefox", "Chrome", "Chromium", "Edge"]
    for name in browser_names:
        try:
            result = subprocess.run(['xdotool', 'search', '--onlyvisible', '--name', name], capture_output=True, text=True, check=True)
            window_ids = result.stdout.strip().split('\n')
            if window_ids:
                return name
        except subprocess.CalledProcessError:
            continue
    return None

def bring_window_to_foreground(window_name):
    """
    Bring the specified window to the foreground.
    """
    try:
        subprocess.run(['xdotool', 'search', '--name', window_name, 'windowactivate'], check=True)
    except subprocess.CalledProcessError:
        print(f"Failed to bring window '{window_name}' to the foreground")

def minimize_window(window_name):
    """
    Minimize the specified window.
    """
    try:
        subprocess.run(['xdotool', 'search', '--name', window_name, 'windowminimize'], check=True)
    except subprocess.CalledProcessError:
        print(f"Failed to minimize window '{window_name}'")

def click_icon_when_found(image_path, timeout=TIMEOUT * 60, confidence=0.9, region=None, window_name=None):
    """
    Parameters:
    - image_path: Path to icon image file
    - timeout: Maximum seconds to search (default 30)
    - confidence: Match accuracy (0-1, default 0.9)
    - region: Tuple (x, y, width, height) to limit search area
    - window_name: Name of the window to bring to the foreground
    """
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        if window_name:
            bring_window_to_foreground(window_name)
        
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
                
                if window_name:
                    minimize_window(window_name)
                
                return True  # Return after successful click
                
        except pyautogui.ImageNotFoundException:
            pass  # Icon not found in this iteration
        
        # Wait before retrying
        time.sleep(TRY)  # Reduce CPU usage
    
    print("Icon not found within timeout period")
    return False

# Usage example: Keep trying forever with 10-second timeouts
while True:
    window_name = get_browser_window_name()
    if window_name:
        click_icon_when_found('icon.png', window_name=window_name)
    else:
        print("No browser window found")
    time.sleep(TRY)  # Optional: Wait after clicking before next check