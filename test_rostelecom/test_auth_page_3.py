from selenium.webdriver.common.by import By


from pages.auth_page import AuthPage  # импортируем файл auth_page с классом



def test_auth_page_pozitive_three(driver):
    page = AuthPage(driver)  # создаем страницу, передаем в нее вебдрайвер
    page.btnpost_click()  # нажимаем на кнопку
    page.enter_email(" ")

    # Убедимся, что найденный элемент содержит текст

    post_message = driver.find_element(By.CLASS_NAME,
                                        'rt-input__placeholder').text
    assert 'Электронная' in post_message
