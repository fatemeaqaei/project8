import gtts
import os.path
words_bank = []
print('welcome to the Translator')  

def read_from_file():
    global words_bank
    f = 'translate.txt'
    if os.path.isfile(f):
        f = open(f,'r')
    else:
        print('there is not exist!!')
        exit(0)

    temp = f.read().split('\n')

    words_bank = []
    for i in range(0,len(temp),2):
        my_dict = {'en': temp[i], 'fa': temp[i+1]}
        words_bank.append(my_dict)
    f.close()
    
def show_menu():
    print('1 - Translate English to Persian')
    print('2 - Translate Persian to English') 
    print('3 - Add new word to database')
    print('4 - Exit') 

    
def translate_en_to_fa():
    user_text = input('Enter your English text: ')
    user_words = user_text.split(' ')
    output1 = ''
    for user_word in user_words:
        for word in words_bank:
            if user_word == word['en']:
                output1 = output1 + word['fa'] + ' '
                break
        else:
            
            output1 = output1 + user_word + ' '

    print(output1)
    #gtts.gTTS(output1, lang='ar', slow=False).save('voice\_fa_' + output1 + '.mp3')

def translate_fa_to_en():
    user_text = input('Enter your farsi text: ')
    user_words = user_text.split(' ')
    output2 = ''
    for user_word in user_words:
        for word in words_bank:
            if user_word == word['fa']:
                output2 = output2 + word['en'] + ' '
                break
        else:
            output2 = output2 + user_word + ' '

    print(output2)
    #gtts.gTTS(output2, lang='ar', slow=False).save('voice\_fa_' + output2 + '.mp3')

def add_new_word():
    f= open('translate.txt', 'a')
    f.write(input('Enter your english text: '))
    f.write('\n')
    f.write(input('Enter your farsi text: '))
    f.write('\n')
    f.close()
print('add word succesful')


while True:
    show_menu()
    choice = int(input('Enter your Choice: '))

    if choice == 1:
        translate_en_to_fa()
    elif choice == 2:
        translate_fa_to_en()
    elif choice == 3:
        add_new_word()
    elif choice == 4:
        exit(0)