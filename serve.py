#!/usr/bin/env python

# Runs the bot using python 2.7.x +

from sys import exit
from config.config import config
import lib.bot as bot

try:
    bot.Bot().run()
except KeyboardInterrupt:
    exit()
