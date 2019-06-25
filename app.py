import json
import random

with open('data/kana.json') as f:
    data = json.load(f)

class bcolors:
    W = '\033[0m'
    R = '\033[31m'
    G = '\033[32m'

arr = []
kana = data['kana']
for x in kana:
    arr.append(x)

# randomize the arr
random.shuffle(arr)

for hira in arr:
    input_kana = input(f"Please tell me what is this? {hira['hira']}\nYou Answer: ")
    romaji = hira['romaji']

    romaji = romaji if isinstance(romaji, list) else [romaji]
    romaji = '/'.join(romaji) if romaji[0] else romaji

    if input_kana == 'exit':
        exit()
    elif input_kana in romaji:
        print(bcolors.G + 'You are right!' + bcolors.W)
    else:
        print(bcolors.R + f'You are wrong, the right is: {romaji}' + bcolors.W)
