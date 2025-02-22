#!/usr/bin/env python3
# train_nb_model.py

from srbstp.classifiers.sr_naive_bayes import SrNaiveBayesClassifier

def main():
    # 1) Ovde možete ručno definisati dataset ili učitati iz fajla/CSV-a
    training_data = [
        ("Ovo je baš dobar film", "pozitivno"),
        ("Ovaj film je loš i dosadan", "negativno"),
        ("Sjajan nastup, odlična energija!", "pozitivno"),
        ("Katastrofa, nikada više neću doći", "negativno")
    ]

    # 2) Kreiramo klasifikator
    classifier = SrNaiveBayesClassifier(remove_stopwords=True, alpha=1.0)

    # 3) Treniramo
    classifier.train(training_data)

    # 4) Čuvamo model
    model_path = "nb_model.json"
    classifier.save_model(model_path)
    print(f"Model sačuvan u: {model_path}")

if __name__ == "__main__":
    main()
