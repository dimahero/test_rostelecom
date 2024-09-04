# test_rostelrcom
Это программа, написанная на Python, предназначена для автотестирования сайта Ростелеком
Для запуска тестов необходимо следующее:
  - папка с драйвером Chromedriver должна находиться в директории нахождения набора тест-кейсов
  - установить библиотеки selenium и pytest
  - в терминале PyCharm вбить команду: python -m pytest -v --driver Chrome --driver-path /Chromedriver/chromedriver.exe test_rostelecom.py
