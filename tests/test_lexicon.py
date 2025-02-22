# tests/test_lexicon.py

import pytest
from srbstp.data.sr_lexicon import get_sentiment_polarity

def test_sentiment_positive():
    # Provera pozitivnih reči
    # U recniku: "dobar": 1, "odličan": 1, itd.
    assert get_sentiment_polarity("dobar") == 1
    assert get_sentiment_polarity("ODLIČAN") == 1  # case-insensitive

def test_sentiment_negative():
    # Provera negativnih reči
    # U recniku: "loš": -1, "grozan": -1, ...
    assert get_sentiment_polarity("loš") == -1
    assert get_sentiment_polarity("GROZAN") == -1

def test_sentiment_unknown():
    # Reč koja nije u leksikonu treba da vrati 0.0
    assert get_sentiment_polarity("kompjuter") == 0.0
    assert get_sentiment_polarity("nestoNepoznato") == 0.0
