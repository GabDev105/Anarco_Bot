import sys
import time
import amanobot
from amanobot.loop import MessageLoop

TOKEN = '1173665239:AAEmGc8HMTq3J5EmDLN_75g2cfar55co7Ok'

def handle(msg):
    content_type, chat_type, chat_id = amanobot.glance(msg)
    ##print(bot.getUpdates())
    if content_type == 'text': msgtext = msg['text']
    else: msgtext = "Vazio"
    print("=======================================\nTipo de Chat: {}\nNome: {}\nTipo: {}\nMensagem: {}\n=======================================\n".format(msg['chat']['type'], msg['from']['first_name'], content_type, msgtext))

    if msg['text'] == '/start':
        bot.sendMessage(chat_id,"Olá {}, Meu nome é AnarcoBotⒶ.\n"
                                "Meu objetivo é descentralizar a informação dispersa sobre o Libertarianismo.\n"
                                "Estou aqui para ajudá-lo se tiver dúvidas sob o tema!\n"
                                "Tenho muitos comandos úteis e um fluxograma (/QuemFaria) para acabar com as perguntas:\n"
                                "\n"
                                "'¿Mas, sem o estado quem faria as estradas?'\n"
                                "'¿Quem forneceria saúde, educação e segurança?'\n"
                                "\n"
                                "Para inicar meus comandos, clique em /help\n"
                                "Salve galera, tmj🐍.".format(msg['from']['username']))

    if msg['text'] == '/help':
        bot.sendMessage(chat_id,"/Defs: Mostrar lista de comandos de termos libertários e suas respectivas definições.\n"
"/QuemFaria: Iniciar fluxograma sobre a produção de qualquer serviço ou mercadoria.\n"
"/Cryptos: Mostrar comandos com resumos breves de criptomoedas com utilidade para o nosso agorismo do dia a dia.\n"
"/Canais: Mostrar uma quantidade sustancial de canais de viés libertário.\n"
"/Livros: Recomendações de leituras para iniciar no Libertarianismo.\n"
"/About: Mostrar mais informações sobre o processo e apoio no desenvolvimento do bot.\n".format(msg['from']['username']))
    
    if msg['text'].split(' ')[0] == '/echo':
        bot.sendMessage(chat_id, msg[u'text'].split(' ', 1)[1])

bot = amanobot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()

while 1:
    time.sleep(2)
