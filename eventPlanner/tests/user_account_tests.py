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
    
    # Sprint 3: Test Case #3
    def test_create_event_w_task(self):
        with chrome_driver() as driver:
            user_login(driver=driver)
            driver.get(self.url + "events")
            events = [event.text for event in driver.find_elements(By.CLASS_NAME, "title")]
            # so as to not create a new TestEvent upon each run
            if "TestEvent" not in events:
                driver.get(self.url + "createEvent")
                self.assertEqual(driver.current_url, self.url + "createEvent")
                driver.find_element(By.ID, "title").send_keys("TestEvent")
                driver.find_element(By.ID, "host").send_keys("test")
                driver.find_element(By.ID, "location").send_keys("test location")
                driver.find_element(By.ID, "time").send_keys("11/11/11")
                driver.find_element(By.ID, "description").send_keys("This is my test event description.")
                driver.find_element(By.CSS_SELECTOR, ".mr-2").click()
                driver.find_element(By.ID, "taskInput").send_keys("Test Task")
                driver.find_element(By.ID, "addTaskButton").click()
                driver.find_element(By.ID, "submit").click()
                driver.get(self.url + "events")
            events = driver.find_elements(By.CLASS_NAME, "title")
            events = [event.text for event in events]
            self.assertTrue("TestEvent" in events)


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
    
    # Sprint 3: Test Case #6
    def test_too_many_characters_other_fields(self):
        with chrome_driver() as driver:
            user_login(driver=driver) # helper login function
            driver.get(self.url + "createEvent")
            self.assertEqual(driver.current_url, self.url + "createEvent")
    
            inputstr = " ".join(["test" for i in range(1000)])
            
            # check host
            hostInput = driver.find_element(By.ID, "host")
            hostInput.send_keys(inputstr)
            hostText = hostInput.get_attribute("value")
            self.assertEqual(len(hostText), 100)
    
            # check time
            timeInput = driver.find_element(By.ID, "time")
            timeInput.send_keys(inputstr)
            timeText = timeInput.get_attribute("value")
            self.assertEqual(len(timeText), 100)

            # check location 
            locationInput = driver.find_element(By.ID, "location")
            locationInput.send_keys(inputstr)
            locText = locationInput.get_attribute("value")
            self.assertEqual(len(locText), 100)

    
    # Sprint 3: Supplementary Test Case 
    def test_rsvp(self):
        with chrome_driver() as driver:
            user_login(driver)
            self.assertEqual(driver.current_url, self.url + "events/")
            events = driver.find_elements(By.CLASS_NAME, "event") # grab all of the events
            events[0].click() # click on the first one
            driver.find_element(By.CLASS_NAME, "rsvp-button").click() # click rsvp button
            driver.find_element(By.ID, "id_name").send_keys(str(hash(self))) # RSVP under 'Test RSVP'
            driver.find_element(By.CLASS_NAME, "button.is-success").click() # submit RSVP
            attendees = driver.find_elements(By.CLASS_NAME, "attendee") # find the name
            self.assertEqual(attendees[len(attendees) - 1].text, str(hash(self)))

    # Sprint 3: Test Case #7
    def test_rsvp_refresh(self):
        with chrome_driver() as driver:
            user_login(driver)
            self.assertEqual(driver.current_url, self.url + "events/")
            events = driver.find_elements(By.CLASS_NAME, "event") # grab all of the events
            events[0].click() # click on the first one
            driver.find_element(By.CLASS_NAME, "rsvp-button").click() # click rsvp button
            driver.find_element(By.ID, "id_name").send_keys(str(hash(self))) # RSVP under 'Test RSVP'
            driver.find_element(By.CLASS_NAME, "button.is-success").click() # submit RSVP
            driver.refresh() # refresh the page 
            attendees = driver.find_elements(By.CLASS_NAME, "attendee") # find the name
            # check the previous two RSVPs
            self.assertEqual(attendees[len(attendees) - 1].text, str(hash(self)))
            self.assertNotEqual(attendees[len(attendees) - 2].text, str(hash(self)))

    # Sprint 3: Test Case #10
    def test_login(self):
        with chrome_driver() as driver:
            user_login(driver)
            self.assertEqual(driver.current_url, self.url + "events/")

    # Sprint 3: Test Case #11
    def test_not_logged_in(self):
        with chrome_driver() as driver: 
            driver.get(self.url)
            driver.find_element(By.ID, "events").click()
            self.assertEqual(driver.current_url, self.url + "login?next=/events/")


if __name__ == '__main__':
    unittest.main()