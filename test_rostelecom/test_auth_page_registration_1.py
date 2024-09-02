from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




def test_auth_page_registration(driver):

    driver.find_element(By.ID, 'kc-register').click()  # нажимаем на кнопку


    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//*[@id="page-right"]/div[1]'))
    )



