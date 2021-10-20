from django.shortcuts import HttpResponse
import telebot
from django.views.decorators.csrf import csrf_exempt
from telebot import *
from .models import *
from googlesearch import search




bot = TeleBot("1985195461:AAFSX-rnFK8zJAf-aqfqcOdZFaZ_Qu7t_QY")


@csrf_exempt
def index(request):
    if request.method == 'GET':
        return HttpResponse("<a href='http://t.me/dkarimoff96'>Created by</>")
    if request.method == 'POST':
        bot.process_new_updates([
            telebot.types.Update.de_json(
                request.body.decode("utf-8")
            )
        ])
        return HttpResponse(status=200)

@bot.message_handler(commands="start")
def start(a):
    bot.send_message(a.from_user.id, "Welcome " + str(a.from_user.first_name))


@bot.message_handler(func=lambda l: True)
def google_search(l):
    searches = search(l.text, num_results=10)
    for i in searches:
        bot.send_message(l.from_user.id, "Your results are:\n " + i)












