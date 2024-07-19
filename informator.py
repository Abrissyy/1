
import telepot
import socket  # Import socket library to get hostname

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Got command: %s' % command)

    if command == '/bots':  # New command to respond with hostname
        hostname = socket.gethostname()
        bot.sendMessage(chat_id, 'Bot username: %s' % hostname)
    else:
        bot.sendMessage(chat_id, 'unknown command' % command)

TOKEN = '7305306422:AAEpaGGqL8rQSAm8kzjUafsySJdT44i12YM'
bot = telepot.Bot(TOKEN)
bot.message_loop(handle)

print('Listening...')
while True:
    pass
