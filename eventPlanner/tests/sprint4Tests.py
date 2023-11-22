from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import unittest


class  Sprint4Tests(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        print("testing started")
        
        self.driver = webdriver.Chrome(options=options)

        self.driver.get("http://127.0.0.1:8000")

        self.driver.implicitly_wait(2)

        self.driver.find_element(By.ID, "login").click()
        self.driver.find_element(By.ID, "username").send_keys("test")
        self.driver.find_element(By.ID, "password").send_keys("test")
        self.driver.find_element(By.ID, "submit").click()

    


    
    """
    test for issue #99 - all fields must required to create an event
    """
    def testcreateEventRequiredFeilds(self):
        self.driver.find_element(By.ID, "planEvent").click()
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:8000/createEvent")

        self.driver.find_element(By.ID, "submit").click()
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:8000/createEvent")

        fields = {"test": "test event", "host": "test host", "location": "test location", "date": "2021-05-05", "time": "12:00", "description": "test description"}

        #popluate the fields for the form with test information
        for field in fields:
            self.driver.find_element(By.ID, field).send_keys(fields[field])

        #remove each field one at a time and check if the form still submits
        #each field should be required, so the form should not submit even if all the other fields are filled out
        for field in fields:
            self.driver.find_element(By.ID, field).clear()
            self.assertEqual(self.driver.current_url, "http://127.0.0.1:8000/createEvent")
            self.driver.find_element(By.ID, field).send_keys(fields[field])

    



   


if __name__ == '__main__':
    unittest.main()