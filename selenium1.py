#-*- coding: utf-8 -*-

import unittest
from selenium import webdriver


class SeleniumTraing1(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Firefox()

    def testCase1(self):
        driver=self.driver
        driver.get("http://www.wsb.pl")
        self.assertIn("Wyższe Szkoły Bankowe".decode("utf-8"), driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
