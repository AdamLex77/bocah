import os

DEVS = [
    2033248262,
]

API_ID = int(os.getenv("API_ID", "20041941"))

API_HASH = os.getenv("API_HASH", "050e7be583eeb13d8f52c8e7cf8740e9")

BOT_TOKEN = os.getenv("BOT_TOKEN", "6727312932:AAGYOHo_MOtZT4h0V42DF1_jXiDg9RkZpGU")

OWNER_ID = int(os.getenv("OWNER_ID", "2033248262"))

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002079896647"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1001473548283").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "550"))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

COMMAND = os.getenv("COMMAND", ".")
PREFIX = COMMAND.split()

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
    "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",
).split()

MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://vewonon211:vewonon211@joysoy.kokbtub.mongodb.net/?retryWrites=true&w=majority",
)


