import pytest


@pytest.fixture
def test_data():
    return[
        {'id': 114832369,
        'state': 'EXECUTED',
        'date': '2019-09-29T14:25:28.588059',
        'operationAmount': {'amount': '48150.39',
                            'currency': {'name': 'USD', 'code': 'USD'}},
        'description': 'Перевод организации',
        'from': 'Visa Classic 2842878893689012',
        'to': 'Счет 35158586384610753655'},
       {'id': 154927927,
        'state': 'EXECUTED',
        'date': '2019-10-30T01:49:52.939296',
        'operationAmount': {'amount': '30153.72',
                            'currency': {'name': 'руб.', 'code': 'RUB'}},
        'description': 'Перевод организации',
        'to': 'Счет 43241152692663622869'},
       {'id': 482520625,
        'state': 'EXECUTED',
        'date': '2019-11-19T09:22:25.899614',
        'operationAmount': {'amount': '62814.53',
                            'currency': {'name': 'руб.', 'code': 'RUB'}},
        'description': 'Перевод со счета на счет',
        'from': 'Счет 38611439522855669794',
        'to': 'Счет 46765464282437878125'},
       {'id': 509645757,
        'state': 'CANCELED',
        'date': '2019-12-07T06:17:14.634890',
        'operationAmount': {'amount': '23036.03',
                            'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод со счета на карту',
        'from': 'Счет 48943806953649539453',
        'to': 'Visa Gold 7756673469642839'},
       {'id': 888407131,
        'state': 'EXECUTED',
        'date': '2019-11-13T17:38:04.800051',
        'operationAmount': {'amount': '45849.53',
                            'currency': {'name': 'USD', 'code': 'USD'}},
        'description': 'Перевод со счета на счет',
        'from': 'Счет 35421428450077339637',
        'to': 'Счет 46723050671868944961'}
       ]