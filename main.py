import pyautogui
import pytesseract
import random
import time



kwbox =(1118, 508)
kwbox2 =(1308, 603)


def click_if_tree_in_box(treebox_left_top, treebox_right_bottom):
    # Capture the screen within the specified box
    screenshot = pyautogui.screenshot(region=(treebox_left_top[0], treebox_left_top[1], treebox_right_bottom[0] - treebox_left_top[0], treebox_right_bottom[1] - treebox_left_top[1]))

    # Use pytesseract to extract text from the image
    extracted_text = pytesseract.image_to_string(screenshot).lower()
    print(extracted_text)
    # Check if "tree" appears in the extracted text
    return "copper" in extracted_text

while True:
    if click_if_tree_in_box(kwbox, kwbox2):
        pyautogui.click()
        print("Clicked in the box!")
        time.sleep(5)
        pyautogui.moveTo(1430, 656)
        print("moving to r2")
    else:
        pyautogui.moveTo(1430, 656)
        print("moving to r2")
        if click_if_tree_in_box(kwbox, kwbox2):
            print("moving to r1")
            pyautogui.click()
            print("Clicked in the box!")
            time.sleep(5)
        else:
            pyautogui.moveTo(1286, 683)
