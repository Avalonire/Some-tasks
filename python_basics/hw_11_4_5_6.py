class StorageError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    """Общий склад
       Учёт ведется по серийным номерам техники
       Для каждой группы техники свои складские номера"""

    storage = {'printers': {}, 'scanners': {}, 'mfp': {}}

    @classmethod
    def stock(cls, item):
        try:
            cls.param_validator(item)
            if cls.sn_validator(item):
                raise StorageError(f'SN"{item.serial_number}" equipment is already in stock!')
        except StorageError as error:
            print('-' * 50 + '\nERROR:', error)
            exit(1)
        if item.__class__ is Printer:
            if Warehouse.storage['printers']:
                idx = max(Warehouse.storage['printers'])
                Warehouse.storage['printers'].update([(idx + 1, item.__dict__)])
            else:
                Warehouse.storage['printers'].update([(1, item.__dict__)])
            print(
                f'Printer {item.brand} {item.serial_number} added to stock on {max(Warehouse.storage["printers"])} slot'
                f'\n{"-" * 100}')
        elif item.__class__ is Scanner:
            if Warehouse.storage['scanners']:
                idx = max(Warehouse.storage['scanners'])
                Warehouse.storage['scanners'].update([(idx + 1, item.__dict__)])
            else:
                Warehouse.storage['scanners'].update([(1, item.__dict__)])
            print(
                f'Scanner {item.brand} {item.serial_number} added to stock on {max(Warehouse.storage["scanners"])} slot'
                f'\n{"-" * 100}')
        elif item.__class__ is Mfp:
            if Warehouse.storage['mfp']:
                idx = max(Warehouse.storage['mfp'])
                Warehouse.storage['mfp'].update([(idx + 1, item.__dict__)])
            else:
                Warehouse.storage['mfp'].update([(1, item.__dict__)])
            print(
                f'Mfp {item.brand} {item.serial_number} added to stock on {max(Warehouse.storage["mfp"])} slot'
                f'\n{"-" * 100}')

    @classmethod
    def destock(cls, item):
        try:
            cls.param_validator(item)
            if not cls.sn_validator(item):
                raise StorageError(f'Equipment {item.brand}, SN"{item.serial_number}" is not in stock!')
        except StorageError as error:
            print('-' * 50 + '\nERROR:', error)
            exit(2)
        for equip, stock in Warehouse.storage.items():
            for key, val in stock.items():
                if item.serial_number in val.values():
                    stock[key] = {}
                    print(
                        f'Equipment {item.brand}, id: {key}, SN"{item.serial_number}" destocked\n'
                        f'slot {key} for "{equip}" is empty\n{"-" * 100}')

    @staticmethod
    def param_validator(param):
        """Проверка числовых параметров офисной техники"""

        if param.__class__ is Printer:
            if type(param.page_resource) is not int:
                raise StorageError('Page resource for printers must be integer!')
        if param.__class__ is Scanner:
            if type(param.scan_speed) is not int:
                raise StorageError('Scan speed for scanners must be integer!')
        if param.__class__ is Mfp:
            if type(param.page_capacity) is not int:
                raise StorageError('Mfp page capacity must be integer!')

    @staticmethod
    def sn_validator(item):
        """Проверка наличия на складе"""

        for equip in Warehouse.storage.values():
            for val in equip.values():
                if item.serial_number in val.values():
                    return True


class Equipment:
    """Офисная техника"""

    def __init__(self, brand, model, serial_number):
        self.brand = brand
        self.model = model
        self.serial_number = serial_number


class Printer(Equipment):
    def __init__(self, brand, model, serial_number, page_resource, color=True):
        super().__init__(brand, model, serial_number)
        self.page_resource = page_resource
        self.color = color


class Scanner(Equipment):
    def __init__(self, brand, model, serial_number, scan_speed, resolution):
        super().__init__(brand, model, serial_number)
        self.scan_speed = scan_speed
        self.resolution = resolution


class Mfp(Equipment):
    def __init__(self, brand, model, serial_number, page_capacity, can_scan=True):
        super().__init__(brand, model, serial_number)
        self.can_scan = can_scan
        self.page_capacity = page_capacity


printer_1 = Printer('HP', 'LaserJet', '2940FGS01', 5000, True)
printer_2 = Printer('Brother', 'Micro', '223ITY38', 2000, False)
mfp_1 = Mfp('Canon', '307F', '12031032K8SDL', 100, False)
mfp_2 = Mfp('HP', 'MF9867', 'KKL3444', 500, True)
scanner_1 = Scanner('Epson', 'Light360', 'I4356O', 1, '1980x1650')

# проверка добавления оборудования на склад
Warehouse.stock(printer_1)
Warehouse.stock(printer_2)
Warehouse.stock(mfp_1)
Warehouse.stock(mfp_2)
Warehouse.stock(scanner_1)

# проверка удаления оборудования со склада
# индексы убранных со склада приборов не удаляются, так как они являются имитацией складских полок
Warehouse.destock(printer_2)
Warehouse.destock(mfp_2)

# проверка валидации добавления уже существующего оборудования на складе
Warehouse.stock(printer_1)
