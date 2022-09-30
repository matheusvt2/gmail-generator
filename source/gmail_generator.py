"""Generates a gmail account using selenium.
"""

import random

# pyright: reportUnknownMemberType=false
import secrets
import string
import time
from tempfile import mkdtemp

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

FIRSTNAME = "matheus"
LASTNAME = "torres"
EMAIL_ID = f"{FIRSTNAME}.{LASTNAME}.temp"


def generate_passwd() -> str:
    """Function to generate a random 12 character password

    Returns:
        str: generated password
    """
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    alphabet = letters + digits + special_chars
    pwd_length = 12
    pwd = ""
    for _ in range(pwd_length):
        pwd += "".join(secrets.choice(alphabet))
    return pwd


def slow_typing(element: WebElement, text: str) -> None:
    """Slow input to a WebElement
    Args:
        element (object): WebElement returned by find_element
        text (str): text to be inserted into a WebElement
    """
    for character in text:
        element.send_keys(character)
        time.sleep(0.1)
        # time.sleep(random.random())


def create_gmail() -> None:
    """Main execution of gmail generator"""
    # Visit chrome://version/ and copy profile path in place of '<chrome user profile>'
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280x1696")
    options.add_argument("--single-process")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-dev-tools")
    options.add_argument("--no-zygote")
    options.add_argument(f"--user-data-dir={mkdtemp()}")
    options.add_argument(f"--data-path={mkdtemp()}")
    options.add_argument(f"--disk-cache-dir={mkdtemp()}")
    # options.add_argument("--remote-debugging-port=9222")

    browser = Chrome(options=options)
    browser.get("http://gmail.com/")

    time.sleep(1)

    # to accept cookie notification so that it doesn't interfere
    # cookie_cta = browser.find_element("data-action", "accept-cookie-notification")
    # cookie_cta.click()

    # Navigate to Signup Page
    button = browser.find_element(By.CLASS_NAME, "tmMcIf")
    button.click()

    time.sleep(1)

    # Press "Show password" checkbox
    checkbox = browser.find_element(By.CLASS_NAME, "VfPpkd-muHVFf-bMcfAe")
    checkbox.click()

    # Fill user's first name
    firstname = browser.find_element(By.ID, "firstName")
    slow_typing(firstname, FIRSTNAME)

    # Fill user's last name
    lastname = browser.find_element(By.ID, "lastName")
    slow_typing(lastname, LASTNAME)

    # Fill user's email ID
    email = browser.find_element(By.ID, "username")
    slow_typing(email, EMAIL_ID)

    # Fill user's password
    PASSWORD = generate_passwd()
    password = browser.find_element(By.NAME, "Passwd")
    slow_typing(password, PASSWORD)

    password_check = browser.find_element(By.NAME, "ConfirmPasswd")
    slow_typing(password_check, PASSWORD)

    # Validation printscreen #1
    browser.save_screenshot("./images/telaPasswd.png")

    # Click on signup page
    signupbutton = browser.find_element(By.ID, "accountDetailsNext")
    signupbutton.click()

    time.sleep(2)

    # Validation printscreen #2
    browser.save_screenshot("./images/telaTelefone.png")

    time.sleep(1)
    browser.close()

    print(f"Email: {EMAIL_ID}@gmail.com , Temp Password: {PASSWORD}")


if __name__ == "__main__":
    print("Execute main.py instead")
