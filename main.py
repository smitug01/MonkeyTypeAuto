# Import Library.
import time
import random
import string
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Print Information.
print('''
-------------Warning-------------
To using this script more easily, there is something you need to know.
This script is designed only for testing or learning purpose
Do NOT use it for public testing
''')

# User enter length of time to test.
try:
    rderrinput = int(input("Enter how many time you want to test? (30 in default): "))
    if not isinstance(rderrinput, int): print("Input invalid, use default value 30"); usr_time = 30
    else: usr_time = rderrinput()
except:
    print("Input invalid, use default value 30"); usr_time = 30

try:
    rderrinput = int(input("Enter how many the base time in RPM? (1~1000, 30 in default): "))
    if not isinstance(rderrinput, int): print("Input invalid, use default value 30"); basic_time = 30
    else: basic_time = rderrinput()
except:
    print("Input invalid, use default value 30"); basic_time = 30

rderrinput = input("Random Error? (True) or False: ")
if not isinstance(rderrinput, bool): print("Input invalid, use default value True"); random_error = True
else: random_error = rderrinput()

rdspdinput = input("Random Speed? (True) or False: ")
if not isinstance(rderrinput, bool): print("Input invalid, use default value True"); random_speed = True
else: random_speed = rdspdinput()

def pause_time():
    if (random_speed):
        pyautogui.PAUSE = ((int(random.choice(string.digits))) / basic_time)
    else:
        pyautogui.PAUSE = 1 / basic_time

# Create a auto-control for webdriver using.
browser_web = webdriver.Chrome(ChromeDriverManager().install())
browser_web.get('https://monkeytype.com/')
time.sleep(3)

# Keyboard simulation variable change.
select_time_buttom = "/html/body/div[35]/div[@id='centerContent']/div[@id='top']/div[@class='config']/div[@class='desktopConfig']/div[@class='group time']/div[@class='buttons']/div[@class='text-button'][4]/i[@class='fas fa-tools']"
change_time_value = "/html/body/div[@id='customTestDurationPopupWrapper']/div[@id='customTestDurationPopup']/input"
change_time_check = "/html/body/div[@id='customTestDurationPopupWrapper']/div[@id='customTestDurationPopup']/div[@class='button']"
pyautogui.FAILSAFE = False
running_status = True

def change_test_time(usr_time):
    browser_web.find_element(by=By.XPATH, value=select_time_buttom).click()
    browser_web.find_element(by=By.XPATH, value=change_time_value).clear()
    browser_web.find_element(by=By.XPATH, value=change_time_value).send_keys(usr_time)
    browser_web.find_element(by=By.XPATH, value=change_time_check).click()

def random_replace(length):
    seed = "abcdefghijklmnopqrstuvwxyz"
    sa = []
    for i in range(length):
        sa.append(random.choice(seed))
    salt = ''.join(sa)
    return salt

def random_char():
    seed = "abcdefghijklmnopqrstuvwxyz"
    sa = []
    for i in range(1):
        sa.append(random.choice(seed))
    salt = ''.join(sa)
    return salt

# use try, expect to check element status to control program stop
def check_test_status():
    select_filter = "/html/body/div[35]/div[@id='centerContent']/div[@id='middle']/div[@class='page pageTest active']/div[@id='typingTest']/div[@id='wordsWrapper']/div[@id='words']/div[@class='word active']"
    filter_class = browser_web.find_elements(by=By.XPATH, value=select_filter)
    if "[]" in filter_class:
        return False
    else:
        return True

def filter_word():
    select_filter = "/html/body/div[35]/div[@id='centerContent']/div[@id='middle']/div[@class='page pageTest active']/div[@id='typingTest']/div[@id='wordsWrapper']/div[@id='words']/div[@class='word active']"
    filter_class = browser_web.find_elements(by=By.XPATH, value=select_filter)
    type_text(filter_class)

def type_text(words):
    for word in words:
        if "'" in word.get_attribute('textContent') or '"' in word.get_attribute('textContent'):
            if (bool(random.getrandbits(1))) and (bool(random.getrandbits(1))):
                pyautogui.typewrite(random_replace(len(word.get_attribute('textContent'))))
            else:
                pyautogui.typewrite(word.get_attribute('textContent'))
            pyautogui.typewrite(' ')
            pause_time()

        else:
            for char in word.get_attribute('textContent'):
                if (bool(random.getrandbits(1))) and (bool(random.getrandbits(1))):
                    if (bool(random.getrandbits(1))) and (bool(random.getrandbits(1))):
                        if (bool(random.getrandbits(1))) and (bool(random.getrandbits(1))):
                            if (random_error == True):
                             pyautogui.typewrite(random_char())
                            else:
                             pyautogui.typewrite(char)
                        else:
                            pyautogui.typewrite(char)
                    else:
                        pyautogui.typewrite(char)
                else:
                    pyautogui.typewrite(char)
            pyautogui.typewrite(' ')
            pause_time()

# Main Program
change_test_time(usr_time)
time.sleep(2)

while(True):
    # check Test Status
    if (check_test_status() == False):
        break
    else:
        continue
    # filter_word()
    filter_word()

print("Thanks For Using.")
