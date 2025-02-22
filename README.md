# Simplified Serbian Text Processing
[![Run Pytest](https://github.com/tomkaboris/srbstp/workflows/Run%20Pytest/badge.svg)](https://github.com/tomkaboris/srbstp/actions?query=workflow%3A%22Run+Pytest%22)

**srbstp** je biblioteka inspirisana [TextBlob‑om](https://textblob.readthedocs.io/en/dev/), prilagođena srpskom jeziku. Nudi osnovne funkcionalnosti za:

- :white_check_mark: Tokenizaciju (reči i rečenice)
- :white_check_mark: Rad sa stop rečima i osnovnim leksikonom
- :white_check_mark: Normalizaciju i konverziju ćirilica ↔ latinica 
- :white_check_mark: Analizu sentimenta (leksikon‑bazirani pristup)
- :white_check_mark: Klasifikaciju (Naive Bayes)
- :white_check_mark: Part‑of‑Speech (POS) tagovanje (sopstveni model uz NLTK ili integracija s drugim alatima)

Pruža jednostavan API za uranjanje u uobičajene zadatke obrade prirodnog jezika (NLP), kao što su označavanje dela govora, izdvajanje imenskih fraza, analiza osećanja, klasifikacija i još mnogo toga.

---

## Sadržaj

1. [Instalacija](#instalacija)  
2. [Tokenizacija](#tokenizacija)  
3. [Stop reči i leksikon](#stop-reči-i-leksikon)  
4. [Normalizacija](#normalizacija)  
5. [Analiza sentimenta](#analiza-sentimenta)  
6. [Klasifikacija (Naive Bayes)](#klasifikacija-naive-bayes)  
7. [POS Tagger](#pos-tagger-u-procesu)  
8. [Testovi](#testovi)  
9. [Doprinos i razvoj](#doprinos-i-razvoj) 

---

## Instalacija

Projekat koristi `pyproject.toml`, tako da možete instalirati paket (i sve zavisnosti) tako što ćete klonirati ovaj repo i pokrenuti:

```bash
pip install -e .
```

## Zavisnosti
- nltk
- regex
- pytest (za testove, opcionalno)


## Tokenizacija
Modul: srbstp/tokenizers/sr_tokenizer.py

```bash
from srbstp.tokenizers.sr_tokenizer import SrTokenizer

tokenizer = SrTokenizer()

text = "Ovo je prva rečenica. Druga rečenica?! Treća rečenica."
sentences = tokenizer.tokenize_sentences(text)
print(sentences)
# ["Ovo je prva rečenica", "Druga rečenica", "Treća rečenica"]

words = tokenizer.tokenize_words(sentences[0])
print(words)
# ["Ovo", "je", "prva", "rečenica"]
```

### Ključne tačke:
- Metod tokenize_sentences(text) deli tekst na rečenice po . ! ?.
- Metod tokenize_words(text) deli tekst na reči koristeći regex.


## Stop reči i leksikon
Folder: srbstp/data/

### sr_stopwords.py
- Sadrži skup (set) srpskih stop reči i metode:
- is_stopword(token: str) -> bool
- get_stopwords() -> set[str]

```bash
from srbstp.data.sr_stopwords import is_stopword

print(is_stopword("i"))         # True
print(is_stopword("kompjuter")) # False
```

### sr_lexicon.py
- Sadrži rečnike za različite potrebe, na primer:
- SENTIMENT_LEXICON (mapa reč → polaritet)
- get_sentiment_polarity(word: str) -> float (vraća -1 do +1, 0 ako je reč nepoznata)

```bash
from srbstp.data.sr_lexicon import get_sentiment_polarity

print(get_sentiment_polarity("dobar"))    # 1
print(get_sentiment_polarity("užasan"))   # -1
print(get_sentiment_polarity("kompjuter")) # 0 (nepoznato)
```


## Normalizacija

Modul: srbstp/utils/sr_normalizer.py

### Ključne funkcije:
- cyr_to_lat(text: str) -> str – ćirilica → latinica
- lat_to_cyr(text: str) -> str – latinica → ćirilica
- remove_diacritics(text: str) -> str – uklanja dijakritike (š, đ, ž, ć, č → s, d, z, c, c)
- normalize_text(text, to_lat=True, lowercase=True, strip_diacritics=False) -> str – omotač koji radi sve korake odjednom

```bash
from srbstp.utils.sr_normalizer import cyr_to_lat, lat_to_cyr, remove_diacritics

text_cyr = "Ово је пример ћириличног текста."
text_lat = cyr_to_lat(text_cyr)
print(text_lat)
# Ovo je primer ćiriličnog teksta.

back_to_cyr = lat_to_cyr(text_lat)
print(back_to_cyr)
# Ово је пример ћириличног текста.

no_diacritics = remove_diacritics(text_lat)
print(no_diacritics)
# Ovo je primer cirilicnog teksta.
```


## Analiza sentimenta
- Modul: srbstp/sentiments/sr_sentiment_analyzer.py

Primer:
```bash
from srbstp.sentiments.sr_sentiment_analyzer import SrSentimentAnalyzer

analyzer = SrSentimentAnalyzer()
score = analyzer.analyze("Ovo je odličan i sjajan dan!")
print(score)
# Pozitivan skor (npr. > 0)
```

## Klasifikacija (Naive Bayes)
- Modul: srbstp/classifiers/sr_naive_bayes.py
- Klasa SrNaiveBayesClassifier implementira osnovni Bag‑of‑Words pristup s Laplace smoothing‑om.

Primer:
```bash
from srbstp.classifiers.sr_naive_bayes import SrNaiveBayesClassifier

training_data = [
    ("Ovo je fantastično!", "pozitivno"),
    ("Užasno, grozno...", "negativno"),
    # ...
]

clf = SrNaiveBayesClassifier()
clf.train(training_data)

print(clf.classify("Ovo je odlično"))  # "pozitivno"
```
Snimanje/Učitavanje modela:
```bash
clf.save_model("nb_model.json")
# ...
new_clf = SrNaiveBayesClassifier()
new_clf.load_model("nb_model.json")
```

## POS Tagger (u procesu)
- Folder: srbstp/taggers/
- Sopstveni model (sr_tagger.py)
- Koristi NLTK i HMM (Hidden Markov Model):

```bash
from srbstp.taggers.sr_tagger import SrPosTagger

tagger = SrPosTagger()
# 1) Treniranje:  tagger.train(tagged_sentences)
# 2) Tagovanje
tokens = ["Ovo", "je", "test", "."]
print(tagger.tag(tokens))
# [("Ovo", "DET"), ("je", "AUX"), ("test", "NOUN"), (".", "PUNCT")]
```
- train_pos_tagger.py – skripta za treniranje (čuva .pkl model)
- use_pos_tagger.py – skripta za učitavanje i korišćenje modela

## Testovi
Svi testovi su u folderu tests/, npr:

* test_tokenizer.py
* test_stopwords.py
* test_lexicon.py
* test_normalizer.py
* test_sentiment.py
* test_naive_bayes.py
* test_tagger.py

Pokreću se komandom:
```bash
pytest tests
```


## Doprinos i razvoj
* Fork/Clone: Napravite fork ili klonirajte repo.
* Razvojne zavisnosti: Instalirajte pytest, nltk, googletrans itd.
* Izmena koda: Dodajte nove funkcionalnosti ili optimizacije.
* Testiranje: Obezbedite testove za svoju izmenu.
* Pull Request: Napravite PR s opisom izmena.

### Ideje za budućnost:

* Bogatiji srpski sentiment leksikon
* Naprednija obrada negacije i modaliteta
* Offline prevod (npr. MarianMT)
* Named Entity Recognition (NER) za srpski
* Konverzija ćirilice↔latinice zasnovana na zvaničnim standardima (velika/mala slova, digrafi, itd.)