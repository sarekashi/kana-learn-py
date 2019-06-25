import json
import random

file_json = open('data/kana.json')
data = json.loads(file_json.read())

class bcolors:
    W = '\033[0m'; R = '\033[31m'; G = '\033[32m'

arr = []; score = hira_quiz = 0; kana = data['kana']

for x in kana:
    arr.append(x)

# randomize the arr
random.shuffle(arr)

# option to choose between hiragana or katakana
input_type = input(f"- Please choose between Hiragana or Katakana [H/K]? ")
if input_type == 'H' or input_type == 'h':
    i_type = 'hira'
elif input_type == 'K' or input_type == 'k':
    i_type = 'kata'

print('=' * 30)

for hira in arr:
    input_kana = input(f"Please tell me what is this? {hira[i_type]}\nYou Answer: ")
    hira_quiz += 1

    romaji = hira['romaji']
    romaji = romaji if isinstance(romaji, list) else [romaji]
    romaji = '/'.join(romaji) if romaji[0] else romaji
    # determine hiragana or katakana
    k_type = 'hiragana' if i_type == 'hira' else 'katakana'

    if input_kana == 'exit':
        print('=' * 30)
        print(f'- Your total score is {bcolors.G}{score}{bcolors.W} from {bcolors.G}{hira_quiz - 1}{bcolors.W} {k_type}')
        exit()
    elif input_kana in romaji:
        print(bcolors.G + 'You are right!' + bcolors.W)
        score += 1
    else:
        print(bcolors.R + f'You are wrong, the right is: {romaji}' + bcolors.W)

print(f'Your total score is {bcolors.G}{score}{bcolors.W} from {hira_quiz} {k_type}')
