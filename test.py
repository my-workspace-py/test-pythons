import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
#import pyautogui
import time


class TestClass:
    def test_Login(self):
        driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.implicitly_wait(5)
        driver.maximize_window()

        driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys('Admin')
        driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys('admin123')
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(5)
        print("Successfully logged in")