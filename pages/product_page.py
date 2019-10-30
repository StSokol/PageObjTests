from .base_page import BasePage
from .locators import ProductPageLocators
from operator import attrgetter

class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_product_form()
        self.should_be_add_to_basket_btn()

    def should_be_product_url(self):
        # проверка на корректный url адрес
        #print(self.browser.current_url)
        #print(r'/catalogue/' in self.browser.current_url)
        assert r'/catalogue/' in self.browser.current_url, "The link looks like incorrect"


    def should_be_product_form(self):
        # здесь должно быть описание товара
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ARTICLE), "Product description was not found"

    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), "Button 'Add to Busket' hasn't been found"

    def add_to_basket(self):
        #если не упали проверяем дальше
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN).click()

        #посчитать и показать код
        self.solve_quiz_and_get_code()


    def should_be_prod_name_on_page(self):
        element = self.get_element_if_exist(*ProductPageLocators.PROD_NAME_ON_PAGE)
        assert element, "Product name hasn't been found on page"
        return element


    def should_be_prod_price_on_page(self):
        element = self.get_element_if_exist(*ProductPageLocators.PROD_PRICE_ON_PAGE)
        assert element, "Product price hasn't been found on page"
        return element

    def should_be_added_prod_name_the_same(self,prod_name_before):
        assert self.is_element_present(*ProductPageLocators.PROD_NAME_ADDED_HINT), \
            "Product name hasn't been observed as added to the basket"

        elements = list(map(attrgetter('text'),
                            self.browser.find_elements(*ProductPageLocators.PROD_NAME_ADDED_HINT) ))
        assert prod_name_before in elements, "Product name hasn't been observed as added to the basket"

    def should_be_added_prod_price_the_same(self,prod_price_before):
        # надо переделать - этот вариант работает только для первого товара,
        # дальше должна быть переменная сумма на цену добавленного товара
        assert self.is_element_present(*ProductPageLocators.PROD_PRICE_ADDED_HINT), \
            "Product price hasn't been observed as added to the basket"

        elements = list(map(attrgetter('text'),
                            self.browser.find_elements(*ProductPageLocators.PROD_PRICE_ADDED_HINT) ))
        assert prod_price_before in elements, "Product price hasn't been observed as added to the basket"