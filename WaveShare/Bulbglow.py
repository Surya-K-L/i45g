import minimalmodbus
import time

# Define serial communication parameters
SERIAL_PORT = '/dev/ttyAMA3'  # Update based on your device
BAUD_RATE = 9600
SLAVE_ADDRESS = 1  # Confirm with device

# Create Modbus RTU instrument
relay = minimalmodbus.Instrument(SERIAL_PORT, SLAVE_ADDRESS)
relay.serial.baudrate = BAUD_RATE
relay.serial.bytesize = 8
relay.serial.parity = minimalmodbus.serial.PARITY_NONE
relay.serial.stopbits = 1
relay.serial.timeout = 1

# Function to control Channel 7 relay
def turn_on_relay():
    relay.write_bit(6, 1, functioncode=5)  # Turn ON Channel 7
    print("Bulb is ON")

def turn_off_relay():
    relay.write_bit(6, 0, functioncode=5)  # Turn OFF Channel 7
    print("Bulb is OFF")

# Test the relay control
if _name_ == "_main_":
    turn_on_relay()
    time.sleep(5)  # Keep the bulb ON for 8 seconds
    turn_off_relay()



#Output Comments: The bulb will be on when we run the program and it will have a delay time of five seconds and after that it will be off.
