from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import unittest

class TestAllie(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        print("testing started")
        self.driver = webdriver.Chrome(options=options)

        self.driver.get("http://127.0.0.1:8000/events")
        sleep(3)
        # start on the events page in order to show button brings to home 
        self.assertIn("http://127.0.0.1:8000/events", self.driver.current_url) 

    
    
    
    """
    test for issue #45 and #47 - 
    makes sure that clicking on the event logo takes you to the home page
    """
    def testLogoLinkToHome(self):
        # click on logo button 
        self.driver.find_element(By.ID, "navbarLogo").click()
        sleep(3)

        # check if the page we are on is the home page 
        self.assertIn("http://127.0.0.1:8000", self.driver.current_url); 

if __name__ == '__main__':
    unittest.main()        
