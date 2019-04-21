from selenium.common.exceptions import NoSuchElementException

def get_element(driver, selector, value):
    """
    Returns the elements of driver with given value and selector.
    Args:
        driver: selenium webdriver object
        selector: valid selenium selector string
        value: value on which elements needs to be selected
    Returns:
        Selenium webelement
    Raises:
        TypeError: if webdriver is not correct.
        ValueError: if selector is not in dict.
    """
    driver_type = str(type(driver))
    if 'selenium.webdriver' not in driver_type:
        raise TypeError("Invalid selenium driver passed\nType of object you passed: " + driver_type)

    selectors = {
            'css': driver.find_elements_by_css_selector,
            'name': driver.find_elements_by_name,
            'id': driver.find_elements_by_id,
            'tag_name': driver.find_elements_by_tag_name,
            'xpath': driver.find_elements_by_xpath,
            'link_text': driver.find_elements_by_link_text,
            'partial_link_text': driver.find_elements_by_partial_link_text,
            'class_name': driver.find_elements_by_class_name,
    }

    selector_names = list(selectors.keys())
    if selector not in selector_names:
        raise ValueError(f"Invalid selctor.\nProvide from {str(selector_names)}")

    value = str(value)
    try:
        element = selectors[selector](value)
    except NoSuchElementException:
        raise RuntimeError(f"{value} not found")

    if len(element) == 0:
        raise RuntimeError(f"{value} not found")

    return element[0]