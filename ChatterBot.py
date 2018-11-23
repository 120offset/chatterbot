# -*- coding: utf-8 -*-
from chatterbot import ChatBot
chatbot = ChatBot('Unlucky Overlord')
# Uncomment the following lines to enable verbose logging
import logging
logging.basicConfig(level=logging.INFO)

bot = ChatBot(
    'Unlucky Overlord',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database='./database.sqlite3'
)

bot = ChatBot(
    'Unlucky Overlord',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    database='./database.sqlite3'
)

bot = ChatBot(
    'Unluck Overlord',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    database='./database.sqlite3'
)

while True:
    try:
     bot_input = bot.get_response(None)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break


bot.train([

    'The Wu\' is comin through, the outcome is critical',
    'If what you say is true, the Shaolin and the Wu-Tang could be dangerous',
    'And that\'s one in the chamber, Wu-Tang banger 36 styles of danger',
    'Wu-Tang slang\'ll leave your headpiece hangin\'',
    'Here I go, deep type flow.',
])

