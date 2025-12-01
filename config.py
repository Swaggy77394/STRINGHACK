# TEAM DAXX ALL COPYRIGHT ©️
from pyrogram import filters
import os

class Config:
    API_ID = "22351692"
    API_HASH = "f4871ddfefa0b6c25047f29e573e0a0d"
    #TOKEN = "6521122303:AAGCO3XMjcA0SN5NAi1M0NpmbmMxEtwwYbg"
    TOKEN = os.environ.get("TOKEN", "8078339956:AAGW4jgT7dNRgHzZRryGVmBohMyiPoMvKks")
    MONGO_URL = "mongodb+srv://STRINGHACK:Nothing0000@cluster0.nbjdl3k.mongodb.net/?appName=Cluster0"
    START_PIC = "https://telegra.ph/file/a8ba8edd60489a54f2f84.jpg"
    SUDOERS = filters.user(["8438947274","7603581459"])
