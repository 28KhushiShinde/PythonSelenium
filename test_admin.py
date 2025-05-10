from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.mark.usefixtures("setup")
class TestCase2:
    def test_admin(self):
        expected_url="https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"
        self.driver.find_element(By.XPATH,"//span[text()='Admin']").click()
        sleep(2)
        actual_url=self.driver.current_url
        assert expected_url==actual_url,"You are in wrong page"
        print("You are in right page")
        self.driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]").send_keys("")


