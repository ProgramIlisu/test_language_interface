import time
from selenium.webdriver.common.by import By
def test_product_page_has_add_to_cart_button(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/."
    browser.get(url)

    # Визуальная проверка языка 
    time.sleep(3)

    button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    time.sleep(2)

    assert len(button) > 0, "Кнопка добавления в корзину НЕ найдена!"
