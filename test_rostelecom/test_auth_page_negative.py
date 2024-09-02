from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.auth_page import AuthPage  # импортируем файл auth_page с классом
import time

def test_auth_page_negative(driver):
    page = AuthPage(driver)  # создаем страницу, передаем в нее вебдрайвер
    page.enter_email("goginaginus@gmail.com")  # вводим емейл
    page.enter_pass("1111222333aA")  # вводим неверный пароль
    time.sleep(5)
    page.btn_click()  # нажимаем на кнопку

    # Ожидаем, что появится заголовок с текстом ошибки или другой ожидаемый элемент
    error_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]'))
    )

    # Проверяем текст ошибки (пример текста 'Неверный логин или пароль')
    assert error_element.text == "Неверный логин или пароль", f"Expected error message not found, got: '{error_element.text}'"

