import os

DEVS = [
    1948761604,
]

API_ID = int(os.getenv("API_ID", "14920143"))

API_HASH = os.getenv("API_HASH", "5a316e55fb121d9b5e891b5ff07d4677")

BOT_TOKEN = os.getenv("BOT_TOKEN", "6248764230:AAGl3J_1ViCxVcqhkBbRiwjMZppqdtXh1SU")

OWNER_ID = int(os.getenv("OWNER_ID", "1948761604"))

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1001914077416"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1001914077416").split()))

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

