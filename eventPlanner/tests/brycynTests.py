from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import unittest
from time import sleep

class BrycynTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        print("Testing started")
        self.driver = webdriver.Chrome(options=options)

        self.driver.get("http://127.0.0.1:8000/createEvent")  # open Create Event
        sleep(3)
        self.assertIn("http://127.0.0.1:8000/createEvent", self.driver.current_url) # make sure I am in the correct site


    def test_addTask(self):
        self.driver.find_element(By.CLASS_NAME, "button.is-link").click()  # click add task 
        sleep(3)
        self.driver.find_element(By.ID, "taskInput").send_keys("helping out") #type task
        sleep(3)
        self.driver.find_element(By.ID, "addTaskButton").click() # confirm task
        sleep(3)
        

        add_task = self.driver.find_element(By.NAME, "task-item").get_attribute('value') #get the value of task (input) field
        self.assertEqual(add_task, "helping out")

if __name__ == '__main__':
    unittest.main()
