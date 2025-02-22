# textblob_sr/taggers/sr_tagger.py

import pickle
from nltk.tag import hmm

class SrPosTagger:
    """
    Sopstveni POS tagger za srpski jezik, zasnovan na NLTK HiddenMarkovModelTrainer.
    """

    def __init__(self):
        self.tagger = None

    def train(self, tagged_sentences):
        """
        Treniranje POS taggera.
        :param tagged_sentences: lista rečenica,
               svaka rečenica je lista (token, tag) parova.
               Primer:
               [
                 [("Ovo", "DET"), ("je", "AUX"), ("test", "NOUN")],
                 [("Idem", "VERB"), ("kući", "ADV"), ... ],
                 ...
               ]
        """
        # Koristimo HiddenMarkovModelTrainer iz nltk.tag.hmm
        trainer = hmm.HiddenMarkovModelTrainer()
        self.tagger = trainer.train_supervised(tagged_sentences)

    def tag(self, tokens):
        """
        Taguje listu tokena (stringova) i vraća listu (token, tag).
        :param tokens: npr. ["Ovo", "je", "test"]
        :return: npr. [("Ovo", "DET"), ("je", "AUX"), ("test", "NOUN")]
        """
        if not self.tagger:
            raise ValueError("Tagger nije treniran ili nije učitan model.")
        return self.tagger.tag(tokens)

    def save_model(self, filepath):
        """
        Serijalizuje i čuva model u fajl pomoću pickle.
        """
        if not self.tagger:
            raise ValueError("Nema treniranog modela za čuvanje.")
        with open(filepath, "wb") as f:
            pickle.dump(self.tagger, f)

    def load_model(self, filepath):
        """
        Učitava istrenirani model iz fajla pomoću pickle.
        """
        with open(filepath, "rb") as f:
            self.tagger = pickle.load(f)
