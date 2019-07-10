from json import loads
from random import shuffle

# Class for coloring the text
class TextColors:
    W = '\033[0m'
    R = '\033[31m'
    G = '\033[32m'

# Open the json file (kana.json)
json_file = open('data/kana.json')
data_kana = loads(json_file.read())
# now get every kana set in dictionaries
basic = data_kana['kana']['basic']
voiced = data_kana['kana']['voiced']
combo = data_kana['kana']['combo']
mixed = []
for all_sets in data_kana.get('kana').values():
    for all_kana in all_sets:
        mixed.append(all_kana)

# Make some variables
kana_quiz = []
score = total_quiz = 0

# Function to choose Kana Type (Basic, Voiced, Combo, or Mixed)
def kana_type():
    input_type = input('Please choose the kana type between Basic, Voiced, Combo, or Mixed: [B|V|C|M]> ')
    if input_type.lower() == 'b':
        return basic
    elif input_type.lower() == 'v':
        return voiced
    elif input_type.lower() == 'c':
        return combo
    elif input_type.lower() == 'm':
        return mixed

def kana_list(kanaSet, kanaType):
    if kanaSet == 'hira':
        makeKanaList(kanaSet, kanaType)
    elif kanaSet == 'kata':
        makeKanaList(kanaSet, kanaType)
    elif kanaSet == 'mix':
        makeKanaList(kanaSet, kanaType)

def makeKanaList(kanaSet, kanaType):
    if kanaSet == 'mix':
        for kana in kanaType:
            hiraList = {
                'kana': kana['hira'],
                'romaji': kana['romaji']
            }
            kataList = {
                'kana': kana['kata'],
                'romaji': kana['romaji']
            }
            kana_quiz.extend([hiraList, kataList])
    else:
        for kana in kanaType:
            kanaList = {
                'kana': kana[kanaSet],
                'romaji': kana['romaji']
            }
            kana_quiz.append(kanaList)

# Make input for choose between Kana Set (Hiragana, Katakana, or Mixed)
# This is will print first in console
kanaSet = input("Please choose the kana set between Hiragana, Katakana, or Mixed: [H|K|M]> ")
if kanaSet.lower() == 'h':
    kana_set = 'hira'
    tipe = kana_type()
    kana_list(kana_set, tipe)
elif kanaSet.lower() == 'k':
    kana_set = 'kata'
    tipe = kana_type()
    kana_list(kana_set, tipe)
elif kanaSet.lower() == 'm':
    kana_set = 'mix'
    tipe = kana_type()
    kana_list(kana_set, tipe)

# now is the last, the question
# this will print all values from kana_quiz list
# before that, we must shuffle the list first
shuffle(kana_quiz)
print('=' * 50)
# and now use For Loops
for quiz in kana_quiz:
    print(f'What romaji for this kana? {quiz["kana"]}')
    answer = input('Answer> ')
    # Add 1 to total_quiz for every quiz answered
    total_quiz += 1

    # Get the romaji
    # Make all romaji become to list
    romaji_quiz = quiz['romaji']
    romaji_quiz = romaji_quiz if isinstance(romaji_quiz, list) else [romaji_quiz]
    romaji_quiz = ','.join(romaji_quiz) if romaji_quiz[0] else romaji_quiz
    # This variables is for identify what is set that used for quiz
    k_set = 'hiragana' if kana_set == 'hira' else 'katakana'
    k_set = 'mixed' if kana_set == 'mix' else k_set

    # Compare the answer and romaji_quiz
    # Make the exit option
    if answer == 'exit':
        print('=' * 50)
        print(f'Your total score is {TextColors.G}{score}{TextColors.W} from {TextColors.G}{total_quiz - 1}{TextColors.W} {k_set}')
        exit()
    if answer == '' or romaji_quiz.__contains__(answer) == False: 
        # Send back the wrong quiz to list to repeat   
        wrong = {
            "kana": quiz["kana"],
            "romaji": quiz['romaji']
        }
        kana_quiz.append(wrong)
        print(f'{TextColors.R}Wrong, the correct one is {romaji_quiz}{TextColors.W}')
        total_quiz -= 1
        score -= 1
    elif romaji_quiz.__contains__(answer):
        print(f'{TextColors.G}Correct!{TextColors.W}')
        score += 1

# Print this if all quiz has been answered
print('=' * 50)
print(f'Your total score is {TextColors.G}{score}{TextColors.W} from {TextColors.G}{total_quiz}{TextColors.W} {k_set}')
        
