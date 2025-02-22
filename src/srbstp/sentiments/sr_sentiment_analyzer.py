from srbstp.tokenizers.sr_tokenizer import SrTokenizer
from srbstp.data.sr_stopwords import is_stopword
from srbstp.data.sr_lexicon import get_sentiment_polarity

class SrSentimentAnalyzer:
    def __init__(self, tokenizer=None):
        if tokenizer is None:
            tokenizer = SrTokenizer()
        self.tokenizer = tokenizer

    def analyze(self, text: str) -> float:
        """
        Vraća sentiment skor (npr. prosečan polaritet)
        na osnovu leksikon-baziranog pristupa.
        - <0 znači negativno, 
        - >0 znači pozitivno,
        - =0 znači neutralno.
        """
        # 1) Tokenizacija rečenice
        tokens = self.tokenizer.tokenize_words(text)

        # 2) Filtriranje stop reči
        meaningful_tokens = [t for t in tokens if not is_stopword(t.lower())]

        # 3) Računamo polaritet iz sr_lexicon.py
        polarities = [get_sentiment_polarity(token) for token in meaningful_tokens]

        # 4) Prosečan polaritet
        if polarities:
            return sum(polarities) / len(polarities)
        else:
            return 0.0  # Nema reči koje bi imale sentiment
