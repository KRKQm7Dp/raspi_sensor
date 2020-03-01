import time
import board
import adafruit_dht

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D18)
def getTempHum():
    try:
        # Print the values to the serial port
        temperature_c = "%.1f" % dhtDevice.temperature
        humidity = dhtDevice.humidity
        print("{} C,{}% "
                .format(temperature_c, humidity))
        return (temperature_c, humidity)

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        return None
