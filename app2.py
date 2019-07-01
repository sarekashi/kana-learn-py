import json, random

class bcolors:
    W = '\033[0m'; R = '\033[31m'; G = '\033[32m'

# Get kana.json file
kana_json = open('data/kana.json')
kana_data = json.loads(kana_json.read())

# Get list from kana_data and random it
kana = kana_data['kana']
random.shuffle(kana)

# score and already answered quiz variable
score = kana_quiz = 0
# Choose option between Hiragana or Katakana
kana_input = input(f"> Choose between Hiragana or Katakana [h/k]? ")
if kana_input.lower() == 'h':
    kana_type = 'hira'
elif kana_input.lower() == 'k':
    kana_type = 'kata'
else:
    print('Wrong Input')
    exit()

print('=' * 50)

def randRomaji(i):
    romaji = kana_data['kana'][i]['romaji']
    romaji = romaji if isinstance(romaji, list) else [romaji]
    romaji = ','.join(romaji) if romaji[0] else romaji
    return romaji

def randLenKana(num = 0):
    return random.randint(num, len(kana_data['kana']) - 1)


# Print kana continuously
for x in kana:
    kana_name = 'hiragana' if kana_type == 'hira' else 'katakana'
    # Add 1 to kana_quiz for every kana has already answered
    kana_quiz += 1

    ans1 = x['romaji']
    ans1 = ans1 if isinstance(ans1, list) else [ans1]
    ans1 = ','.join(ans1) if ans1[0] else ans1

    ans2 = randRomaji(randLenKana())
    ans3 = randRomaji(randLenKana())
    for same in range(len(kana)):
        if ans2 == ans3:
            ans2 = randRomaji(randLenKana(1))
        if ans2 == ans1:
            ans2 = randRomaji(randLenKana(1))
        if ans3 == ans1:
            ans3 = randRomaji(randLenKana(1))
    
    answers = [ans1, ans2, ans3]

    random.shuffle(answers)

    kana_answer = input(f'What Romaji for this {kana_name}? {x[kana_type]} ({" / ".join(answers)})\nYour Answer:(1 / 2 / 3) ')
    if kana_answer == '1':
        if answers[0] == ans1:
            print(f'{bcolors.G}You are right!{bcolors.W}')
            score += 1
        else:
            print(f'{bcolors.R}You are wrong, the right is: {ans1}{bcolors.W}')
    elif kana_answer == '2':
        if answers[1] == ans1:
            print(f'{bcolors.G}You are right!{bcolors.W}')
            score += 1
        else:
            print(f'{bcolors.R}You are wrong, the right is: {ans1}{bcolors.W}')
    elif kana_answer == '3':
        if answers[2] == ans1:
            print(f'{bcolors.G}You are right!{bcolors.W}')
            score += 1
        else:
            print(f'{bcolors.R}You are wrong, the right is: {ans1}{bcolors.W}')
    elif kana_answer == 'exit':
        print('=' * 30)
        print(f'- Your total score is {bcolors.G}{score}{bcolors.W} from {bcolors.G}{kana_quiz - 1}{bcolors.W} {kana_name}')
        exit()
    else:
        print(f'{bcolors.R}You are wrong, the right is: {ans1}{bcolors.W}')

print('=' * 50)
print(f'- Your total score is {bcolors.G}{score}{bcolors.W} from {bcolors.G}{kana_quiz}{bcolors.W} {kana_name}')
