import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures('get_webdriver', 'auth_of_user')
class TestUsersPage:

    def test_show_count_pets(self):
        count_line_with_pets= WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody tr')))
        assert len(count_line_with_pets) == 4

    def test_pet_image(self):
        pets_images = self.driver.find_elements(By.CSS_SELECTOR, 'th[scope="row"]:first-of-type')
        for i in range(len(pets_images)):
            assert pets_images[i].get_attribute('src') != ''

    def test_name_age_breed(self):
        self.driver.implicitly_wait(5)
        list_name_age_breed = self.driver.find_elements(By.TAG_NAME, 'td')
        for i in range(len(list_name_age_breed)):
            assert list_name_age_breed[i].text != ''

    def test_different_names(self):
        list_pets_names = self.driver.find_elements(By.CSS_SELECTOR, 'td:first-of-type')
        for i in list_pets_names:
            assert i.text in ['Zhulia', 'Dik', 'vasiaca', 'Murchik']

    def test_different_lines(self):
        list_values = self.driver.find_elements(By.CSS_SELECTOR, 'tr td:not(.smart_cell)')
        string_1 = list_values[0].text + ' ' + list_values[1].text + ' ' + list_values[2].text
        string_2 = list_values[3].text + ' ' + list_values[4].text + ' ' + list_values[5].text
        string_3 = list_values[6].text + ' ' + list_values[7].text + ' ' + list_values[8].text
        string_4 = list_values[9].text + ' ' + list_values[10].text + ' ' + list_values[11].text
        assert string_1.split() != string_2.split() or string_1.split() != string_3.split() or string_1.split() != string_4.split()
        assert string_2.split() != string_3.split() or string_2.split() != string_4.split()
        assert string_3.split() != string_4.split()
