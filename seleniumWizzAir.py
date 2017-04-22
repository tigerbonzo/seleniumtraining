# -*- coding: utf-8" -*
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

valid_name = "Dick"
valid_surname = "Laurent"
telefon = "123123123"
invalid_email = "hhjkj.pl"
valid_password = "Qshiukk12"
name1="Marianna"
surname1="Kowalska"
cellnumber1 = "48558741156"
email1 = "mkowalska@@xxx.xx"


class TestWizzAir(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_wizzair_niepoprawne(self):
        driver = self.driver
        driver.get("https://wizzair.com/pl-pl/main-page#/")
        login_btn = driver.find_element_by_css_selector("li.navigation__item:nth-child(3) > button:nth-child(1)")
        login_btn.click()
        signup_btn = driver.find_element_by_css_selector("p.login-form__footer:nth-child(6) > button:nth-child(1)")
        signup_btn.click()


        #imie
        namefield = driver.find_element_by_xpath("//input[@placeholder='Imię']")
        namefield.send_keys(name1)

        #imie_field = driver.find_element_by_xpath("//input[@placeholder='Imię']")
        #imie_field.send_keys(valid_name)

        surnamefield= driver.find_element_by_xpath("//input[@placeholder='Nazwisko']")
        surnamefield.send_keys(surname1)

        gender_switch = driver.find_element_by_id("register-gender-female")
        driver.execute_script("arguments[0].click()", gender_switch)
        #driver.find_elements_by_xpath("")
        cellnumber = driver.find_element_by_css_selector("input[placeholder='Telefon komórkowy']")
        cellnumber.send_keys(cellnumber1)
        emailfield = driver.find_element_by_css_selector("input[data-test='booking-register-email']")
        emailfield.send_keys(email1)

        sleep(5)

        # li.navigation__item:nth-child(3) > button:nth-child(1)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
