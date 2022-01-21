from requests import get
from decimal import Decimal
import datetime


def currency_rates(c_code):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding=response.encoding)
    c_code = str(c_code).upper()
    if content.find(c_code) >= 0 and c_code.isalpha():
        spl_date = content.split('ValCurs Date="')
        current_date = spl_date[1].split('"', 1)[0].split('.')
        current_date = datetime.date(int(current_date[2]), int(current_date[1]), int(current_date[0]))
        spl_cur = content.split(c_code)
        rate = spl_cur[1].split('<Value>')[1].split('<')[0]
        rate = Decimal(rate.replace(',', '.'))
        result = f'{rate}, {current_date}'
    else:
        result = 'Invalid currency name'
    return result


if __name__ == '__main__':
    print(currency_rates('asd'))
    print(currency_rates(244))
    print(currency_rates('USD'))
    print(currency_rates('aZn'))
    print(currency_rates('123'))
