from login import Login
from helpers import get_elements
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pydub import AudioSegment
from pydub.playback import play
import json
import time

with open("config.json") as config_file:
    config = json.loads(config_file.read())

# URLS
urls = config.get("urls", {})
login_url = urls.get("login",None)
target_url = urls.get("target_url", None)

# BUTTONS
buttons = config.get("buttons", {})
sign_in_button_id = buttons.get("signin_id",None)
login_button_id = buttons.get("login_id",None)
personalized_profile_cancel_id = buttons.get("personalized_profile_cancel_id",None)
update_popup_cancel_class = buttons.get("update_popup_cancel_class",None)
book_tickets_link_text = buttons.get("book_tickets_link_text", None)

# FORMS
forms = config.get("forms", {})
email_form_id = forms.get("email_id", None)
password_form_id = forms.get("password_id", None)

# CREDENTIALS
credentials = config.get("credentials", {})
email = credentials.get("email", None)
password = credentials.get("password", None)

details = {
    "login_url":login_url,
    "sign_in_button_id":sign_in_button_id,
    "login_button_id":login_button_id,
    "personalized_profile_cancel_id":personalized_profile_cancel_id,
    "update_popup_cancel_class":update_popup_cancel_class,
    "book_tickets_link_text": book_tickets_link_text,
    "email_form_id":email_form_id,
    "password_form_id":password_form_id,
    "email":email,
    "password":password,
}

def initialize_driver():
    driver = webdriver.Chrome("chromedriver")
    driver.maximize_window()
    return driver

def login(driver):
    login = Login(details)
    driver = login.get_logged_in_session(driver)
    return driver

def go_to_target_url(driver):
    driver.get(target_url) 
    return driver

def close_popup(driver):
    driver.switch_to_frame(driver.find_element_by_css_selector("body>iframe"))
    update_popup_close_button = get_elements(driver, selector="class_name", value=update_popup_cancel_class)
    update_popup_close_button.click()
    driver.switch_to_default_content()
    time.sleep(0.5)
    return driver

def get_book_tickets_button(driver):
    try:
        button = get_elements(driver, selector="link_text", value=book_tickets_link_text)
        return button
    except RuntimeError:
        # Button not found
        return None

def play_notification():
    song = AudioSegment.from_wav("sound/notification.wav")
    play(song)

def main():
    driver = initialize_driver()
    driver = login(driver)
    driver = go_to_target_url(driver)
    try:
        driver = close_popup(driver)
    except RuntimeError:
        # pop up not found
        pass

    with open("/tmp/bms.html","w") as w:
        w.write(driver.page_source)

    time.sleep(0.5)

    book_tickets_button= get_book_tickets_button(driver)
    while not book_tickets_button:
        print("Book now button not available")
        time.sleep(0.1)
        driver = go_to_target_url(driver)
        book_tickets_button = get_book_tickets_button(driver)

    book_tickets_button.click()
    # play song on successfull click
    play_notification()

    input()

if __name__ == "__main__":
    main()