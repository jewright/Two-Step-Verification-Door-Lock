# from subprocess import check_output
# from time import sleep
# from datetime import datetime
# from RPLCD.i2c import CharLCD
#
# lcd = CharLCD('PCF8574', 0x27, auto_linebreaks=False)
# lcd.clear()
#
#
# def get_ip():
#     cmd = "hostname -I | cut -d\' \' -f1"
#     return check_output(cmd, shell=True).decode("utf-8").strip()
#
#
# while True:
#     lcd_line_1 = datetime.now().strftime('%b %d  %H:%M:%S')
#     lcd_line_2 = "IP " + get_ip()
#
#     lcd.home()
#     lcd.write_string(f'{lcd_line_1}\r\n{lcd_line_2}')
#     sleep(10)


from subprocess import check_output
from RPLCD.i2c import CharLCD
from time import sleep

lcd = CharLCD('PCF8574', 0x27, auto_linebreaks=False)
lcd.clear()

while True:
    lcd_line_1 = "hi"
    lcd_line_2 = "bye"

    lcd.home()
    lcd.write_string(lcd_line_1)
    sleep(10)
    lcd.write_string(f'{lcd_line_1}\r\n{lcd_line_2}')
