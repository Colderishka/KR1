# задание 1
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest
@pytest.mark.skip
def test():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    path_Fname = '[name="first-name"]'
    driver.find_element(By.CSS_SELECTOR, path_Fname).send_keys("Иван")
    filled1_css = driver.find_element(By.CSS_SELECTOR, path_Fname).value_of_css_property("color")

    path_Lname = '[name="last-name"]'
    driver.find_element(By.CSS_SELECTOR, path_Lname).send_keys("Петров")
    filled2_css = driver.find_element(By.CSS_SELECTOR, path_Lname).value_of_css_property("color")

    path_address = '[name="address"]'
    driver.find_element(By.CSS_SELECTOR, path_address).send_keys("Ленина, 55-3")
    filled3_css = driver.find_element(By.CSS_SELECTOR, path_address).value_of_css_property("color")

    path_mail = '[name="e-mail"]'
    driver.find_element(By.CSS_SELECTOR, path_mail).send_keys("test@skypro.com")
    filled4_css = driver.find_element(By.CSS_SELECTOR, path_mail).value_of_css_property("color")

    path_phone = '[name="phone"]'
    driver.find_element(By.CSS_SELECTOR, path_phone).send_keys("+7985899998787")
    filled5_css = driver.find_element(By.CSS_SELECTOR, path_phone).value_of_css_property("color")

    path_city = '[name="city"]'
    driver.find_element(By.CSS_SELECTOR, path_city).send_keys("Москва")
    filled6_css = driver.find_element(By.CSS_SELECTOR, path_city).value_of_css_property("color")

    path_country = '[name="country"]'
    driver.find_element(By.CSS_SELECTOR, path_country).send_keys("Россия")
    filled7_css = driver.find_element(By.CSS_SELECTOR, path_country).value_of_css_property("color")

    path_job_possion = '[name="job-position"]'
    driver.find_element(By.CSS_SELECTOR, path_job_possion).send_keys("QA")
    filled8_css = driver.find_element(By.CSS_SELECTOR, path_job_possion).value_of_css_property("color")

    path_company = '[name="company"]'
    driver.find_element(By.CSS_SELECTOR, path_company).send_keys("SkyPro")
    filled9_css = driver.find_element(By.CSS_SELECTOR, path_company).value_of_css_property("color")

    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    unfilled_css = driver.find_element(By.CSS_SELECTOR, '[class="alert py-2 alert-danger"]').value_of_css_property("color")
    green_css = 'rgba(33, 37, 41, 1)'

    assert unfilled_css == 'rgba(132, 32, 41, 1)'
    assert green_css == filled1_css
    assert green_css == filled2_css
    assert green_css == filled3_css
    assert green_css == filled4_css
    assert green_css == filled5_css
    assert green_css == filled6_css
    assert green_css == filled7_css
    assert green_css == filled8_css
    assert green_css == filled9_css

    driver.close()
    driver.quit()

