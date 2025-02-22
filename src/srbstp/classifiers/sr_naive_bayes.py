import math
import json
from collections import defaultdict, Counter
from srbstp.tokenizers.sr_tokenizer import SrTokenizer
from srbstp.data.sr_stopwords import is_stopword

class SrNaiveBayesClassifier:
    """
    Jednostavan Naive Bayes klasifikator za srpski, sa mogućnošću čuvanja/učitavanja modela.
    """

    def __init__(self, tokenizer=None, remove_stopwords=True, alpha=1.0):
        self.tokenizer = tokenizer if tokenizer else SrTokenizer()
        self.remove_stopwords = remove_stopwords
        self.alpha = alpha

        # Statistike za trening
        self.label_counts = Counter()
        self.word_counts = defaultdict(Counter)
        self.total_words_in_label = Counter()
        self.vocab = set()

    def _preprocess_text(self, text):
        tokens = self.tokenizer.tokenize_words(text)
        tokens = [t.lower() for t in tokens]
        if self.remove_stopwords:
            tokens = [t for t in tokens if not is_stopword(t)]
        return tokens

    def train(self, training_data):
        """
        training_data: lista (tekst, label) parova
        """
        for text, label in training_data:
            self.label_counts[label] += 1
            tokens = self._preprocess_text(text)
            for token in tokens:
                self.word_counts[label][token] += 1
                self.total_words_in_label[label] += 1
                self.vocab.add(token)

    def classify(self, text):
        total_labels = sum(self.label_counts.values())
        tokens = self._preprocess_text(text)

        best_label = None
        max_score = float("-inf")

        for label in self.label_counts:
            # log P(label)
            log_prior = math.log(self.label_counts[label] / total_labels)
            log_likelihood = 0.0

            for token in tokens:
                token_count = self.word_counts[label][token]
                total_words = self.total_words_in_label[label]
                # Laplace smoothing
                prob = (token_count + self.alpha) / (total_words + self.alpha * len(self.vocab))
                log_likelihood += math.log(prob)

            score = log_prior + log_likelihood

            if score > max_score:
                max_score = score
                best_label = label

        return best_label

    def save_model(self, filepath):
        """
        Čuva istrenirani model (statistike) u JSON formatu.
        filepath: putanja do fajla
        """
        # S obzirom na to da `Counter` i `defaultdict(Counter)` nisu direktno JSON-serializable,
        # moramo ih prevesti u obične diktove. Takođe, `vocab` je set (pretvorićemo ga u listu).
        model_data = {
            "label_counts": dict(self.label_counts),
            "word_counts": {
                label: dict(word_cnt) for label, word_cnt in self.word_counts.items()
            },
            "total_words_in_label": dict(self.total_words_in_label),
            "vocab": list(self.vocab),
            "remove_stopwords": self.remove_stopwords,
            "alpha": self.alpha
        }

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(model_data, f, ensure_ascii=False, indent=2)

    def load_model(self, filepath):
        """
        Učitava model iz JSON fajla i popunjava interne strukture.
        filepath: putanja do JSON fajla
        """
        with open(filepath, "r", encoding="utf-8") as f:
            model_data = json.load(f)

        self.label_counts = Counter(model_data["label_counts"])
        # word_counts zahteva re-kreiranje defaultdict(Counter)
        self.word_counts = defaultdict(Counter)
        for label, word_dict in model_data["word_counts"].items():
            self.word_counts[label] = Counter(word_dict)

        self.total_words_in_label = Counter(model_data["total_words_in_label"])
        self.vocab = set(model_data["vocab"])
        self.remove_stopwords = model_data["remove_stopwords"]
        self.alpha = model_data["alpha"]
