from gpiozero import CPUTemperature
import RPi.GPIO as GPIO
import socket
import numpy as np
import encodings
import time


HOST = '169.254.163.50'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
cpu = CPUTemperature()
LED_PIN = 25
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN,GPIO.OUT)

    
def server_data():
    
    temperature, cutoff_temperature = cpu.temperature, 60

    if temperature is not None:
        print("Temperature =",temperature,"C")
        if temperature > cutoff_temperature:
            GPIO.output(LED_PIN,GPIO.HIGH)
        else:
            GPIO.output(LED_PIN,GPIO.LOW)
        data = '{},{}'.format(temperature,cutoff_temperature)
    return data



def my_server():
        
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("Server Started waiting for client to connect ")
        s.bind((HOST, PORT))
        s.listen(5)
        conn, addr = s.accept()

        with conn:
            print('Connected by', addr)
            while True:

                data = conn.recv(1024).decode('utf-8')

                if str(data) == "Data":

                    my_data = server_data()

                    x_encoded_data = my_data.encode('utf-8')

                    conn.sendall(x_encoded_data)

                elif  str(data) == "Quit":
                    print("shutting down server ")
                    break


                if not data:
                    break
                else:
                    pass


if __name__ == '__main__':
    while 1:
        my_server()
