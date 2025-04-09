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

# Function to control a specific channel
def turn_on_relay(channel):
    if 1 <= channel <= 8:
        relay.write_bit(channel - 1, 1, functioncode=5)  # Turn ON specified channel
        print(f"Relay {channel} is ON")
    else:
        print("Invalid channel. Choose between 1 and 8.")

def turn_off_relay(channel):
    if 1 <= channel <= 8:
        relay.write_bit(channel - 1, 0, functioncode=5)  # Turn OFF specified channel
        print(f"Relay {channel} is OFF")
    else:
        print("Invalid channel. Choose between 1 and 8.")

# Function to turn all relays ON
def turn_on_all_relays():
    for channel in range(8):
        relay.write_bit(channel, 1, functioncode=5)
    print("All relays are ON")

# Function to turn all relays OFF
def turn_off_all_relays():
    for channel in range(8):
        relay.write_bit(channel, 0, functioncode=5)
    print("All relays are OFF")

# Test the relay control
if __name__ == "__main__":
    turn_on_all_relays()
    time.sleep(5)  # Keep all relays ON for 5 seconds
    turn_off_all_relays()
