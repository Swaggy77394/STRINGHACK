# TEAM DAXX ALL COPYRIGHT ©️
from pyrogram import filters
import os

class Config:
    API_ID = "22351692"
    API_HASH = "f4871ddfefa0b6c25047f29e573e0a0d"
    #TOKEN = "6521122303:AAGCO3XMjcA0SN5NAi1M0NpmbmMxEtwwYbg"
    TOKEN = os.environ.get("TOKEN", )
    MONGO_URL = "mongodb+srv://spicystring:Nothing0000@string.rsr5s28.mongodb.net/?retryWrites=true&w=majority&appName=String"
    START_PIC = "https://telegra.ph/file/a8ba8edd60489a54f2f84.jpg"
    SUDOERS = filters.user(["8438947274","7603581459"])
