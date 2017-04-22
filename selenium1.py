#!/bin/python

import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


valid_username = "testerwsb_t1"
valid_password = "adam1234"


class TestWpPoczta(unittest.TestCase):



    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        # driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://www.wp.pl")


    def properLogin(self):

        driver = self.driver
        driver.find_element_by_link_text('Poczta').click()
        #login_field = WebDriverWait(self.driver,10).until( #EC.presence_of_element_located(By.ID,"login"))
        #login_field = driver.find_element_by_id("login")
        #login_field.sendKeys(valid_username)
        #login_field.send = driver.find_element_by_id("password")
        #login_field.sendKeys(valid_password)

    def tearDown(self):
        # close the browser window
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
