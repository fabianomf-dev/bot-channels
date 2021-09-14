from flask import Flask, request, jsonify
import telebot
import json
from telebot import types
from telebot import util
from time import sleep
from datetime import datetime, timedelta
from mongodb import insert_user,insert_channels_groups

TOKEN = '1987688072:AAH56T9QnHGuD0kEzVoy_o2lSp93AXcihj8'
bot = telebot.TeleBot(TOKEN)
bot.set_webhook(url="https://bot-channels.herokuapp.com",allowed_updates=util.update_types)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def command_start(message: types.ChatMemberUpdated):
    id = message.chat.id
    bot.send_message(id, f"\U00002935 estou online")


@app.route('/', methods=["POST", "GET"])
def webhook():
    
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "ok"

@bot.my_chat_member_handler()
def my_chat_m(message: types.ChatMemberUpdated):
    id_canal_grupo = message.chat.id
    try:
        old = message.old_chat_member
        new = message.new_chat_member
    except Exception as e:
        print(e)    
    if new.status == "member":
        bot.send_message(message.chat.id,"bot adicionado") # Welcome message, if bot was added to group
        bot.leave_chat(message.chat.id)
## verificar quando user é adicionado        
@bot.chat_member_handler()
def chat_m(message: types.ChatMemberUpdated):
    old = message.old_chat_member
    new = message.new_chat_member
    if new.status == "member":
        insert_channels_groups(message.chat.id,message.chat.type,message.chat.title)
        insert_user(new.user.first_name,new.user.id)
        bot.send_message(message.chat.id,"Olá {name}!".format(name=new.user.first_name))
        sleep(30)
        bot.ban_chat_member(message.chat.id,new.user.id,datetime.now())
        bot.send_message(message.chat.id,f"{new.user.first_name}, removido")
    else:
         pass
    
    
if __name__ == "__main__":
    app.run()
