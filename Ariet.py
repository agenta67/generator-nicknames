import random
print("=== Nickname Generator ===") 
fantasy = ["Dragon", "Shadow", "Knight", "Wizard", "Blade", "Elf","Necromancy","Sorcery","Goblin","Dwarf","Overlord"]
cyber = ["Neo", "Cyber", "Byte", "Zero", "Glitch", "Core","Byte","Hacker","Vector","Binary","Exe","Node","Secure"]
common = ["Fast", "Cool", "Lucky", "Crazy", "Pro", "Mega","Sigma","Alpha","Beta","Sahur","Overvoltage","Nimble"]
while True:
   mode = int(input("Nickname type (1-meaningful, 2-random): ").strip())
   length = int(input("Nickname length: ").strip())
   digits = "0123456789"
   if mode == 1:
      theme = input("Theme (1-fantasy, 2-cyber, 3-common): ").strip()
       if theme == "1":
            words = fantasy
        elif theme == "2":
            words = cyber
        else:
            words = common
        nickname = ""
      while True:
         word = random.choice(words)
         if len(nickname) + len(word) > length - 1:  
                break
            nickname += word
       nickname += random.choice(digits)
      while len(nickname) < length:
            nickname += random.choice(digits)
   elif mode == 2:
      letters = "abcdefghijklmnopqrstuvwxyz"
      letters_and_digits = letters + digits
      nickname = ""
      nickname += random.choice(digits)
      while len(nickname) < length:
            nickname += random.choice(letters_and_digits)
      nickname = ''.join(random.sample(nickname, len(nickname)))

