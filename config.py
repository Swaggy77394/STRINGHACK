7# TEAM DAXX ALL COPYRIGHT ©️
from pyrogram import filters
import os

class Config:
    API_ID = "22351692"
    API_HASH = "f4871ddfefa0b6c25047f29e573e0a0d"
    #TOKEN = "6521122303:AAGCO3XMjcA0SN5NAi1M0NpmbmMxEtwwYbg"
    TOKEN = os.environ.get("TOKEN", "8078339956:AAHSYifb0IqGm3v8eMI44v-5EqgF0I6IT2M")
    MONGO_URL = "mongodb+srv://SpicyxMusicBot:SpicyxMusicBot@spicyxmusicbot.sghwtvp.mongodb.net/?appName=SpicyxMusicBot"
    START_PIC = "https://telegra.ph/file/a8ba8edd60489a54f2f84.jpg"
    SUDOERS = filters.user(["924235973","7603581459"])
