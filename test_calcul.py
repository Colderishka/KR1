# задание 2
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def test():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    waiter = WebDriverWait(driver, 50)

    driver.find_element(By.CSS_SELECTOR, '#delay').clear()
    driver.find_element(By.CSS_SELECTOR, '#delay').send_keys("45")
    driver.find_element(By.XPATH, '//*[@id="calculator"]//span[contains(text(), 7)]').click()
    driver.find_element(By.XPATH, '//*[@id="calculator"]//span[contains(text(), "+")]').click()
    driver.find_element(By.XPATH, '//*[@id="calculator"]//span[contains(text(), 8)]').click()
    sleep(3)
    driver.find_element(By.CSS_SELECTOR, "[class='btn btn-outline-warning']").click()
    waiter.until(EC.text_to_be_present_in_element( (By.CSS_SELECTOR, "[class='screen']"), '15'))
    result = driver.find_element(By.CSS_SELECTOR, "[class='screen']").text
    assert result == "15"

    driver.close()
    driver.quit()


