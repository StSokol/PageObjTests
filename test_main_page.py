
#from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    page = MainPage(browser,link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page(browser):
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = MainPage(browser,link)

    page.open()   # открываем страницу
    page.go_to_login_page() # выполняем метод страницы - переходим на страницу логина

    login_page = LoginPage(browser, browser.current_url)   #загружаем страницу регистрации-логина
    login_page.should_be_login_page()        # запускаем ее стандартные проверки




