import time
from helpers import get_elements

class Login():
    """
    Login:
    It takes detials dictionary and initialize all required
    element names, credentials
    """
    def __init__(self,details):
        self.login_url = details.get("login_url", None)
        self.sign_in_button_id = details.get("sign_in_button_id", None)
        self.login_button_id = details.get("login_button_id", None)
        self.personalized_profile_cancel_id = details.get("personalized_profile_cancel_id", None)
        self.email_form_id = details.get("email_form_id", None)
        self.password_form_id = details.get("password_form_id", None)
        self.email = details.get("email", None)
        self.password = details.get("password", None)
        
    def get_logged_in_session(self, driver):
        """
        This method takes driver and uses url, elements, credentials provided while
        initantiating Login object and fills information and returns updated driver
        instances.

        Args: driver - selenium webdriver instance

        Exceptions: 

        TypeError: if element is not avaliable

        """
        # Go to loggin url
        driver.get(self.login_url)
        time.sleep(0.2)

        # Click sigin button
        sigin_button = get_elements(driver,selector="id",value=self.sign_in_button_id)

        # Check if ther is get personalized info pop up click cancle if it is there 
        personalized_profile_cancel_button = get_elements(driver,selector="id",value=self.personalized_profile_cancel_id)
        personalized_profile_cancel_button.click()

        sigin_button.click()

        # Enter email address
        email_form = get_elements(driver,selector="id",value=self.email_form_id)
        email_form.send_keys(self.email)

        # Enter password
        password_form = get_elements(driver,selector="id",value=self.password_form_id)
        password_form.send_keys(self.password)

        # Click Login button
        loggin_button = get_elements(driver,selector="id",value=self.login_button_id)
        loggin_button.click()

        time.sleep(1)
 
        return driver
