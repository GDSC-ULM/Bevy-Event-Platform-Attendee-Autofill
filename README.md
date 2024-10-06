# Bevy Event Platform Attendee Autofill

This script automates the process of adding attendees to the Bevy event management platform from an Excel file. It's designed to save time for event organizers who need to transfer attendee information from suitable.co to Bevy (https://gdg.community.dev/).

## Features

- Reads attendee information from an Excel file
- Automates the process of filling in attendee details on the Bevy platform
- Handles multiple attendees sequentially
- Includes built-in delays to account for page loading times

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Installation

1. Clone this repository or download the script file.

2. Install the required Python libraries:

```bash
pip install -r requirements.txt
```

## Usage

1. Prepare your Excel file with the following columns:

| Last Name | First Name | Email |

2. Run the script:

```bash
python main.py
```

3. When prompted, enter the name of your Excel file (including the .xlsx extension).

4. Open the Bevy event page in your web browser and navigate to the attendee management section.

5. Click on the "Add attendees" button to open the add attendee popup.

6. Place your cursor in the "First name" field of the popup and press Enter to confirm that the script can detect the field.

7. The script will now start filling in attendee details. For each record:

   - Place your cursor in the "First name" field
   - Press Enter to trigger the script to fill in the details for that attendee

8. The script will automatically click "Save and add more" for all attendees except the last one, where it will click "Add".

## Important Notes

- The script uses GUI automation, so it's crucial not to move your mouse or use your keyboard while it's running (except when instructed to place the cursor and press Enter).
- The script includes a 0.5-second delay between actions to allow for page loading. You may need to adjust this based on your internet speed and computer performance.
- You can press Ctrl+C in the terminal at any time to stop the script.
- Always test the script with a small sample of data first to ensure it works correctly with your specific Bevy interface and screen resolution.

## Customization

You may need to adjust the following in the script:

- Column names in the Excel file (if different from "Last Name", "First Name", "Email")
- Coordinates for clicking the "Save and add more" and "Add" buttons (adjust the x and y values in the `pyautogui.click()` function calls)
- Delay times (adjust the `time.sleep()` values if needed)

## Troubleshooting

- If the script is not clicking in the right places, you may need to adjust the coordinates in the `pyautogui.click()` function calls.
- If the script is moving too fast for your computer or internet connection, try increasing the `time.sleep()` values.
- Ensure your Excel file is formatted correctly with the expected column names.

## Disclaimer

This script interacts directly with your computer's GUI. Use it at your own risk and always have a backup of your data. The authors are not responsible for any unintended actions or data loss that may occur from using this script.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check issues page if you want to contribute.

## License

[MIT](https://choosealicense.com/licenses/mit/)
