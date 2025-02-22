# tests/test_stopwords.py

import pytest
from srbstp.data.sr_stopwords import is_stopword

def test_is_stopword_basic():
    # Proveravamo neke reči za koje sigurno znamo da su stop reči
    assert is_stopword("i") is True
    assert is_stopword("ne") is True
    # Provera velikog slova (case-insensitive)
    assert is_stopword("Da") is True

def test_is_stopword_negative():
    # Reči za koje smo sigurni da NISU stop reči
    assert is_stopword("kompjuter") is False
    assert is_stopword("fantastično") is False
    # Možemo još reči koje su izvan spiska stop reči
