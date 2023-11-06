from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from time import sleep
import unittest

"""
PREREQUISITE: You have at least one event.
SIDE EFFECT: 'permanently' adds 2 new attendees to your event
"""
class JosuaTestCases(unittest.TestCase):
    
    
    """
    This funciton opens the home page of our website,
    navigates to the view events page, and clicks on the first event.
    """
    def setUp(self):
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        print("Starting Test:", "\n")

        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://127.0.0.1:8000/")

        view_events_button = self.driver.find_element(By.LINK_TEXT, "View Events")
        view_events_button.click()

        events = self.driver.find_elements(By.CLASS_NAME, "event")

        events[0].click()

        rsvp_button = self.driver.find_elements(By.CLASS_NAME, "button")
        rsvp_button[4].click()


    """
    Test 1: RSVP Functionality
    signs a Fish up for the event and checks the latest item on the
    attendees list to see if it matches.
    """
    def testRSVP(self):
        print("testing rsvp funcitonality") 

        self.driver.find_element(By.ID, "id_name").send_keys("Fish")
        submit_button = self.driver.find_element(By.CLASS_NAME, "is-success")
        submit_button.click()

        attendees = self.driver.find_elements(By.CLASS_NAME, "m-1")
        most_recent_attendee = attendees[len(attendees) - 1]
        assert "Fish" in most_recent_attendee.text
        print("TEST PASSED: RSVP FUNCTIONALITY", "\n")

    """
    Test 2: RSVP Character length
    Puts a giant sentence into the RSVP form, which is cut off.
    Checks the latest item on the list of attendees to see
    if it matches the cut-off entry.
    """
    def testRSVPCharacterLength(self):
        print("testing rsvp character limit")

        self.driver.find_element(By.ID, "id_name").send_keys("This message just so happens to go over the character limit!")
        submit_button = self.driver.find_element(By.CLASS_NAME, "is-success")
        submit_button.click()

        attendees = self.driver.find_elements(By.CLASS_NAME, "m-1")
        most_recent_attendee = attendees[len(attendees) - 1]
        assert "This message just so happens to go over the charac" in most_recent_attendee.text
        print("TEST PASSED: RSVP CHARACTER LIMIT", "\n")

        

if __name__ == '__main__':
    unittest.main()

