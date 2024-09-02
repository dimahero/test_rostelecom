from selenium.webdriver.common.by import By




def test_auth_page_registration_negative(driver):

    # Возвращаемся на начальную страницу
    driver.get("https://b2c.passport.rt.ru")

    driver.find_element(By.ID, 'kc-register').click()

    driver.find_element(By.NAME, 'firstName').send_keys('П')
    driver.find_element(By.NAME, 'lastName').send_keys('Петров')
    driver.find_element(By.ID, 'address').send_keys('petrov954759@mail.ru')
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('111222333Bb')
    driver.find_element(By.XPATH, '//*[@id="password-confirm"]').send_keys('111222333Bb')

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()


    # Убедимся, что найденный элемент содержит текст
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]').text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'




