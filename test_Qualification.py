from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.mark.usefixtures("setup1")
class TestCase1:
    def test_admin(self):
        sleep(3)
        self.driver.find_element(By.XPATH, "//span[text()='Admin']").click()
        sleep(2)
        self.driver.find_element(By.XPATH,"//span[text()='Qualifications ']").click()
        sleep(1)
        self.driver.find_element(By.XPATH,"//a[text()='Skills']").click()
        sleep(1)
        self.driver.find_element(By.XPATH,"//button[text()=' Add ']").click()
        sleep(1)
        self.driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]").send_keys("Vasu")
        sleep(1)
        self.driver.find_element(By.XPATH,"//textarea[@placeholder='Type description here']").send_keys("sql")
        sleep(1)
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        sleep(8)


