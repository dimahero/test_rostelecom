from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.auth_page import AuthPage  # импортируем файл auth_page с классом

def test_auth_page_pozitive_seven(driver):
    page = AuthPage(driver)  # создаем страницу, передаем в нее вебдрайвер
    page.help_click()  # нажимаем на кнопку

    # Явное ожидание, чтобы убедиться, что элемент доступен
    help_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/div[1]/div[1]/h1[1]'))
    ).text

    assert 'Ваш безопасный ключ' in help_text