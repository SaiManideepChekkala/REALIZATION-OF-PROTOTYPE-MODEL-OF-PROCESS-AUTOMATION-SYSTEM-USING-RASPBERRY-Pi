from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from pymodbus.client.sync import ModbusTcpClient
import time

host = '169.254.163.50'  # ip of your raspberry pi
port = 502
client = ModbusTcpClient(host, port)
Builder.load_file('switch.kv')

class MyLayout(Widget):
    def switch_click(self, switchObject, switchValue):
        if switchValue:
            print(switchValue)
            client.connect()
            wr = client.write_registers(1000, switchValue, unit=1)
        else:
            print(switchValue)
            client.connect()
            wr = client.write_registers(1000, switchValue, unit=1)

        if switchValue:
            self.ids.my_Label.text = "LED status: on"
        else:
            self.ids.my_Label.text = "LED status: off"


class AwesomeApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    AwesomeApp().run()
    