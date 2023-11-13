import unittest
from selenium.webdriver.common.by import By

from SeleniumDriver import chrome_driver, user_login

class TestUserAccounts(unittest.TestCase):
    url = "http://127.0.0.1:8000/"

    # Sprint 3: Test Case #1
    def test_signup_page(self):
        with chrome_driver() as driver: 
            driver.get(self.url)
            driver.find_element(By.ID, "signup").click()
            self.assertEqual(driver.current_url, self.url + "signup")

    # Sprint 3: Test Case #2
    def test_login_page(self):
        with chrome_driver() as driver: 
            driver.get(self.url)
            driver.find_element(By.ID, "login").click()
            self.assertEqual(driver.current_url, self.url + "login")
    
    # Sprint 3: Test Case #4
    def test_too_many_characters_title(self):
        with chrome_driver() as driver:
            user_login(driver=driver) # helper login function
            driver.get(self.url + "createEvent")
            self.assertEqual(driver.current_url, self.url + "createEvent")
            inputstr = " ".join(["test" for i in range(1000)])
            nameInput = driver.find_element(By.ID, "title")
            nameInput.send_keys(inputstr)
            nameText = nameInput.get_attribute("value")
            self.assertEqual(len(nameText), 250)

    # Sprint 3: Test Case #5
    def test_too_many_characters_description(self):
        with chrome_driver() as driver:
            user_login(driver=driver) # helper login function
            driver.get(self.url + "createEvent")
            self.assertEqual(driver.current_url, self.url + "createEvent")
            inputstr = " ".join(["test" for i in range(1000)])
            nameInput = driver.find_element(By.ID, "description")
            nameInput.send_keys(inputstr)
            nameText = nameInput.get_attribute("value")
            self.assertEqual(len(nameText), 1000)
        
    # Sprint 3: Test Case #10
    def test_login(self):
        with chrome_driver() as driver:
            user_login(driver)
            self.assertEqual(driver.current_url, self.url + "events")

    # Sprint 3: Test Case #11
    def test_not_logged_in(self):
        with chrome_driver() as driver: 
            driver.get(self.url)
            driver.find_element(By.ID, "events").click()
            self.assertEqual(driver.current_url, self.url + "login?next=/events/")


if __name__ == '__main__':
    unittest.main()