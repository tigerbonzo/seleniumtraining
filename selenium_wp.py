#!/bin/python

import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestWpPoczta(unittest.TestCase):

    valid_username = "testerwsb_t1"
    valid_password = "adam1234"

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://www.wp.pl"")
        self.driver.find_element_by_link_text('Poczta').click()
        sleep(5)


    def properLogin(self):
        driver = self.driver
        #driver.find_element_by_id


#    def WrongPassword(self):


#    def wrongUserName(self):


#    def WrongPasswordAndUser(self):


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
