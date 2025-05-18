"""
import os

class Config:
    startmsg = (
        'The bot is up and running. These bots '
        'can store messages in custom chats, '
        'and users access them through the bot.'
    )
    forcemsg = (
        'To view messages shared by bots. '
        'Join first, then press the Try Again button.'
    )

    OWNER_ID = int(os.environ.get('OWNER_ID', ''))
    BOT_TOKEN = os.environ.get('BOT_TOKEN', '')
    DATABASE_ID = int(os.environ.get('DATABASE_ID', '0'))  # Berikan nilai default '0'
    MONGO_URL = os.environ.get('MONGO_URL', '')

    API_ID = 2040
    API_HASH = 'b18441a1ff607e10a989891a5462e627'
    BOT_ID = BOT_TOKEN.split(':', 1)[0]

Config = Config()
"""


import os


class Config:
    startmsg = (
        'The bot is up and running. These bots '
        'can store messages in custom chats, '
        'and users access them through the bot.'
    )
    forcemsg = (
        'To view messages shared by bots. '
        'Join first, then press the Try Again button.'
    )

    OWNER_ID = int(os.environ.get('OWNER_ID', '7763935232'))
    BOT_TOKEN = os.environ.get('BOT_TOKEN', '7552355284:AAHDEkyqrD_3HU_K9cyymYNGFY70Sm9Z8oU')
    DATABASE_ID = int(os.environ.get('DATABASE_ID', '-1002549094524'))
    MONGO_URL = os.environ.get('MONGO_URL', 'mongodb+srv://Linkdaget:Malik10_@linkdaget.cqwn8.mongodb.net/?retryWrites=true&w=majority&appName=Linkdaget')

    API_ID = 29057224
    API_HASH = 'da205c3d61724a1358a02f2f09305928'
    BOT_ID = BOT_TOKEN.split(':', 1)[0]


Config = Config()
