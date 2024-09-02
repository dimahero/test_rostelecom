from urllib.parse import urlparse

class BasePage(object):
    # конструктор класса - специальный метод с ключевым словом __init__
    # Нам нужны объект веб-драйвера, адрес страницы и время ожидани элементов
    #автоматически вызывается и задает параметры

    def __init__(self, driver, url, timeout=10): #ссылка на драйвер юрл,таймаут (прогрузиться странице)
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)


#доп метод - дает относительный путь. В стандартной библиотеке есть метод driver.current_url
# метод будет выдавать путь без домена (напр ya.com/login будет выдавать путь login)

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path