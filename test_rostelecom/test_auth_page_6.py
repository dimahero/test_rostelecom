from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.auth_page import AuthPage  # импортируем файл auth_page с классом

def test_auth_page_pozitive_six(driver):
    page = AuthPage(driver)  # создаем страницу, передаем в нее вебдрайвер
    page.agreement_click()  # нажимаем на кнопку

        # Сохраняем текущее окно
    original_window = driver.current_window_handle

        # Ожидаем появления новой вкладки
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

        # Переключаемся на новую вкладку
    new_window = [window for window in driver.window_handles if window != original_window][0]
    driver.switch_to.window(new_window)

        # Явное ожидание, чтобы убедиться, что элемент доступен в новой вкладке
    agreement_text = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="title"]/h1'))
        ).text

    assert 'Публичная оферта' in agreement_text

        # Закрываем новую вкладку и возвращаемся на исходную
    driver.close()
    driver.switch_to.window(original_window)