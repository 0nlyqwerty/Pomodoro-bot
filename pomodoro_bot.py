import os
import platform

# Get token from ./token.txt
CURRENT_DIR_PATH = os.path.dirname(__file__)
if CURRENT_DIR_PATH == "":
    CURRENT_DIR_PATH = "."
if platform.system() == "Linux":
    CURRENT_DIR_PATH = CURRENT_DIR_PATH + "/"
elif platform.system() == "Windows":
    CURRENT_DIR_PATH = CURRENT_DIR_PATH + "\\"
t = open(CURRENT_DIR_PATH + "token.txt", "r", encoding="utf-8")
TOKEN = t.read().split()[0]
