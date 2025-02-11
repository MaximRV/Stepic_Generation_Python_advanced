import random

def generate_index():
   numbers = random.sample([i for i in range(0, 100)],2)
   letters = random.sample([i for i in range(65, 91)],4)
   return f'{chr(letters[0])}{chr(letters[1])}{numbers[0]}_{numbers[1]}{chr(letters[2])}{chr(letters[3])}'
