from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password): # тест на получение ключа
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_post_api_create_pet_simple(name='Zhulia', animal_type='dvorniazhka', age='14'): # тест на код ответа 200 и возраст равен 14
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_api_create_pet_simple(auth_key, name, animal_type, age)
    assert status == 200
    assert result['age'] == age

def test_post_api_create_pet_simple_without_data(name='', animal_type='', age=''): # код ответа должен быть 400 при пустых значениях
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_api_create_pet_simple(auth_key, name, animal_type, age)
    assert status == 400

def test_post_api_create_pet_simple_with_incorrect_age(name='Zhulia', animal_type='dvorniazka', age='Fourteen'): # код ответа должен быть 400 при вводе возраста буквами
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_api_create_pet_simple(auth_key, name, animal_type, age)
    assert status == 400

def test_post_api_create_pet_simple_with_long_name(name='Zhulia mestnaia sobaka, kotoraia vseh lyubit i obozhaet',
                                                   animal_type='dvorniazhka', age='14'): # имя не должно быть больше 15 знаков
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_api_create_pet_simple(auth_key, name, animal_type, age)
    assert status == 200
    assert len(result['name']) < 15

def test_post_api_create_pet_simple_with_incorrect_key(name='Zhulia', animal_type='dvorniazhka', age='14'): # код ответа должен быть 403 при неверно введенном ключе
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key['key'] = 'FALSE'
    status, result = pf.post_api_create_pet_simple(auth_key, name, animal_type, age)
    assert status == 403

def test_post_api_create_set_photo(pet_photo='images\lazy_dog.png'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.post_api_create_set_photo(auth_key, pet_id, pet_photo)

    assert status == 200

def test_add_new_pet_with_valid_data(name='Sharik', animal_type='dvorniazhka',
                                     age='15', pet_photo='images\lazy_dog.png'):

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name
