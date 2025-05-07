import json
import random

with open('pytania.json', 'r', encoding = 'utf-8') as file:
    questions = json.load(file)

ilosc_pytan = 10
wybrane_pytania = random.sample(questions, ilosc_pytan)

punkty = 0

for q in wybrane_pytania:

    user_input = input(q["pytanie"] + ' ')
    if user_input.strip().lower() == q["odpowiedz"].lower():
        print('Dobrze!')
        punkty += 1

    else:
        print(f"Źle! Poprawna odpowiedź to: {q["odpowiedz"]}")

print(f"\nTwój wynik: {punkty} / {ilosc_pytan}")

