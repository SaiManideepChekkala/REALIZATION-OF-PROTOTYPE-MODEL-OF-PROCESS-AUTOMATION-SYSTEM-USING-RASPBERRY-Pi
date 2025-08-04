from pymodbus.client.sync import ModbusTcpClient
import RPi.GPIO as GPIO
import time

host = '169.254.163.50'
port = 502

client = ModbusTcpClient(host, port)
client.connect()
LED_PIN = 25
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN,GPIO.OUT)

while 1:
    rr = client.read_holding_registers(0x3E8,1,unit=1)
    if (rr.registers[0]):
        GPIO.output(LED_PIN, GPIO.HIGH)
    elif ((rr.registers[0])==0):
        GPIO.output(LED_PIN, GPIO.LOW)
    else:
        GPIO.cleanup()