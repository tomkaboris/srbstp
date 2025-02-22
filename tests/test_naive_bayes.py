# tests/test_naive_bayes.py

import pytest
from srbstp.classifiers.sr_naive_bayes import SrNaiveBayesClassifier

@pytest.fixture
def classifier():
    training_data = [
        ("Ovo je baš dobar film", "pozitivno"),
        ("Ovaj film je loš i dosadan", "negativno"),
        ("Dobar nastup, odlična energija", "pozitivno"),
        ("Katastrofalan koncert, sve je bilo loše", "negativno")
    ]
    clf = SrNaiveBayesClassifier(remove_stopwords=True, alpha=1.0)
    clf.train(training_data)
    return clf

def test_classify_positive(classifier):
    text = "Sjajna izvedba i dobar osećaj"
    predicted = classifier.classify(text)
    assert predicted == "pozitivno"

def test_classify_negative(classifier):
    text = "Užasno iskustvo, jako loše"
    predicted = classifier.classify(text)
    assert predicted == "negativno"

def test_classify_unknown_words(classifier):
    # Reči koje nisu baš česte u trening setu:
    text = "Proba sa novim i čudnim rečima"
    # Moglo bi da ispadne ili pozitivno ili negativno, 
    # ali svakako treba da se izvrši klasifikacija bez greške.
    predicted = classifier.classify(text)
    assert predicted in ["pozitivno", "negativno"]  # bar da je jedna od validnih klasa

def test_classify_mixed(classifier):
    # Pozitivne i negativne reči zajedno
    text = "Dobar početak, ali loš kraj"
    predicted = classifier.classify(text)
    # Rezultat može varirati u zavisnosti od toga kako su reči raspoređene
    # U praksi, proveravamo da se kod ne ruši i da dobijemo neku klasu
    assert predicted in ["pozitivno", "negativno"]
