# Импортируем все нужные библиотеки, Decimal не обязательно
from requests import get
from decimal import Decimal
import datetime


def currency_rates(c_code):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    # достаем информацию с API (это уже готовый кусок сайта, без гиперссылок и переходов, дан исходно)
    # контент, который возвращает метод GET не читаемый (попробуйте сделать тут print(response)), так как он в XML кодировке

    content = response.content.decode(encoding=response.encoding)
    # надо его РАСПАКОВАТЬ (декодировать) методом *запрос get*.content.decode(encoding=*метод декодирования*)
    # метод декодирования в библиотеке requests есть по умолчанию: *запрос get*.encoding
    # в методичке указано несколько других декодировок, но тут нам нужна сама простая и общая
    # попробуйте в этом месте print(content), что бы понять, с чем мы работаем
    # (это будет строка с ключевыми словами и значениями)
    # дальше идет сама функция:
    # нам просто нужно достать по имени валюты (AUD, EUR, ...) ее значение из длинной строки

    c_code = str(c_code).upper()                            # приводим аргумент функции к нужному виду
    if content.find(c_code) >= 0 and c_code.isalpha():      # если аргумент существует в нашем контенте и передан не цифрами
        spl_date = content.split('ValCurs Date="')          # это задача со звездочкой, где надо вынуть дату, но суть такая же
        current_date = spl_date[1].split('"', 1)[0].split('.')
        current_date = datetime.date(int(current_date[2]), int(current_date[1]), int(current_date[0]))
        spl_cur = content.split(c_code)                     # делим нашу строку по имени валюты, получится список, где 1 - будет строка, начинающася с нужной нам валюты
        rate = spl_cur[1].split('<Value>')[1].split('<')[0] # вынимаем оттуда цену, так же поделив строку по ключевым словам перед ценой
        rate = Decimal(rate.replace(',', '.'))              # приводим цену к Decimal или float, тут разницы нет
        result = f'{rate}, {current_date}'                  # здесь я еще дату добавил от сервера
    else:
        result = 'Invalid currency name'                    # выдача при не правильном вводе аргумента
    return result


if __name__ == '__main__':                                  # это для того, что бы проверять данный файл (модуль) запуская его, а не импортируя
    print(currency_rates('asd'))
    print(currency_rates(244))
    print(currency_rates('USD'))
    print(currency_rates('aZn'))
    print(currency_rates('123'))
