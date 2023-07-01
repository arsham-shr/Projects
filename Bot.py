from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the webdriver
driver = webdriver.Chrome()

# Open a website
driver.get('https://www.example.com')

# Find an element by its ID and perform an action
element = driver.find_element_by_id('my_element_id')
element.click()

# Find an element by its class name and perform an action
element = driver.find_element_by_class_name('my_element_class')
element.send_keys('Hello, World!')

# Wait for an element to be visible, then perform an action
element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '.my_css_selector')))
element.clear()
element.send_keys('This is a bot!')

# Submit a form
form_element = driver.find_element_by_tag_name('form')
form_element.submit()

# Close the browser
driver.quit()
