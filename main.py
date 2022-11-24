import pyautogui
import win32api
import time


def move_mouse_until_click():
    left_click_state = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
    right_click_state = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128
    clicked = False
    while clicked is False:
        a = win32api.GetKeyState(0x01)
        b = win32api.GetKeyState(0x02)
        pyautogui.moveTo(150, 150)
        if a != left_click_state:  # Button state changed
            left_click_state = a
            if a < 0:
                clicked = True
                print('Mouse released.')
            else:
                clicked = True
                print('Mouse released.')

        pyautogui.moveTo(300, 300)
        if b != right_click_state:  # Button state changed
            right_click_state = b
            if b < 0:
                clicked = True
                print('Mouse released.')
            else:
                clicked = True
                print('Mouse released.')
        pyautogui.moveTo(450, 450)
        time.sleep(0.001)


if __name__ == '__main__':
    move_mouse_until_click()
