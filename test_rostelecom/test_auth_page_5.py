from selenium.webdriver.common.by import By


from pages.auth_page import AuthPage  # импортируем файл auth_page с классом



def test_auth_page_pozitive_five(driver):
    page = AuthPage(driver)  # создаем страницу, передаем в нее вебдрайвер
    page.btnpersaccount_click()  # нажимаем на кнопку
    page.enter_persaccount(" ")

    # Убедимся, что найденный элемент содержит текст

    post_message = driver.find_element(By.CLASS_NAME,
                                        'rt-input__placeholder').text
    assert 'Лицевой' in post_message
