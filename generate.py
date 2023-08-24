import sys

def generate_serial_number(mac_address, port_number):
    # Разделяем MAC-адрес на байты и убираем точки и двоеточия
    mac_parts = mac_address.replace('.', '').replace(':', '')

    # Определяем часть производителя (BDCM, FGXP, HWTC)
    manufacturers = {
        "0055": "BDCM",
        "8007": "FGXP",
        "e0e8": "HWTC",
        "70a5": "HWTC",
        "1cef": "FGXP",
        "bc60": "BDCM",
        "38f7": "FGXP",
        "70b6": "FGXP",
        "d425": "xPON",
        "a094": "HWTC",
        "e067": "PICO",
        "9845": "BDCM",
        "845b": "HWTC",
        "384c": "HWTC"

    }

    manufacturer = manufacturers.get(mac_parts[:4], "Unknown Manufacturer")

    # Получаем последние 8 символов и приводим их к верхнему регистру
    serial_part = mac_parts[-8:].upper()

    # Для производителя FGXP заменяем 7 и 8 символ с конца на "00"
    if manufacturer == "FGXP":
        serial_part = serial_part[:-8] + "00" + serial_part[-6:]

        # Преобразуем последние 6 символов в шестнадцатеричное число, увеличиваем на 1 и форматируем обратно
        serial_part_int = int(serial_part[-6:], 16)
        serial_part_int += 1
        serial_part = serial_part[:-6] + format(serial_part_int, '06X')

    # Собираем серийный номер
    serial_number = f"{manufacturer}:{serial_part}"

    # Добавляем номер порта
    serial_number_with_port = f"{serial_number} {port_number}"
    return serial_number_with_port

# Чтение мас-адресов и номеров портов из файла
def read_mac_addresses_from_file(file_path):
    mac_entries = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 5 and parts[0] == 'epon' and parts[1] == 'bind-onu' and parts[2] == 'mac' and not parts[3].startswith('0000'):
                mac_entries.append((parts[3], int(parts[4])))
    return mac_entries

def main(file_path):
    examples = read_mac_addresses_from_file(file_path)

    for index, (mac_address, port_number) in enumerate(examples, start=1):
        generated_serial = generate_serial_number(mac_address, port_number)
        print(f"gpon bind-onu sn {generated_serial} {port_number}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py input_file")
        sys.exit(1)

    input_file = sys.argv[1]
    main(input_file)
