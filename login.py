class Login():
    """
    Login:
    It takes detials dictionary and initialize all required
    element names, credentials etc
    """
    def __init__(self,details):
        self.login_url = details.get("login_url", None)
        self.sign_in_button_id = details.get("sign_in_button_id", None)
        self.login_in_button_class = details.get("login_button_class", None)
        self.email_form_id = details.get("email_form_id", None)
        self.password_form_id = details.get("password_form_id", None)
        self.email = details.get("email", None)
        self.password = details.get("password", None)
        
    def get_logged_in_session(self, driver):
        return driver
