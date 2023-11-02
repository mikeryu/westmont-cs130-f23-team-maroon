from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import unittest
from time import sleep

class LeviTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument("--headless=new")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        print("Testing started")
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(2)
        self.driver.get("http://127.0.0.1:8000/events")  # open Create Event
        self.assertIn("http://127.0.0.1:8000/event", self.driver.current_url) # make sure I am in the correct site

    """
    Test for issue #49
    """
    def test_RSVP(self):
        numEvents = len(self.driver.find_elements(By.CLASS_NAME, "event")) 
        for num in range(numEvents):
            self.driver.find_elements(By.CLASS_NAME, "event")[num].click() # open the next event
            self.driver.find_element(By.CLASS_NAME, "rsvp-button").click() # click rsvp button
            self.driver.find_element(By.ID, "id_name").send_keys("Test RSVP") # RSVP under 'Test RSVP'
            self.driver.find_element(By.CLASS_NAME, "button.is-success").click() # submit RSVP
            attendees = self.driver.find_elements(By.CLASS_NAME, "attendee") # find the name
            self.assertEqual(attendees[len(attendees) - 1].text, "Test RSVP")
            print(num + " test(s) complete.")
            self.driver.get("http://127.0.0.1:8000/events")  # open Create Event

if __name__ == '__main__':
    unittest.main()
