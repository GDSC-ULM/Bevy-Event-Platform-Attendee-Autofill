import pyautogui
import time
import pandas as pd
import keyboard

def load_attendees(filename):
    df = pd.read_excel(filename)
    return df.to_dict('records')

def fill_attendee_details(attendee):
    print(attendee['First Name'], attendee['Last Name'], attendee['Email'])
    # Fill First Name
    pyautogui.typewrite(attendee['First Name'])
    pyautogui.press('tab')

    # Fill Last Name
    pyautogui.typewrite(attendee['Last Name'])
    pyautogui.press('tab')

    # Fill Email
    pyautogui.typewrite(attendee['Email'])
    pyautogui.press('tab')

    # Check the Check-in box
    pyautogui.press('space')

    # save and add more
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('space')

    time.sleep(0.5)

def main():
    filename = input("Enter the Excel file name containing attendees: ")
    attendees = load_attendees(filename)

    print("Place your cursor in the 'First name' field and press 'Enter' to start...")
    keyboard.wait('enter')

    for i, attendee in enumerate(attendees):
        fill_attendee_details(attendee)
        print(f"Attendee {i+1} added successfully!")

        print("Place your cursor in the 'First name' field and press 'Enter' to start...")
        keyboard.wait('enter')

    print("All attendees added successfully!")

if __name__ == "__main__":
    main()