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
    test for issue #99 - test cases 1-6
      - all fields must required to create an event
    """
    def testcreateEventRequiredFeilds(self):
        self.driver.find_element(By.ID, "planEvent").click()
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:8000/createEvent")

        self.driver.find_element(By.ID, "submit").click()
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:8000/createEvent")

        fields = {"title": "test event", "host": "test host", "location": "test location", "date": "2021-05-05", "time": "12:00", "description": "test description"}

        #popluate the fields for the form with test information
        for field in fields:
            self.driver.find_element(By.ID, field).send_keys(fields[field])

        #remove each field one at a time and check if the form still submits
        #each field should be required, so the form should not submit even if all the other fields are filled out
        for field in fields:
            self.driver.find_element(By.ID, field).clear()
            self.assertEqual(self.driver.current_url, "http://127.0.0.1:8000/createEvent")
            self.driver.find_element(By.ID, field).send_keys(fields[field])


    """
    test for issue 98 - test cases 8
        - user should be able to update their username on the manage.py account page
    """
    def testUpdateUsername(self):
        self.driver.find_element(By.ID, "manageAccount").click()
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:8000/manageAccount")

        #update the username
        self.driver.find_element(By.ID, "username").clear()
        self.driver.find_element(By.ID, "username").send_keys("test2")
        self.driver.find_element(By.ID, "submit").click()

        #check if the username was updated
        self.driver.find_element(By.ID, "manageAccount").click()
        self.assertEqual(self.driver.find_element(By.ID, "username").get_attribute("value"), "test2")

        #reset the username back to test
        self.driver.find_element(By.ID, "username").clear()
        self.driver.find_element(By.ID, "username").send_keys("test")
        self.driver.find_element(By.ID, "submit").click()

    """
    test for issue 101 - test case 9
        - user should be able to sign up with username, first name, last name, email, and password
        Note: instead of creating a new account everything, we are just making sure 
        that those input fields exist on the sign up page and assume that they information can be entered. 
    """
    def testcreateNewUsername(self):
        self.driver.find_element(By.ID, "logoutButton").click()
        self.driver.find_element(By.ID, "signup").click()
        try:    
            self.driver.find_element(By.ID, "first")
        except:
            self.fail("first name input does not exist")
        
        try:
            self.driver.find_element(By.ID, "last")
        except:
            self.fail("last name input does not exist")

        try:
            self.driver.find_element(By.ID, "username")
        except:
            self.fail("username input does not exist")

        try:
            self.driver.find_element(By.ID, "email")
        except:
            self.fail("email input does not exist")
        

        try:
            self.driver.find_element(By.ID, "password")
        except:
            self.fail("password input does not exist")
        
    """
    Test for issue 100 - test case 12
    - user should not be able to enter more than 30 characters into the task input. 
    """
    def testTaskMaxLength(self):
        self.driver.find_element(By.ID, "planEvent").click()
        self.driver.find_element(By.ID, "addTaskBttn").click()

        for i in range(31):
            self.driver.find_element(By.ID, "taskInput").send_keys("a")
        
        self.assertEqual(self.driver.find_element(By.ID, "taskInput").get_attribute("value"), "a"*30)

    """
    Test for issue 107 - test case 19
    - user should be able to go back to the event page from the create event page using the cacncel button
    """
    def testCancelButton(self):
        self.driver.find_element(By.ID, "planEvent").click()
        self.driver.find_element(By.ID, "cancelButton").click()
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:8000/events/")


    """
    Test for issue 98 - test case 22
    - if the user enters their current username in the form, 
      they should get than error preventing them from doing so
    
    """
    def testUpdateExistingUsername(self):
        self.driver.find_element(By.ID, "manageAccount").click()
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:8000/manageAccount")

        #update the username
        self.driver.find_element(By.ID, "username").clear()
        self.driver.find_element(By.ID, "username").send_keys("test")
        self.driver.find_element(By.ID, "submit").click()

        self.assertEqual(self.driver.find_element(By.ID, "error_message").text, "Username is already taken")
    
    
    """
    Test for issue 98 - test case 23
    - if the user is logged out and try to navgate to the manage account page, 
      they should be blocked from doing so and be redirected to the login page
    """
    def testAccessAccountPage(self):
        self.driver.find_element(By.ID, "logoutButton").click()
        self.driver.get("http://127.0.0.1:8000/manageAccount")
        self.assertNotEqual(self.driver.current_url, "http://127.0.0.1:8000/manageAccount")

        

    def tearDown(self):
        self.driver.quit()
        print("testing complete")
        

    



   


if __name__ == '__main__':
    unittest.main()