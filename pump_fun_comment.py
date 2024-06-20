from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Chrome(executable_path='C:\Users\Lenovo\Downloads\chromedriver.exe')

# Open Pump.fun and log in (assuming you have a login process)
driver.get("https://www.pump.fun")

try:
    # Navigate to the comment section
    comment_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "comment-section"))
    )
    comment_button.click()

    # Post a comment
    comment_field = driver.find_element(By.ID, "comment-field")
    comment_field.send_keys("Check out our amazing trading bot at Pump.fun!")
    post_button = driver.find_element(By.ID, "post-comment-button")
    post_button.click()

finally:
    driver.quit()
