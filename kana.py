import json, random

# Open kana.json file
jsonFile = open('data/new_kana.json')
dataKana = json.loads(jsonFile.read())

kana = []; mixed = []; score = hira_quiz = 0
# Random the list from dataKana
basic = dataKana['kana']['basic']
voiced = dataKana['kana']['voiced']
combo = dataKana['kana']['combo']

class bcolors:
    W = '\033[0m'; R = '\033[31m'; G = '\033[32m'

# Fungsi untuk memilih tipe kana (basic, voice, combo)
def tipeKana():
    tipeInput = input('- Please choose between Basic, Voiced, Combo, or Mixed [b/v/c/m]> ')
    if tipeInput == 'b':
        return basic
    elif tipeInput == 'v':
        return voiced
    elif tipeInput == 'c':
        return combo
    elif tipeInput == 'm':
        for b in basic:
            mixed.append(b)
        for v in voiced:
            mixed.append(v)
        for c in combo:
            mixed.append(c)
        return mixed

def kanaList(jenis, tipe):
    if jenis == 'hira':
        for x in tipe:
            hiraList = {
                'kana': x['hira'],
                'romaji': x['romaji']
            }
            kana.append(hiraList)
    elif jenis == 'kata':
        for x in tipe:
            kataList = {
                'kana': x['kata'],
                'romaji': x['romaji']
            }
            kana.append(kataList)
    elif jenis == 'mix':
        for x in tipe:
            hiraList = {
                'kana': x['hira'],
                'romaji': x['romaji']
            }
            kataList = {
                'kana': x['kata'],
                'romaji': x['romaji']
            }
            kana.append(hiraList)
            kana.append(kataList)

# Choose between Hiragana, Katakana, or Mixed
jenisInput = input('- Please choose between Hiragana, Katakana, or Mixed [h/k/m]> ')
if jenisInput.lower() == 'h':
    jenisKana = 'hira'
    tipe = tipeKana()
    kanaList(jenisKana, tipe)
elif jenisInput.lower() == 'k':
    jenisKana = 'kata'
    tipe = tipeKana()
    kanaList(jenisKana, tipe)
elif jenisInput.lower() == 'm':
    jenisKana = 'mix'
    tipe = tipeKana()
    kanaList(jenisKana, tipe)

random.shuffle(kana)
for x in kana:
    inputQuiz = input(f"- Please tell me what is this? {x['kana']}\nYou Answer> ")
    hira_quiz += 1

    romaji = x['romaji']
    romaji = romaji if isinstance(romaji, list) else [romaji]
    romaji = ','.join(romaji) if romaji[0] else romaji
    k_jenis = 'hiragana' if jenisKana == 'hira' else 'katakana'
    k_jenis = 'mixed' if jenisKana == 'mix' else k_jenis

    if inputQuiz == 'exit':
        print('=' * 50)
        print(f'- Your total score is {bcolors.G}{score}{bcolors.W} from {bcolors.G}{hira_quiz - 1}{bcolors.W} {k_jenis}')
        exit()
    if inputQuiz in romaji:
        print(f'{bcolors.G}You are right!{bcolors.W}')
        score += 1
    else:
        print(f'{bcolors.R}You are wrong, the right is: {romaji}{bcolors.W}')

print('=' * 50)
print(f'Your total score is {bcolors.G}{score}{bcolors.W} from {hira_quiz} {k_jenis}')
