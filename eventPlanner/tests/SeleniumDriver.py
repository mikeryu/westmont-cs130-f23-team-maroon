from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions

def user_login(driver):
    # opens Login Page and logs in as the test user
    driver.get("http://127.0.0.1:8000/login") 
    driver.find_element(By.ID, "username").send_keys("test")
    driver.find_element(By.ID, "password").send_keys("test")
    driver.find_element(By.ID, "submit").click()

# This defines a context manager for the Selenium WebDriver
class ChromeDriver:
    def __init__(self):
        options = ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument("--headless=new")
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(4)
        self.driver = driver

    def __enter__(self):
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()

chrome_driver = ChromeDriver