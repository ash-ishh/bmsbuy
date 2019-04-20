from bmsbuy import login_url, sign_in_button_id, login_button_class, \
        email_form_id, password_form_id, \
        email, password
from login import Login, initialize_driver, login

def test_get_login_elements():
    if not login_url:
        assert False
    if not sign_in_button_id:
        assert False
    if not login_button_class:
        assert False
    if not email_form_id:
        assert False
    if not password_form_id:
        assert False
    if not email:
        assert False
    if not password:
        assert False
    assert True

def test_login():
    driver = initialize_driver()
    if not driver:
        assert False
    assert True

if __name__ == "__main__":
    test_get_login_elements()
    test_login()
