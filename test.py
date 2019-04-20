from bmsbuy import login_url, target_url, \
        sign_in_button_id, login_button_id,\
        personalized_profile_cancel_id, update_popup_cancel_class, \
        email_form_id, password_form_id, \
        email, password, play_notification
from bmsbuy import initialize_driver, login
from login import Login

def test_get_login_elements():
    if not login_url:
        assert False
    if not sign_in_button_id:
        assert False
    if not login_button_id:
        assert False
    if not personalized_profile_cancel_id:
        assert False
    if not update_popup_cancel_class:
        assert False 
    if not email_form_id:
        assert False
    if not password_form_id:
        assert False
    if not email:
        assert False
    if not password:
        assert False
    if not target_url:
        assert False
    assert True

def _test_login():
    driver = initialize_driver()
    if not driver:
        assert False
    try:
        driver = login(driver)
    except TypeError as e:
        print("Element not found: ", str(e))
        driver.close()
        assert False
    assert True

def test_sound():
    play_notification()

if __name__ == "__main__":
    test_get_login_elements()
    _test_login()
