import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def get_webdriver(request):
    driver = webdriver.Chrome(r'C:\Users\ilyas\chromedriver\chromedriver.exe')
    driver.get('https://petfriends.skillfactory.ru/login')
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture
def auth_of_user(get_webdriver):
    driver = get_webdriver
    driver.find_element(By.ID, 'email').send_keys('ilyasbadrik@mail.ru')
    driver.find_element(By.ID, 'pass').send_keys('ilias0709')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    driver.find_element(By.CSS_SELECTOR, 'a[href="/my_pets"]').click()
