"""
Task 1. Напишите скрипт, который бы получал на вход фразу и переводил 
бы ее в азбуку Морзе в виде разделенных пробелам точек и тире.
например для сообщения:
	ПРЕВЕД
выводило бы:
	·––· ·–· ·–· · ·–– · –··
Буквы кириллицей, пробелами и препинанием пренебрегаем.

Task 2. Напишите скрипт, который бы выполнял обратное действие - получал 
на вход точки-тире, разделенные пробелами и переводил бы их в текст
Например для сообщения:
	·–– ·· –·– – ––– ·–· –··· ––– ·––– –·– –––
Выводило бы:
	В И К Т О Р Б О Й К О
Преобразовать старый словарь(буква-точки-тире) в новый(точки-тире-буквы).
"""

file_morze = open('azbuka_morze.txt','r')
azbuka_morze = file_morze.readlines()
file_morze.close()

morze_let = []
morze_sign = []

for item in azbuka_morze:
	morze_let.append(item.split()[0].strip())
	morze_sign.append(item.split()[1].strip())

"""Create dict with letters as keys"""
morze_to_sign = dict(list(zip(morze_let, morze_sign)))

"""Create dict with signs as keys"""
morze_to_let = dict(list(zip(morze_sign, morze_let)))

#Task 1
some_word = "ПРЕВЕД"
word_conv = ""
for char in some_word:
	word_conv += morze_to_sign[char]
print(word_conv)

#Task 2
some_sign = "·–– ·· –·– – ––– ·–· –··· ––– ·––– –·– –––"
some_sig_parsed = some_sign.split()
new_word = ""
for sign in some_sig_parsed:
	new_word += morze_to_let[sign] + " "
print(new_word)
