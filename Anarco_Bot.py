import sys
import time
import amanobot
from amanobot.loop import MessageLoop

TOKEN = 'TOKEN'

def handle(msg):
    content_type, chat_type, chat_id = amanobot.glance(msg)
    ##print(bot.getUpdates())

#startPriv
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
#startGrupo
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
#helpPriv
    if msg['text'] == '/help':
        bot.sendMessage(chat_id,"/Defs: Mostrar lista de comandos de termos libertários e suas respectivas definições.\n"
"/QuemFaria: Iniciar fluxograma sobre a produção de qualquer serviço ou mercadoria.\n"
"/Cryptos: Mostrar comandos com resumos breves de criptomoedas com utilidade para o nosso agorismo do dia a dia.\n"
"/Canais: Mostrar uma quantidade sustancial de canais de viés libertário.\n"
"/Artistas: Mostrar canais de conteúdo musical libertário.\n"
"/Livros: Recomendações de leituras para iniciar no Libertarianismo.\n"
"/Apoiar: Mostrar endereços de crypto para o apoio no desenvolvimento do bot.".format(msg['from']['username']))
#helpGrupo
    if msg['text'] == '/help@Anarco_Bot':
        bot.sendMessage(chat_id,"/Defs: Mostrar lista de comandos de termos libertários e suas respectivas definições.\n"
"/QuemFaria: Iniciar fluxograma sobre a produção de qualquer serviço ou mercadoria.\n"
"/Cryptos: Mostrar comandos com resumos breves de criptomoedas com utilidade para o nosso agorismo do dia a dia.\n"
"/Canais: Mostrar uma quantidade sustancial de canais de viés libertário.\n"
"/Artistas: Mostrar canais de conteúdo musical libertário.\n"
"/Livros: Recomendações de leituras para iniciar no Libertarianismo.\n"
"/Apoiar: Mostrar endereços de crypto para o apoio no desenvolvimento do bot.".format(msg['from']['username']))
#DefsPriv
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
#DefsGrupo
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
#QuemFariaPriv
    if msg['text'] == '/QuemFaria':
        bot.sendMessage(chat_id,"Ainda em desenvolvimento...".format(msg['from']['username']))
#QuemFariaGrupo
    if msg['text'] == '/QuemFaria@Anarco_Bot':
        bot.sendMessage(chat_id,"Ainda em desenvolvimento...".format(msg['from']['username']))
#CryptosPriv
    if msg['text'] == '/Cryptos':
        bot.sendMessage(chat_id,"Indivíduos podem evitar grande parte do roubo estatal por meio\n"
                                "das criptomoedas, meios de troca resultados dos avanços de estudos criptográficos na década de 80.\n"
                                "A privacidade e características monetárias delas protegem a liberdade financeira dos indivíduos.\n"
                                "\n"
                                "Aqui uma lista breve de criptomoedas com características relevantes para a defesa libertária:\n"
                                "/Bitcoin(₿)\n"
                                "/Nano(⋰·⋰)\n"
                                "/Monero(XMR)\n".format(msg['from']['username']))
#CryptosGrupo                     
    if msg['text'] == '/Cryptos@Anarco_Bot':
        bot.sendMessage(chat_id,"Indivíduos podem evitar grande parte do roubo estatal por meio\n"
                                "das criptomoedas, meios de troca resultados dos avanços de estudos criptográficos na década de 80.\n"
                                "A privacidade e características monetárias delas protegem a liberdade financeira dos indivíduos.\n"
                                "\n"
                                "Aqui uma lista breve de criptomoedas com características relevantes para a defesa libertária:\n"
                                "/Bitcoin(₿)\n"
                                "/Nano(⋰·⋰)\n"
                                "/Monero(XMR)\n".format(msg['from']['username']))
#CanaisPriv
    if msg['text'] == '/Canais':
        bot.sendMessage(chat_id,"Aqui uma lista de canais com conteúdo libertário:\n"
                                "/PortalLibertarianismo\n"
                                "/AncapSu\n"
                                "/UniversidadeLibertaria\n"
                                "/CafeLibertario\n"
                                "/AlexandrePorto\n"
                                "/FelipeOjeda\n"
                                "/OdinilsonBom\n"
                                "/Fhoer\n"
                                "/OPessimista\n"
                                "/MidiaAncap\n"
                                "/JoaoMazetto\n".format(msg['from']['username']))
#CanaisGrupo
    if msg['text'] == '/Canais@Anarco_Bot':
        bot.sendMessage(chat_id,"Aqui uma lista de canais com conteúdo libertário:\n"
                                "/PortalLibertarianismo\n"
                                "/AncapSu\n"
                                "/UniversidadeLibertaria\n"
                                "/CafeLibertario\n"
                                "/AlexandrePorto\n"
                                "/FelipeOjeda\n"
                                "/OdinilsonBom\n"
                                "/Fhoer\n"
                                "/OPessimista\n"
                                "/MidiaAncap\n"
                                "/JoaoMazetto\n".format(msg['from']['username']))
#canaisPriv
    if msg['text'] == '/PortalLibertarianismo':
        bot.sendMessage(chat_id,"https://www.youtube.com/channel/UC5ciZV6sllUFR0J7QQInnaA".format(msg['from']['username']))
    if msg['text'] == '/AncapSu':
        bot.sendMessage(chat_id,"https://www.youtube.com/channel/UCSyG9ph5BJSmPRyzc_eGC4g".format(msg['from']['username']))
    if msg['text'] == '/UniversidadeLibertaria':
        bot.sendMessage(chat_id,"https://www.youtube.com/channel/UCD65KdRPT7v065JR62rR_qQ".format(msg['from']['username']))
    if msg['text'] == '/CafeLibertario':
        bot.sendMessage(chat_id,"https://www.youtube.com/channel/UCmhpqvtjSv3dYqBM-IfVxgw".format(msg['from']['username']))
    if msg['text'] == '/AlexandrePorto':
        bot.sendMessage(chat_id,"https://www.youtube.com/user/CanalTal".format(msg['from']['username']))
    if msg['text'] == '/FelipeOjeda':
        bot.sendMessage(chat_id,"https://www.youtube.com/user/felipebocaoojeda".format(msg['from']['username']))
    if msg['text'] == '/OdinilsonBom':
        bot.sendMessage(chat_id,"https://www.youtube.com/user/Odinilsonbom".format(msg['from']['username']))
    if msg['text'] == '/Fhoer':
        bot.sendMessage(chat_id,"https://www.youtube.com/channel/UCcgAa7wJ1OwRzd-TGFwIxPA".format(msg['from']['username']))
    if msg['text'] == '/OPessimista':
        bot.sendMessage(chat_id,"https://www.youtube.com/channel/UC4z5OsOcltedh3iZKYJ2UcA".format(msg['from']['username']))
    if msg['text'] == '/MidiaAncap':
        bot.sendMessage(chat_id,"https://www.youtube.com/channel/UCsFgHFNWP-1I9mCoA59TixA".format(msg['from']['username']))
    if msg['text'] == '/JoaoMazetto':
        bot.sendMessage(chat_id,"https://www.youtube.com/channel/UCZ_YyCaw1ajwZ2BlqDALbvA".format(msg['from']['username']))
    if msg['text'] == '/DanielFraga':
        bot.sendMessage(chat_id,"https://www.youtube.com/user/DanielFragaBR".format(msg['from']['username']))
#CanaisGrupo
    if msg['text'] == '/PortalLibertarianismo@Anarco_Bot':
        bot.sendMessage(chat_id,"https://www.youtube.com/channel/UC5ciZV6sllUFR0J7QQInnaA".format(msg['from']['username']))
    if msg['text'] == '/AncapSu@Anarco_Bot':
        bot.sendMessage(chat_id,"https://www.youtube.com/channel/UCSyG9ph5BJSmPRyzc_eGC4g".format(msg['from']['username']))
    if msg['text'] == '/UniversidadeLibertaria@Anarco_Bot':
        bot.sendMessage(chat_id,"https://www.youtube.com/channel/UCD65KdRPT7v065JR62rR_qQ".format(msg['from']['username']))
    if msg['text'] == '/CafeLibertario@Anarco_Bot':
        bot.sendMessage(chat_id,"https://www.youtube.com/channel/UCmhpqvtjSv3dYqBM-IfVxgw".format(msg['from']['username']))
    if msg['text'] == '/AlexandrePorto@Anarco_Bot':
        bot.sendMessage(chat_id,"https://www.youtube.com/user/CanalTal".format(msg['from']['username']))
    if msg['text'] == '/FelipeOjeda@Anarco_Bot':
        bot.sendMessage(chat_id,"https://www.youtube.com/user/felipebocaoojeda".format(msg['from']['username']))
    if msg['text'] == '/OdinilsonBom@Anarco_Bot':
        bot.sendMessage(chat_id,"https://www.youtube.com/user/Odinilsonbom".format(msg['from']['username']))
    if msg['text'] == '/Fhoer@Anarco_Bot':
        bot.sendMessage(chat_id,"https://www.youtube.com/channel/UCcgAa7wJ1OwRzd-TGFwIxPA".format(msg['from']['username']))
    if msg['text'] == '/OPessimista@Anarco_Bot':
        bot.sendMessage(chat_id,"https://www.youtube.com/channel/UC4z5OsOcltedh3iZKYJ2UcA".format(msg['from']['username']))
    if msg['text'] == '/MidiaAncap@Anarco_Bot':
        bot.sendMessage(chat_id,"https://www.youtube.com/channel/UCsFgHFNWP-1I9mCoA59TixA".format(msg['from']['username']))
    if msg['text'] == '/JoaoMazetto@Anarco_Bot':
        bot.sendMessage(chat_id,"https://www.youtube.com/channel/UCZ_YyCaw1ajwZ2BlqDALbvA".format(msg['from']['username']))
    if msg['text'] == '/DanielFraga@Anarco_Bot':
        bot.sendMessage(chat_id,"https://www.youtube.com/user/DanielFragaBR".format(msg['from']['username']))
                                




    if msg['text'].split(' ')[0] == '/echo':
        bot.sendMessage(chat_id, msg[u'text'].split(' ', 1)[1])

bot = amanobot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()

while 1:
    time.sleep(2)
