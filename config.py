from os import getenv, path

from dotenv import load_dotenv

if path.exists("config.env"):
    load_dotenv("config.env")


APP_ID = int(getenv("APP_ID"))
API_HASH = getenv("84feb2e86bc3fa3b0b9bc1e3a3428177")
STRING_SESSION = getenv("AgDNvmIAnccGbswiyo0Gu8Q9l8nVhVbFiKH4mQDwmlOquANcvVGrOGZ3yytJ_GANLHv1n3eNFn7_t1HpRxW7deug-SQVZQILJ7O9GNOd40ajw1MZNu1WbCzjrlFXiW360olrH0CtBiJ_Lqz7gg-VBg7RrHObw2nmjmL8nB7J_sYWqXk6nfv9LGr9iKoD7yt-UibYwxXcPKuMoK4j1smO4ti7GZzIPrjmB2jiAaKsCNmIgsxFSpLy1QnK5V_F-hNqK5M2THJ12spUbYLnqagwuYuH7kCLtHNRZJey0C2wYqegdkk9n3aEuR3IbBLybbOkaSxA_BShGgcFpO5dOT2Fl4C5c4IwTgAAAAFygVbTAA")
DELAY = int(getenv("DELAY", 3))
if CHATS := getenv("-1002135275970", None):
    CHATS = CHATS.split(" ")
