from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.mark.usefixtures("setup")
class TestCase1:
    def test_uname(self):
        expected_url="https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        # self.driver.find_element(By.NAME,"username").send_keys("Abcd")
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        sleep(2)
        # self.driver.find_element(By.CLASS_NAME, "oxd-userdropdown-name").click()
        # self.driver.find_element(By.XPATH, "//a[text()='Logout']").click()
        assert expected_url==self.driver.current_url,"login unsuccessful"
        print("login done")
        sleep(7)
    def test_uname1(self):
       expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
       self.driver.find_element(By.NAME, "username").send_keys("admin")
       self.driver.find_element(By.NAME, "password").send_keys("abc234")

       self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

       # self.driver.find_element(By.CLASS_NAME, "oxd-userdropdown-name").click()
       #
       # self.driver.find_element(By.XPATH, "//a[text()='Logout']").click()
       assert expected_url == self.driver.current_url, "login unsuccessful"
       print("login done")
       sleep(4)
    def test_uname2(self):
       expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
       self.driver.find_element(By.NAME, "username").send_keys("@dmin")
       self.driver.find_element(By.NAME, "password").send_keys("Khushi235")
       sleep(2)
       self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
       sleep(2)
       assert expected_url == self.driver.current_url, "login unsuccessful"
       print("login done")
       # self.driver.find_element(By.CLASS_NAME, "oxd-userdropdown-name").click()
       # sleep(2)
       # self.driver.find_element(By.XPATH, "//a[text()='Logout']").click()
       sleep(5)
    def test_uname3(self):
       expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
       self.driver.find_element(By.NAME, "username").send_keys("Abcd12")
       self.driver.find_element(By.NAME, "password").send_keys("Hii@$^&156")
       self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
       sleep(2)
       self.driver.find_element(By.CLASS_NAME, "oxd-userdropdown-name").click()
       sleep(2)
       self.driver.find_element(By.XPATH, "//a[text()='Logout']").click()
       assert expected_url == self.driver.current_url, "login unsuccessful"
       print("login done")
       sleep(4)


