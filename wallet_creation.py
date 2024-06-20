from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Chrome(executable_path='C:\Users\Lenovo\Downloads\chromedriver.exe')

# Open Pump.fun
driver.get("https://www.pump.fun")

try:
    # Wait until the element is present
    wallet_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "create-wallet-button"))
    )
    wallet_button.click()

    # Fill in the wallet creation form
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("YourUsername")
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("YourPassword")
    password_field.send_keys(Keys.RETURN)

    # Wait and get the wallet address
    wallet_address = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "wallet-address"))
    )
    print("Wallet Created: ", wallet_address.text)

finally:
    driver.quit()
