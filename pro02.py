# -*- coding: utf-8 -*-

import os
from chatterbot import ChatBot


# cleaning the console

# Creating a new instance of the ChatBot
# Setting the storage adapter
# if not defualt is sqlite3
# Input and output adapters
# Specifying logic adapters

bot = ChatBot(
	'Angela',
	storage_adapter='chatterbot.storage.SQLStorageAdapter',
	input_adapter  ='chatterbot.input.TerminalAdapter',
	output_adapter ='chatterbot.output.TerminalAdapter',
	logic_adapters = [
		'chatterbot.logic.MathematicalEvaluation',
		'chatterbot.logic.TimeLogicAdapter',
		'chatterbot.logic.BestMatch',
	],
	database       = './database.sqlite3'
)


print("Type something to begin...")

# The following loop will execute each time the enters input
while True:
	try:
		# We pass None to this method because the parameter
		# is not used the terminalAdapter
		bot_input = bot.get_response(None)
	# Press ctrl-c or ctrl-d on the keyboard to exit
	except (KeyboardInterrupt, EOFError, SystemExit):
		break

