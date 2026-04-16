import random
import string
print("=== Генератор никнеймов ===")
fantasy = ["Dragon", "Shadow", "Knight", "Wizard", "Blade", "Elf"]
cyber = ["Neo", "Cyber", "Byte", "Zero", "Glitch", "Core"]
common = ["Fast", "Cool", "Lucky", "Crazy", "Pro", "Mega"]
mode = int(input("Тип ника (1-осмысленный, 2-рандом): ").strip())
length = int(input("Длина ника: ").strip())
nickname = ""
if mode == 1:
    theme = input("Тема (1-фэнтези, 2-кибер, 3-обычный): ").strip()
    if theme == "1":
        words = fantasy
    elif theme == "2":
        words = cyber
    else:
        words = common
    while True:
        word = random.choice(words)
        if len(nickname) + len(word) > length:
            break
        nickname = nickname + word
elif mode == 2:
    letters = string.ascii_lowercase

    while len(nickname) < length:
        nickname = nickname + random.choice(letters)
