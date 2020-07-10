#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Bot para responder certas questões sobre Libertarianismo.

Primeiro, algumas funções do manipulador são definidas. Em seguida, essas funções são passadas para
expedidor e registrado em seus respectivos locais.
Em seguida, o bot é iniciado e executado até pressionar Ctrl-C na linha de comando.

Uso:
Responde comandos já estabelecidos.
Pressione Ctrl-C na linha de comando ou envie um sinal ao processo para interromper o
robô.
"""

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text("Olá! Meu nome é AnarcoBotⒶ.\n"
    "Meu objetivo é descentralizar a informação dispersa sobre o Libertarianismo.\n" 
    "Estou aqui para ajudá-lo se tiver dúvidas sob o tema!\n"
    "Tenho muitos comandos úteis e um fluxograma para acabar com as perguntas:\n"
    "\n" 
    "'¿Mas, sem o estado quem faria as estradas?'\n"
    "'¿Quem forneceria saúde, educação e segurança?'\n"
    "\n"
    "Para inicar meus comandos, clique em /help\n"
    "Salve galera, tmj🐍.")


def help_command(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text("/Defs: Mostrar lista de comandos de termos libertários e suas respectivas definições.\n"
"/QuemFaria: Iniciar fluxograma sobre a produção de qualquer serviço ou mercadoria.\n"
"/Cryptos: Mostrar comandos com resumos breves de criptomoedas com utilidade para o nosso agorismo do dia a dia.\n"
"/Canais: Mostrar uma quantidade sustancial de canais de viés libertário.\n"
"/Livros: Recomendações de leituras para iniciar no Libertarianismo.\n"
"/About: Mostrar mais informações sobre o processo e apoio no desenvolvimento do bot.\n")





def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1173665239:AAEmGc8HMTq3J5EmDLN_75g2cfar55co7Ok", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))


    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
