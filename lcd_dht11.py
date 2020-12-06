import time
import board
import adafruit_dht

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D17)
def getTempHum():
    try:
        # Print the values to the serial port
        temperature_c = "%.1f" % dhtDevice.temperature
        humidity = dhtDevice.humidity
        return str("{} C,{}% "
                .format(temperature_c, humidity))

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        return None
if __name__ == '__main__':
    print(getTempHum())
