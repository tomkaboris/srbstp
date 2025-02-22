from srbstp.classifiers.sr_naive_bayes import SrNaiveBayesClassifier

def main():
    # Kreiramo "praznu" instancu
    classifier = SrNaiveBayesClassifier()

    # Učitavamo parametre iz već istreniranog modela
    classifier.load_model("nb_model.json")

    # Sada možemo klasifikovati nove tekstove
    test_texts = [
        "Ovo je super i baš sjajno!",
        "Sve je bilo užasno loše",
        "Nije ni dobro ni loše, ne znam"
    ]
    for text in test_texts:
        pred = classifier.classify(text)
        print(f"Tekst: '{text}' => Kategorija: {pred}")

if __name__ == "__main__":
    main()
