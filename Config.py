import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "27418440"))
    API_HASH = os.environ.get("API_HASH", "0a08a360e0e9f41b9896f655c300d09d")
    BOT_TOKEN = os.environ.get("7804181072:AAGb_ttagnHmbHkRpdd3UenJHXjgd4Bwwpw", "")
    STRING_SESSION = os.environ.get("1BVtsOGQBu3qHNw-t7WPKbfJunDgDq0lFRN5Rkb7f8Peh4LhSwpYOrJLOTAINDQK_XIMKX4Np85NRUW81cV2JN0FcqF8jwclSTc1yl-2XbKGuo1Y20bkyR7Wddp022ZPLCExs4bL57QpITWP3IZP8gvKLg_wtM0BswBOohUVJppUV-p-a2oldgCIysKWBV06Fiq3xrXdFrH1yt72afvgajlrdoewkAw0uqvdkmXoP9briXeGDz2-jXt7qWve2aLPh-ANkPy_t5pnzrirU_QNbjm4RtV06n2sx8jQJB4r8eHCtfemB1DceNpEyK9cmmoZiHuPixpD3XONh-c-xlRuIyeXxaXNtQo8=", "")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BlueGacorMusikBot", "")
    SUPPORT = os.environ.get("SUPPORT", "azellotesti") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "azelloelvano") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("7531000711", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
