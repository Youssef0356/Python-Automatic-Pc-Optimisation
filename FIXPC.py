import time
import pyautogui

def open_temp_folder():
    # Simulate pressing the Windows key (Win) and the 'r' key together to open Run
    pyautogui.hotkey('win', 'r')

    # Type '%temp%' into the Run dialog
    pyautogui.typewrite('%temp%', interval=0.1)

    # Press the 'Enter' key to execute the command
    pyautogui.press('enter')

def select_and_delete_temp_files():
    # Give some time for the Temp folder to open (optional, adjust as needed)
    time.sleep(2)

    # Simulate pressing Ctrl+A to select all files in the Temp folder
    pyautogui.hotkey('ctrl', 'a')

    # Simulate pressing the 'Delete' key to delete all selected files
    pyautogui.press('delete')

def check_disk_health():
    # Open the Command Prompt
    pyautogui.hotkey('win', 'r')
    pyautogui.typewrite('cmd', interval=0.1)
    pyautogui.press('enter')

    time.sleep(2)

    pyautogui.typewrite('wmic diskdrive get caption,status', interval=0.1)
    pyautogui.press('enter')

def run_cleanmgr():
    pyautogui.hotkey('win', 'r')
    pyautogui.typewrite('cmd', interval=0.1)
    pyautogui.press('enter')

    time.sleep(2)

    pyautogui.typewrite('cleanmgr', interval=0.1)
    pyautogui.press('enter')

def type_msconfig():
    time.sleep(1)

    pyautogui.typewrite('msconfig', interval=0.1)

    pyautogui.press('enter')

    time.sleep(4)

def open_run_dialog():
    time.sleep(2)

    pyautogui.hotkey('win', 'r')

def open_cmd_and_type(command):
    pyautogui.hotkey('win', 'r')
    pyautogui.typewrite('cmd', interval=0.1)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.typewrite(command, interval=0.1)
    pyautogui.press('enter')

if __name__ == "__main__":
    open_temp_folder()
    select_and_delete_temp_files()

    # Close Windows Explorer by simulating Alt+F4 key combination
    pyautogui.hotkey('alt', 'f4')
    time.sleep(2)

    check_disk_health()

    time.sleep(6)


    pyautogui.typewrite('exit')
    pyautogui.press('enter')
    time.sleep(2)

    run_cleanmgr()

    time.sleep(5)

    open_cmd_and_type('systempropertiesperformance')

    time.sleep(5)

    open_run_dialog()
    time.sleep(1)  # Add a small delay for the Run dialog to be ready

    # Type 'msconfig' into the Run dialog
    type_msconfig()
