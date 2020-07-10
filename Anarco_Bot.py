import sys
import time
import amanobot
from amanobot.loop import MessageLoop

TOKEN = 'TOKEN'

def handle(msg):
    content_type, chat_type, chat_id = amanobot.glance(msg)
    ##print(bot.getUpdates())

    if msg['text'] == '/start':
        bot.sendMessage(chat_id,"Olá {}, Meu nome é AncapBotⒶ.\n"
                                "Meu objetivo é descentralizar a informação dispersa sobre o Libertarianismo.\n"
                                "Estou aqui para ajudá-lo se tiver dúvidas sob o tema!\n"
                                "Tenho muitos comandos úteis e um fluxograma (/QuemFaria) para acabar com as perguntas:\n"
                                "\n"
                                "'¿Mas, sem o estado quem faria as estradas?'\n"
                                "'¿Quem forneceria saúde, educação e segurança?'\n"
                                "\n"
                                "Para iniciar meus comandos, clique em /help\n"
                                "Salve galera, tmj🐍.".format(msg['from']['username']))

    if msg['text'] == '/start@Anarco_Bot':
        bot.sendMessage(chat_id,"Olá {}, Meu nome é AncapBotⒶ.\n"
                                "Meu objetivo é descentralizar a informação dispersa sobre o Libertarianismo.\n"
                                "Estou aqui para ajudá-lo se tiver dúvidas sob o tema!\n"
                                "Tenho muitos comandos úteis e um fluxograma (/QuemFaria) para acabar com as perguntas:\n"
                                "\n"
                                "'¿Mas, sem o estado quem faria as estradas?'\n"
                                "'¿Quem forneceria saúde, educação e segurança?'\n"
                                "\n"
                                "Para iniciar meus comandos, clique em /help\n"
                                "Salve galera, tmj🐍.".format(msg['from']['username']))

    if msg['text'] == '/help':
        bot.sendMessage(chat_id,"/Defs: Mostrar lista de comandos de termos libertários e suas respectivas definições.\n"
"/QuemFaria: Iniciar fluxograma sobre a produção de qualquer serviço ou mercadoria.\n"
"/Cryptos: Mostrar comandos com resumos breves de criptomoedas com utilidade para o nosso agorismo do dia a dia.\n"
"/Canais: Mostrar uma quantidade sustancial de canais de viés libertário.\n"
"/Artistas: Mostrar canais de conteúdo musical libertário.\n"
"/Livros: Recomendações de leituras para iniciar no Libertarianismo.\n"
"/Apoiar: Mostrar endereços de crypto para o apoio no desenvolvimento do bot.".format(msg['from']['username']))

    if msg['text'] == '/help@Anarco_Bot':
        bot.sendMessage(chat_id,"/Defs: Mostrar lista de comandos de termos libertários e suas respectivas definições.\n"
"/QuemFaria: Iniciar fluxograma sobre a produção de qualquer serviço ou mercadoria.\n"
"/Cryptos: Mostrar comandos com resumos breves de criptomoedas com utilidade para o nosso agorismo do dia a dia.\n"
"/Canais: Mostrar uma quantidade sustancial de canais de viés libertário.\n"
"/Artistas: Mostrar canais de conteúdo musical libertário.\n"
"/Livros: Recomendações de leituras para iniciar no Libertarianismo.\n"
"/Apoiar: Mostrar endereços de crypto para o apoio no desenvolvimento do bot.".format(msg['from']['username']))
    
    if msg['text'] == '/Defs':
        bot.sendMessage(chat_id,"Termos Libertários:\n"
                                "/Propriedade\n"
                                "/Agressao\n"
                                "/Liberdade\n"
                                "/Jusnaturalismo\n"
                                "/DireitoNegativo\n"
                                "/DireitoPositivo\n"
                                "/Juspositivismo\n"
                                "/HomeSteading\n"
                                "/Justica\n"
                                "/Etica\n"
                                "/Moral\n"
                                "/Comunismo\n"
                                "/Estado\n"
                                "/ContratoSocial\n".format(msg['from']['username']))

    if msg['text'] == '/Defs@Anarco_Bot':
        bot.sendMessage(chat_id,"Termos Libertários:\n"
                                "/Propriedade\n"
                                "/Agressao\n"
                                "/Liberdade\n"
                                "/Jusnaturalismo\n"
                                "/DireitoNegativo\n"
                                "/DireitoPositivo\n"
                                "/Juspositivismo\n"
                                "/HomeSteading\n"
                                "/Justice\n"
                                "/Etica\n"
                                "/Moral\n"
                                "/Comunismo\n"
                                "/Estado\n"
                                "/ContratoSocial\n".format(msg['from']['username']))

    if msg['text'] == '/QuemFaria':
        bot.sendMessage(chat_id,"Ainda em desenvolvimento...".format(msg['from']['username']))
    
    if msg['text'] == '/QuemFaria@Anarco_Bot':
        bot.sendMessage(chat_id,"Ainda em desenvolvimento...".format(msg['from']['username']))

    if msg['text'] == '/Cryptos':
        bot.sendMessage(chat_id,"Indivíduos podem evitar grande parte do roubo estatal por meio\n"
                                "das criptomoedas, meios de troca resultados dos avanços de estudos criptográficos na década de 80.\n"
                                "A privacidade e características monetárias delas protegem a liberdade financeira dos indivíduos.\n"
                                "\n"
                                "Aqui uma lista breve de criptomoedas com características relevantes para a defesa libertária:\n"
                                "/Bitcoin(₿)\n"
                                "/Nano(⋰·⋰)\n"
                                "/Monero(XMR)\n".format(msg['from']['username']))
                            
    if msg['text'] == '/Cryptos@Anarco_Bot':
        bot.sendMessage(chat_id,"Indivíduos podem evitar grande parte do roubo estatal por meio\n"
                                "das criptomoedas, meios de troca resultados dos avanços de estudos criptográficos na década de 80.\n"
                                "A privacidade e características monetárias delas protegem a liberdade financeira dos indivíduos.\n"
                                "\n"
                                "Aqui uma lista breve de criptomoedas com características relevantes para a defesa libertária:\n"
                                "/Bitcoin(₿)\n"
                                "/Nano(⋰·⋰)\n"
                                "/Monero(XMR)\n".format(msg['from']['username']))
                                




    if msg['text'].split(' ')[0] == '/echo':
        bot.sendMessage(chat_id, msg[u'text'].split(' ', 1)[1])

bot = amanobot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()

while 1:
    time.sleep(2)





    if msg['text'].split(' ')[0] == '/echo':
        bot.sendMessage(chat_id, msg[u'text'].split(' ', 1)[1])

bot = amanobot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()

while 1:
    time.sleep(2)
