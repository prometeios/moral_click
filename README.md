# Click Icon Script

This script automates the process of searching for an icon on the screen and clicking it when found. It uses the `pyautogui` library to locate and click the icon.

## Requirements

- Python 3.x
- `uv` library

You can activate the existing virtual environment to use the required library.

### Activating the Virtual Environment

1. Activate the virtual environment:

   - On Windows:
     ```sh
     .\moral\Scripts\activate
     ```
   - On macOS and Linux:
     ```sh
     source moral/bin/activate
     ```

## Usage

The script defines a function `click_icon_when_found` that searches for an icon on the screen and clicks it when found. The function takes the following parameters:

- `image_path`: Path to the icon image file.
- `timeout`: Maximum time in seconds to search for the icon (default is 30 seconds).
- `confidence`: Match accuracy (0-1, default is 0.9).
- `region`: Tuple `(x, y, width, height)` to limit the search area (optional).

### Example

The script includes an example usage that continuously searches for an icon named `icon.png` and clicks it when found. The search is retried every 2 seconds.

```python
# Usage example: Keep trying forever with 10-second timeouts
while True:
    click_icon_when_found('icon.png')
    time.sleep(2)  # Optional: Wait after clicking before next check
```

### Modifying Timeout

The `TIMEOUT` constant is defined in minutes. To change the timeout duration, modify the `TIMEOUT` value in the script.

```python
# Global constants
TIMEOUT = 0.5  # Maximum minutes to search
```

### Running the Script

To run the script, execute the following command in your terminal:

```sh
python click.py
```

This will start the script and it will continuously search for the specified icon and click it when found.

## License

This project is licensed under the MIT License.
