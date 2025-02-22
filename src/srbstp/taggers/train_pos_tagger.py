#!/usr/bin/env python3
# train_pos_tagger.py

from srbstp.taggers.sr_tagger import SrPosTagger

def main():
    """
    Skripta za treniranje sopstvenog POS taggera.
    Koristi minimalni primer; u praksi morate imati
    mnogo više rečenica sa ispravnim tagovima.
    """

    # 1) Minimalni primer korpusa
    # Svaka rečenica je lista (token, tag) parova.
    # Tagove (DET, AUX, NOUN, VERB, ADJ...) ovde izmišljamo radi primera.
    tagged_corpus = [
        [("Ovo", "DET"), ("je", "AUX"), ("test", "NOUN"), (".", "PUNCT")],
        [("Ja", "PRON"), ("idem", "VERB"), ("kući", "ADV"), (".", "PUNCT")],
        [("Velika", "ADJ"), ("kuća", "NOUN"), ("je", "AUX"), ("lepa", "ADJ")],
        [("On", "PRON"), ("voli", "VERB"), ("duge", "ADJ"), ("šetnje", "NOUN")],
        # ... ovde dodajte još rečenica
        # Napomena: U realnoj primeni, umesto hardcodovanog tagged_corpus, 
        # učitaćete corpus iz fajla (npr. .tsv, .conllu, ili nešto slično) 
        # i konvertovati ga u (token, tag) format.
    ]

    # 2) Kreiramo tagger
    pos_tagger = SrPosTagger()

    # 3) Treniramo ga na našem korpusu
    pos_tagger.train(tagged_corpus)

    # 4) Čuvamo model
    model_path = "sr_pos_tagger.pkl"
    pos_tagger.save_model(model_path)
    print(f"Model je sačuvan u: {model_path}")

if __name__ == "__main__":
    main()
