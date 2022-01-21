import sys
from hw_4_2345 import currency_rates

if len(sys.argv) > 1:
    print(currency_rates(sys.argv[1]))
else:
    print(f"Request 123: {currency_rates('123')}")
    print(f"Request uSD: {currency_rates('uSD')}")
    print(f"Request EUR: {currency_rates('EUR')}")
    print(f"Request 000: {currency_rates(000)}")
    print(f"Request azn: {currency_rates('azn')}")
