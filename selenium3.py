#!/bin/python

"""
goto  wp.pl
sprawdz czy jest wybrane slowo
sprawdz czy wystepuje wiecej niz jeden
"""

import unittest
from selenium import webdriver
from time import sleep

search_word = "Morawiecki"

class SearchText(unittest.TestCase):

    def setUp(self):
        # create a new Firefox session

        self.driver = webdriver.Chrome()
        driver = self.driver
        # driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://www.wp.pl")


    def test_search_word_Morawiecki(self):
        '''
        driver = self.driver
        results = driver.find_elements_by_xpath('//div[contains(text(),"' + search_word + '")]')
        print(results[1].text)
        self.assertGreater(len(results), 1)
        sleep(5)
        '''

    def tearDown(self):
        # close the browser window
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
