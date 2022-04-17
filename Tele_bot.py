import telebot;

TOKEN_API = 'YOUR TOKEN'

bot = telebot.TeleBot(TOKEN_API);

def Verificar(mensagem):
    return True;

@bot.message_handler(func=Verificar)
def resposta(mensagem):

    bot.send_message(mensagem.chat.id,mensagem.text)

bot.polling();