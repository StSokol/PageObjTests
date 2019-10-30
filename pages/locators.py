
from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR,"#login_link")
    #LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators():
    URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR,"#login_form")
    REGISTRATION_FORM =(By.CSS_SELECTOR,"#register_form")

class ProductPageLocators():
    PRODUCT_ARTICLE = (By.CSS_SELECTOR,".product_page .product_main")
    PROD_NAME_ON_PAGE = (By.CSS_SELECTOR,"div.product_main h1")
    PROD_PRICE_ON_PAGE = (By.CSS_SELECTOR,"div.product_main p.price_color")
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR,".btn-add-to-basket")
    PROD_NAME_ADDED_HINT = (By.CSS_SELECTOR,".page_inner .alertinner strong")
    PROD_PRICE_ADDED_HINT = (By.CSS_SELECTOR, ".page_inner .alertinner strong")