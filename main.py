import random


def random_answers_good():
    start = [
        "Dzień dobry,",
        "Cześć,",
        "Miło nam czytać tak pozytywne komentarze!",
        "Dziękujemy za poświęcony czas na wystawienie opinii!",
        "Bardzo nam miło czytać Twój komentarz",
        "Dziękujemy za pozostawienie opinii!",
        "Dziękujemy za Twoją opinię!",
        "Bardzo nam miło czytać takie komentarze!"
    ]

    random_start= random.choice(start)

    ending = [
        "staramy się, aby Klienci naszych stacji byli zadowoleni ze świadczonych przez nas usług. Cieszymy się, że to doceniasz. Pozdrawiamy serdecznie!",
        "Dziękujemy za tak miłe słowa!",
        "Twoja opinia motywuje nas do dalszej pracy!",
        "Dziękujemy i życzymy wspaniałego dnia!",
        "Życzymy wszystkiego dobrego!",
        "Zapraszamy ponownie!",
        "Do zobaczenia ponownie!",
        "Dziękujemy i życzymy wspaniałego dnia!",
        "Dziękujemy za ciepłe słowa. Codziennie staramy się, aby wizyty na naszych stacjach były jak najlepsze.  Cieszymy się, że nasi Klienci to dostrzegają. Życzymy wspaniałego dnia!"
    ]
    ending_random = random.choice(ending)
    print(f"{random_start} {ending_random}")





def random_answers_bad() -> None:
    start = [
        "Dzień dobry, dziękujemy za opinię",
        "Dziękujemy za opinię",
        "Dzień dobry, dziękujemy za wiadomość",
        "Dziękujemy za wiadomość",
        "Dziękujemy za pozostawienie opinii",
        "Dziękujemy za podzielenie się opinią",
        "Dziękujemy za przekazanie swojej opinii",
        "Dziękujemy za Twoją opinię",
        "Dziękujemy za opinię i poświęcony czas"


    ]

    start_random = random.choice(start)

    ending = [
    "z przykrością przyjmujemy informację, że Twoja wizyta na naszej stacji nie przebiegła zgodnie z oczekiwaniami. "
    "Twoje uwagi są dla nas ważne i stanowią istotny element w procesie doskonalenia obsługi. "
    "Przepraszamy za wszelkie niedogodności.",
    "Przepraszamy za niedogodności. ",
    "traktujemy ją jako ważny sygnał do dalszych usprawnień.",



    ]
    ending_random = random.choice(ending)
    print (f"{start_random} {ending_random}")

random_answers_bad()

random_answers_good()




