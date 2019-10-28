
from selenium.webdriver.common.by import By
from .base_page import BasePage

class MainPage(BasePage):
    def go_to_login_page(self):
        self.login_link = self.browser.find_element(By.CSS_SELECTOR,'#login_link')
        self.login_link.click()