import serial
import os, time
import RPi.GPIO as GPIO

# Configure the serial port
ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)

# Function to send AT commands and get responses
def send_command(command):
    ser.write((command + '\r\n').encode())
    time.sleep(0.5)
    response = ser.read(ser.inWaiting())
    return response.decode()

def check_GSM():
    # Test the GSM module
    ser.flushInput()
    response = send_command('AT')
    print(response)

def send_GSM():
    # Send an SMS
    response = send_command('AT+CMGF=1')  # Set SMS text mode
    print(response)

    response = send_command('AT+CMGS="+639108452053"')  # Replace with the destination phone number
    print(response)

    message = "HELLO butipul do u want do do utang!"  # Replace with your message
    ser.write((message + '\x1A').encode())  # Send the message
    time.sleep(2)
    response = ser.read(ser.inWaiting()).decode()
    print(response)

    ser.close()

def call_GSM():
    phone_number = "+639452073290"
    send_command('ATD{};'.format(phone_number))  # Replace with the destination phone number
    print("Calling...")
    time.sleep(10)

    send_command(b'ATH\r')
    print("Hang call...")

    ser.close()

if __name__ == "__main__":
    call_GSM()
