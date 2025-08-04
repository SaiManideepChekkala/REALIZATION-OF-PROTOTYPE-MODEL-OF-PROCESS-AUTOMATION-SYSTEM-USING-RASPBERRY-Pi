import socket
import threading
import time
HOST = '169.254.163.50'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

def process_data_from_server(x):
    x1, y1 = x.split(",")
    return x1, y1
def my_client():
    threading.Timer(11, my_client).start()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        my = "Data"
        my_inp = my.encode('utf-8')
        s.sendall(my_inp)
        data = s.recv(1024).decode('utf-8')

        x_temperature, y_cutoff = process_data_from_server(data)
        temperature = float(x_temperature)
        cutoff_temperature = float(y_cutoff)

        if temperature > cutoff_temperature:
            print("Temperature {} C".format(x_temperature),"LED ON")
            print("cutoff_temperature",cutoff_temperature)
        else:
            print("Temperature {} C".format(x_temperature),"LED OFF")
            print("cutoff_temperature", cutoff_temperature)

        s.close()
        time.sleep(1)

if __name__ == "__main__":
    while 1:
        my_client()
