from chatterbot import ChatBot

chatbot = ChatBot("Ron Obvius", read_only=True)

# training the chatbot
from chatterbot.trainers import ListTrainer

conversation = [
	'Hello',
	'hi there!',
	'How are you doing?',
	'I am doing great.',
	'That is good to hear',
	'Thank you',
	'You\'re welcome.'
]

chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)

response = chatbot.get_response("Good morning!")

print(response)
""" Read only mode """

