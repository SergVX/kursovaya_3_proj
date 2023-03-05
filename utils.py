import requests
import json
from _datetime import datetime


def get_data(path) -> list:
    """
    Открывает файл json и возвращает в переменную для дальнейшей работы.
    :param path: путь к файлу с данными.
    :return: Список словарей.
    """
    with open(path, "r", encoding="UTF-8") as file:
        data = json.load(file)

        return data


#def get_data(url) -> list:
#    """
#    Получает данные через URL и возвращает в переменную для дальнейшей работы.
#    :param url: путь в сети интернет.
#    :return: Список словарей
#    try:
#        response = requests.get(url)
#        if response.status_code == 200:
#            return response.json(), "INFO: Данные получены успешно!"
#        return None, f"WARNING: Статус ответа {response.status_code}"
#    except requests.exceptions.ConnectionError:
#        return None, "ERROR: requests.exceptions.ConnectionError"


def get_filtered_data(data, filtered_empty_from=False) -> list:
    """
    Фильтрует данные по ключам "state" и "from".
    :param data: Список словарей.
    :param filtered_empty_from: type -> bool фильтрация по ключу "from".
    :return: Список словарей.
    """
    data = [x for x in data if "state" in x and x["state"] == "EXECUTED"]
    if filtered_empty_from:
        data = [x for x in data if "from" in x]
    return data


def get_last_data(data, count_last_values) -> list:
    """
    Функция вывода последних значений сортированных данных по ключу "date".
    :param data: Список словарей.
    :param count_last_values: Количество данных для вывода.
    :return: Список словарей.
    """
    data = sorted(data, key=lambda x: x["date"], reverse=True)
    return data[:count_last_values]


def get_formatted_data(data) -> list:
    """
    Функция принимает список отсортированных словарей и форматирует вывод согласно требованиям.
    :param data: Список словарей.
    :return: Список отформатированных данных в виде строки.
    """
    formatted_data = []
    for row in data:
        # Форматирует дату
        date = datetime.strptime(row["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d-%m-%Y")
        # Описание операции
        description = row["description"]

        # Форматирование отправителя
        # Если ключ "from" имеется в данных
        if "from" in row:
            sender = row["from"].split()
            sender_bill = sender.pop(-1)
            # Если деньги отправили с карты
            if len(sender_bill) == 16:
                sender_bill = f"{sender_bill[:4]} {sender_bill[4:6]}** **** {sender_bill[-4:]}"
            # Если деньги отправили со счета
            else:
                sender_bill = f"**{sender_bill[-4:]}"
            sender_info = " ".join(sender)
        # Если ключ "from" отсутствует в данных
        else:
            sender_bill, sender_info = "", "[СКРЫТО]"

        # Форматирование получателя
        recipient = row['to'].split()
        recipient_bill = recipient.pop(-1)
        # Если деньги получили на карту
        if len(recipient_bill) == 16:
            recipient_bill = f"{recipient_bill[:4]} {recipient_bill[4:6]}** **** {recipient_bill[-4:]}"
        # Если деньги получили на счет
        else:
            recipient_bill = f"**{recipient_bill[-4:]}"
        recipient_info = " ".join(recipient)

        # Форматирование суммы и валюты
        amount = f'{row["operationAmount"]["amount"]} {row["operationAmount"]["currency"]["code"]}'

        # Форматирование данных в виде строки
        formatted_data.append(f"""\
{date} {description}
{sender_info} {sender_bill} -> {recipient_info} {recipient_bill}
{amount}
""")
    return formatted_data
