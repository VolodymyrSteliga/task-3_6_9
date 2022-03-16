from selenium.webdriver.common.by import By


class TestBasket:
    def test_add_goods_to_basket(self, browser):
        browser.implicitly_wait(2)
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        list_of_names_buttons = browser.find_elements(
            By.CSS_SELECTOR, ".btn-add-to-basket"
        )
        assert len(
            list_of_names_buttons
        ), "button 'Add to basket' not found on the page !"
