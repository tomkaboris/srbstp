#!/usr/bin/env python3
# use_pos_tagger.py

from srbstp.taggers.sr_tagger import SrPosTagger

def main():
    # 1) Kreiramo praznu instancu taggera
    pos_tagger = SrPosTagger()

    # 2) Učitavamo model
    model_path = "sr_pos_tagger.pkl"
    pos_tagger.load_model(model_path)
    print(f"Model učitan iz: {model_path}")

    # 3) Tagujemo novu rečenicu
    sentence = "Ovo je nova rečenica za testiranje."
    # Moramo je pretvoriti u listu tokena
    tokens = sentence.split()  # ili koristite SrTokenizer ako želite
    tagged = pos_tagger.tag(tokens)

    print("Tagovi:")
    for word, tag in tagged:
        print(f"{word} -> {tag}")

if __name__ == "__main__":
    main()
