import random


def random_answers_good():
     """Generate unique responses for good reviews by combining predefined text fragments."""
    start = [
        "Dzień dobry, dziękujemy za Twoją opinię.",
        "Dziękujemy za Twoją opinię.",
        "Bardzo nam miło czytać takie słowa.",
        "Dziękujemy za miły komentarz.",
        "Dziękujemy za podzielenie się opinią.",
        "Dziękujemy za pozytywną opinię."
    ]

    random_start= random.choice(start)

    ending = [
        "Cieszymy się, że wizyta spełniła oczekiwania.",
        "Cieszymy się, że doświadczenie było pozytywne.",
        "Twoja opinia motywuje nas do dalszej pracy.",
        "Dokładamy wszelkich starań, aby każda wizyta była udana.",
        "Zapraszamy ponownie i życzymy miłego dnia!",
        "Pozdrawiamy serdecznie i życzymy wszystkiego dobrego!",
        "Cieszymy się, że nasza praca została doceniona."
    ]
    ending_random = random.choice(ending)
    print(f"{random_start} {ending_random}")





def random_answers_bad() -> None:
     """Generate unique responses for bad reviews by combining predefined text fragments."""
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

print("Negatywne")
random_answers_bad()
print("")
print("Pozytywne")
random_answers_good()



