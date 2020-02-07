# -*- coding: utf-8 -*-
import os

from pymongo import MongoClient
from pyrogram import Client
from apscheduler.schedulers.background import BackgroundScheduler

from bot.bot import Bot

from dotenv import load_dotenv
load_dotenv()


# constants
# ---------
SESSION_NAME = os.getenv("SESSION_NAME")
BOT_ID = os.getenv("BOT_ID")
BOT_HASH = os.getenv("BOT_HASH")
MONGO_URI = os.getenv("MONGO_URI")
BOT_NAME = "uborzz_bot"
DB_NAME = "calls_db"


# init
# ----
print("Creating the scheduler...")
scheduler = BackgroundScheduler()
scheduler.start()

print("Connecting to the database...")
db_client = MongoClient(MONGO_URI)
db = db_client[DB_NAME]

print("Instantiating the Pyrogram client...")
pyrogram_client = Client(session_name=SESSION_NAME,
                         api_id=BOT_ID,
                         api_hash=BOT_HASH
                         )

print("Instantiating the bot...")
bot = Bot(name=BOT_NAME,
          bot_client=pyrogram_client,
          database=db,
          scheduler=scheduler
          )

bot.load()
bot.run()

