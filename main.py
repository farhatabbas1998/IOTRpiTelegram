 import datetime  # Importing the datetime library
import telepot   # Importing the telepot library
from telepot.loop import MessageLoop    # Library function to communicate with telegram bot
import RPi.GPIO as GPIO                 # Importing the GPIO library to use the GPIO pins of Raspberry pi
from time import sleep                  # Importing the time library to provide the delays in program

red_led_pin = 21                # Initializing GPIO 21 for red led
yellow_led_pin = 20             # Initializing GPIO 20 for yellow led

GPIO.setmode(GPIO.BCM)               # Use Board pin numbering
GPIO.setup(red_led_pin, GPIO.OUT)    # Declaring the GPIO 21 as output pin
GPIO.setup(yellow_led_pin, GPIO.OUT) # Declaring the GPIO 20 as output pin

now = datetime.datetime.now()       # Getting date and time

def handle(msg):
    chat_id = msg['chat']['id'] # Receiving the message from telegram
    command = msg['text']   # Getting text from the message

    print ('Msg recived:')
    print(command)

    # Comparing the incoming message to send a reply according to it
    if command == '/hi':
        bot.sendMessage (chat_id, str("Hi! Lazy boi"))
    elif command == '/date':
        bot.sendMessage(chat_id, str("Date: ") + str(now.day) + str("/") + str(now.month) + str("/") + str(now.year))
    elif command == '/redon':
        bot.sendMessage(chat_id, str("Red led is ON"))
        GPIO.output(red_led_pin, True)
    elif command == '/redoff':
        bot.sendMessage(chat_id, str("Red led is OFF"))
        GPIO.output(red_led_pin, False)
    elif command == '/yellowon':
        bot.sendMessage(chat_id, str("Yellow led is ON"))
        GPIO.output(yellow_led_pin, True)
    elif command == '/yellowoff':
        bot.sendMessage(chat_id, str("Yellow led is OFF"))
        GPIO.output(yellow_led_pin, False)

# Insert your telegram token below
bot = telepot.Bot('967173198:AAEYRW_OzqqMI-wMHxtVaYadHwHGQeEk7ck')
print (bot.getMe())

# Start listening to the telegram bot and whenever a message is  received, the handle function will be called.
MessageLoop(bot, handle).run_as_thread()
print ('Waiting for command....')
  
 
    
while 1:
    sleep(10)