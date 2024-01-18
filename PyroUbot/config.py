import os

DEVS = [
    1873668175,
]

API_ID = int(os.getenv("API_ID", "14920143"))

API_HASH = os.getenv("API_HASH", "5a316e55fb121d9b5e891b5ff07d4677")

BOT_TOKEN = os.getenv("BOT_TOKEN", "6571031558:AAFyjvrgD7JdyyJN8L5VTeKIgpYehnxN0VE")

OWNER_ID = int(os.getenv("OWNER_ID", "1873668175"))

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002103823552"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1001994121863").split()))

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


