from login import Login
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

with open("config.json") as config_file:
    config = json.loads(config_file.read())

# URLS
urls = config.get("urls", {})
login_url = urls.get("login",None)

# BUTTONS
buttons = config.get("buttons", {})
sign_in_button_id = buttons.get("signin_id",None)
login_button_class = buttons.get("login_class",None)

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
    "login_in_button_class":login_button_class,
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

def main():
    driver = initialize_driver()
    driver = login(driver)

if __name__ == "__main__":
    main()