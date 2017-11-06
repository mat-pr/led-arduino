import telepot
import time
from nanpy import ArduinoApi, SerialManager
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton


connection = SerialManager(device='COM3') #or the port you are yousing
a = ArduinoApi(connection=connection)
a.pinMode(12, a.OUTPUT)
a.pinMode(11, a.OUTPUT)
a.pinMode(10, a.OUTPUT)
a.pinMode(9, a.OUTPUT)

def on_chat_message(msg): #create a customized keyboard
    content_type, chat_type, chat_id = telepot.glance(msg)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Blue", callback_data='/blue'), InlineKeyboardButton(text="Red", callback_data='/red')],
                                     [InlineKeyboardButton(text="Green", callback_data='/green'), InlineKeyboardButton(text="Yellow", callback_data='/yellow')]])

    bot.sendMessage(chat_id, 'Press a button to change the status of the corresponding LED', reply_markup=keyboard)
            

def on_callback_query(msg): #change the status of the LEDs
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)
    
    if query_data == '/blue':
         if a.digitalRead(12)==0:
                a.digitalWrite(12, 1)
                bot.answerCallbackQuery(query_id, text='Blue on')
         else:
                    a.digitalWrite(12, 0)
                    bot.answerCallbackQuery(query_id, text='Blue off')
    elif query_data == '/red':
         if a.digitalRead(11)==0:
                a.digitalWrite(11, 1)
                bot.answerCallbackQuery(query_id, text='Red on')
         else:
                    a.digitalWrite(11, 0)
                    bot.answerCallbackQuery(query_id, text='Red off')
                
    elif query_data == '/green':
            if a.digitalRead(10)==0:
                a.digitalWrite(10, 1)
                bot.answerCallbackQuery(query_id, text='Green on')
            else:
                a.digitalWrite(10, 0)
                bot.answerCallbackQuery(query_id, text='Green off')
                
    elif query_data == '/yellow':
            if a.digitalRead(9)==0:
                a.digitalWrite(9, 1)
                bot.answerCallbackQuery(query_id, text='Yellow on')
            else:
                a.digitalWrite(9, 0)
                bot.answerCallbackQuery(query_id, text='Yellow off')


bot=telepot.Bot('*Insert your own TOKEN here*')
bot.message_loop({'chat': on_chat_message,
                  'callback_query': on_callback_query})
print ('Listening ...')

while 1:
    time.sleep(10)

