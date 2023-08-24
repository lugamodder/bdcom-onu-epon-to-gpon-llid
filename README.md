
Скрипт генерирует конфигурацию llid для GPON OLT BDCOM c серийными номерами ONU, которые преобразовывает из MAC-адресов ONU конфигурации EPON OLT BDCOM.
Используется вместе с двухстандартными ONU для перевода с EPON на GPON.

**Использование:** *python3 script_name.py input_file*

**Пример содержимого изначального файла:**
*epon bind-onu mac 9845.62ab.3943 1
epon bind-onu mac d425.cc06.6e9b 2
epon bind-onu mac d425.cc02.e6b9 3
epon bind-onu mac d425.cc07.ef40 4
epon bind-onu mac d425.cc05.1da0 5
epon bind-onu mac d425.cc03.0b37 6
epon bind-onu mac d425.cc0e.5a67 7
epon bind-onu mac d425.cc03.7e21 8
epon bind-onu mac d425.cc06.aacb 9
epon bind-onu mac d425.cc07.2478 10*

**Пример вывода скрипта:**
*gpon bind-onu sn BDCM:62AB3943 1
gpon bind-onu sn xPON:CC066E9B 2
gpon bind-onu sn xPON:CC02E6B9 3
gpon bind-onu sn xPON:CC07EF40 4
gpon bind-onu sn xPON:CC051DA0 5
gpon bind-onu sn xPON:CC030B37 6
gpon bind-onu sn xPON:CC0E5A67 7
gpon bind-onu sn xPON:CC037E21 8
gpon bind-onu sn xPON:CC06AACB 9
gpon bind-onu sn xPON:CC072478 10*
