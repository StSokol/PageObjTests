from PageObjTests.pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)  # получить страницу
    page.open()
    page.should_be_product_page()

    # проверить наименование и запомнить
    prod_name_before = page.should_be_prod_name_on_page().text
    # проверить наличие цены и запомнить
    prod_price_before = page.should_be_prod_price_on_page().text

    # проверить кнопку корзины
    page.add_to_basket()

    # проверить наименование добавленного товара и сравнить
    page.should_be_added_prod_name_the_same(prod_name_before)

    #проверить цену добавленную в корзину и сравнить с ценой товара
    page.should_be_added_prod_price_the_same(prod_price_before)
