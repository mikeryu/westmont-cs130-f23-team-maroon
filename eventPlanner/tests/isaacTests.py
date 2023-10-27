from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from time import sleep

import unittest

class TestIsaac(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        print("testing started")
        self.driver = webdriver.Chrome(options=options)

        self.driver.get("http://127.0.0.1:8000/events")
        sleep(3)

    def testLinktoEventDetail(self):
        events = self.driver.find_elements(By.CLASS_NAME, "event")

        title = events[0].text.split("\n")[0]

        events[0].click()

        sleep(3)

        self.assertIn("http://127.0.0.1:8000/event/", self.driver.current_url); 
        self.assertEqual(title, self.driver.find_element(By.ID, "title").text)
if __name__ == '__main__':
    unittest.main()
    