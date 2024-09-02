from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.auth_page import AuthPage  # импортируем файл auth_page с классом
import time


def test_auth_page_pozitive(driver):
    page = AuthPage(driver)  # создаем страницу, передаем в нее вебдрайвер
    page.enter_email("goginaginus@gmail.com")  # вводим емейл
    page.enter_pass("111222333aA")  # вводим пароль
    time.sleep(5)
    page.btn_click()  # нажимаем на кнопку

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//*[@id="app"]/main[1]/div[2]/div[1]/div[1]/div[1]/h2[1]'))
    )

    # Убедимся, что найденный элемент содержит текст 'Иванов Иван'
    assert driver.find_element(By.XPATH, '//*[@id="app"]/main[1]/div[2]/div[1]/div[1]/div[1]/h2[1]').text == 'Иванов Иван'

    driver.find_element(By.CSS_SELECTOR, 'div#logout-btn').click()