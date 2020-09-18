# Вывести последнюю букву в слове
word = 'Архангельск'
print(f"Последняя буква в слове 'Архангельск': '{word[-1]}'")
# ???


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(f"Количество букв 'а' в слове 'Архангельск': {word.lower().count('а')}")
# ???


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowel_letters = 'аеёиоуыэюя'

count = 0
for letter in word.lower():
    if letter in vowel_letters:
        count += 1
print(f"Количество гласных букв в слове 'Архангельск': {count}")
# ???


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(f"Количество слов в предложении: {len(sentence.split(' '))}\n")
# ???


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
word = None
for word in sentence.split(' '):
    print(f"Первая буква очередного слова: {word[0]}")
# ???


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
word_count_sent = len(sentence.split(' '))
letter_count_sent = len(sentence.replace(' ', ''))
print (f"\nУсредненная длина слова: {letter_count_sent / word_count_sent}")

# ???