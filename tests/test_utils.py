import utils


def test_get_data():
    """
    Тестирование получения данных из файла
    """
    path = "operations.json"
    assert type(utils.get_data(path)) == list
    assert len(utils.get_data(path)) > 0


#def test_get_data():
#    """
#    Тестирование получения данных из сети интернет
#    """
#    url = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1677780904511&signature=dwlMxeMWOfcA9TIA1pRV9u7S7gtu9YCmiaeYbzjfIXw&downloadName=operations.json"
#    assert get_data(url) is not None
#    url = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1677780904511&signature=dwlMxeMWOfcA9TIA1pRV9u7S7gtu9YCmiaeYbzjfIXw&downloadNam=operations.json"
#    data, info = get_data(url)
#    assert data is None
#    assert info == "WARNING: Статус ответа 400"
#    url = "https://fil.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1677780904511&signature=dwlMxeMWOfcA9TIA1pRV9u7S7gtu9YCmiaeYbzjfIXw&downloadNam=operations.json"
#    data, info = get_data(url)
#    assert data is None
#    assert info == "ERROR: requests.exceptions.ConnectionError"


def test_get_filtered_data(test_data):
    """
    Тестирование фильтрации данных
    """
    data = utils.get_filtered_data(test_data, filtered_empty_from=False)
    assert len(data) == 4
    data = utils.get_filtered_data(test_data, filtered_empty_from=True)
    assert len(data) == 3


def test_get_last_data(test_data):
    """
    Тестирование данных на сортировку по дате
    """
    data = utils.get_last_data(test_data, count_last_values=3)
    assert data[0]["date"] == "2019-12-07T06:17:14.634890"
    assert len(data) == 3


def test_get_formatted_data(test_data):
    """
    Тестирование данных на верное форматирование
    """
    # Проверка на правильное форматирование при отправлении с карты на счёт
    data = utils.get_formatted_data(test_data[:1])
    assert data == ['29-09-2019 Перевод организации\nVisa Classic 2842 87** **** 9012 -> Счет **3655\n48150.39 USD\n']
    # Проверка на правильное форматирование при отсутствии "from"
    data = utils.get_formatted_data(test_data[1:2])
    assert data == ['30-10-2019 Перевод организации\n[СКРЫТО]  -> Счет **2869\n30153.72 RUB\n']
    # Проверка на правильное форматирование при отправлении со счёта на счёт
    data = utils.get_formatted_data(test_data[2:3])
    assert data == ['19-11-2019 Перевод со счета на счет\nСчет **9794 -> Счет **8125\n62814.53 RUB\n']
    # Проверка на правильное форматирование при отправлении со счёта на карту
    data = utils.get_formatted_data(test_data[3:4])
    assert data == ['07-12-2019 Перевод со счета на карту\nСчет **9453 -> Visa Gold 7756 67** **** 2839\n23036.03 RUB\n']
