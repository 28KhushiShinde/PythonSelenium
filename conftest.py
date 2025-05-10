from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.fixture
def setup(request):
    # global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.implicitly_wait(15)
    request.cls.driver = driver
    yield
    driver.close()
@pytest.fixture()
def setup1(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    # expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    driver.maximize_window()

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.implicitly_wait(15)
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    sleep(2)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    sleep(2)
    request.cls.driver=driver
    yield
    driver.find_element(By.CLASS_NAME, "oxd-userdropdown-name").click()
    sleep(2)
    driver.find_element(By.XPATH, "//a[text()='Logout']").click()
    sleep(7)
    driver.close()