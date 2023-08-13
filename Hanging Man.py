###########Nada##########
import emoji
def draw_hangman(chances):
      if chances == 6:
          print("________ ")
          print("| | ")
          print("| ")
          print("| ")
          print("| ")
          print("| ")
      elif chances == 5:
          print("________ ")
          print("| | ")
          print("| 0 ")
          print("| ")
          print("| ")
          print("| ")
      elif chances == 4:
          print("________ ")
          print("|  | ")
          print("|  0 ")
          print("| / ")
          print("| ")
          print("| ")
      elif chances == 3:
          print("________ ")
          print("|  | ")
          print("|  0 ")
          print("| /| ")
          print("| ")
          print("| ")
      elif chances == 2:
          print("________ ")
          print("|  | ")
          print("|  0 ")
          print("| /|\ ")
          print("| ")
          print("| ")
      elif chances == 1:
          print("________ ")
          print("|  | ")
          print("|  0 ")
          print("| /|\ ")
          print("| / ")
          print("| ")
      elif chances == 0:
          print("________ ")
          print("|  | ")
          print("|  0 ")
          print("| /|\ ")
          print("| / \ ")
          print("| ")
          print("Game Over ")
print(" \t\t\t**********        Nada          **********")
print(" \t\t\t********** Hello in Hanging Manp **********")
import random
WORDS = ["python", "php", "nada", "abeer", "fatma",  "cpp"]
word = random.choice(WORDS)

length =len(word)
tries=6
b =list(length * "-")
print(*b)
while tries>=0 :
  guesse = input("please Enter Letter = " ).lower()
  if guesse in word:
    for position in range(length):
     if guesse==word[position]:
        b[position]=guesse         
    print(*b)
    if('-' not in b):
       print(f"you win ,the word is {word}",'\U0001F60D')
       break
  else:
    draw_hangman(tries)
    tries-= 1
    


    