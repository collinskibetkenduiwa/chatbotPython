#chatterbot library,chatterbot-corpus to train
#use chatbot1.0.0

from flask import Flask,render_template,request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorppusTrainer

app=Flask(__name__)

ChatBot("Chatterbot",storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer=ChatterbotCorpusTrainer(english_bot)
trainer.train("chatterbotcorpus.english")


@app.route("/")
def home():
    return render_template('index.html')
@app.route("/get")
def get_bot_response():
    userText=request.args.get('aar')
    return str(english_bot.get_response(UserText))

if __name__== "__main__":
    app.run()