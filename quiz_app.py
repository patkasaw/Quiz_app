import json
import random
from datetime import datetime


with open('pytania.json', 'r', encoding = 'utf-8') as file:
    questions = json.load(file)

ilosc_pytan = 10
wybrane_pytania = random.sample(questions, ilosc_pytan)

punkty = 0

imie = input('Podaj swoje imię').strip().lower()
czas = datetime.now()

for q in wybrane_pytania:

    user_input = input(q["pytanie"] + ' ')
    if user_input.strip().lower() == q["odpowiedz"].lower():
        print('Dobrze!')
        punkty += 1

    else:
        print(f"Źle! Poprawna odpowiedź to: {q["odpowiedz"]}")

wynik = {punkty} / {ilosc_pytan}

wiersz = f'{czas} | {imie} | {wynik} '

print(f"\nTwój wynik: {wynik}")

with open("wyniki.txt", "a", encoding="utf-8") as plik:
    plik.write(wiersz)

print("✅ Twój wynik został zapisany do pliku 'wyniki.txt'.")

