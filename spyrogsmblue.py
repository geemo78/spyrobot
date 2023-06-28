import time
from gsmmodem.modem import GsmModem

# Configure your GSM modem serial port and baudrate
PORT = '/dev/serial0'  # Replace with the actual port of your GSM module
BAUDRATE = 9600

# Configure your SIM card details
PIN = None  # Replace with your SIM card PIN if required
PHONE_NUMBER = '<your_phone_number>'

# Callback function for incoming SMS messages
def incoming_sms(message):
    print('Received SMS from {}: {}'.format(message.number, message.text))

# Initialize the GSM modem
modem = GsmModem(PORT, BAUDRATE)

# Optionally, set the PIN if required
if PIN:
    modem.connect(PIN=PIN)
else:
    modem.connect()

# Register the incoming SMS callback function
modem.sms_text_mode = False
modem.sms_received_callback = incoming_sms

# Send an SMS message
message_text = 'Hello, from Raspberry Pi!'
modem.send_sms(PHONE_NUMBER, message_text)

# Wait for incoming SMS messages
while True:
    time.sleep(1)  # You can change the sleep duration if needed

# Disconnect the modem when done
modem.disconnect()