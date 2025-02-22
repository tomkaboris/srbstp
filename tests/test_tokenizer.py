
import pytest
from srbstp.tokenizers.sr_tokenizer import SrTokenizer, tokenize_sentences, tokenize_words

@pytest.fixture
def tokenizer():
    return SrTokenizer()

@pytest.mark.parametrize("text, expected", [
    ("Ovo je prva rečenica. Ovo je druga! A treća?", ["Ovo je prva rečenica", "Ovo je druga", "A treća"]),
    ("Bez interpunkcije", ["Bez interpunkcije"]),
    ("Višestruki... znaci???", ["Višestruki", "znaci"]),
    ("", [])
])
def test_tokenize_sentences(tokenizer, text, expected):
    assert tokenizer.tokenize_sentences(text) == expected

@pytest.mark.parametrize("text, expected", [
    ("Ovo je test", ["Ovo", "je", "test"]),
    ("Rečenica, sa znakovima!", ["Rečenica", "sa", "znakovima"]),
    ("123 brojke i slova abc", ["123", "brojke", "i", "slova", "abc"]),
    ("", [])
])
def test_tokenize_words(tokenizer, text, expected):
    assert tokenizer.tokenize_words(text) == expected

@pytest.mark.parametrize("text, expected", [
    ("Ovo je test. Još jedan test!", ["Ovo je test", "Još jedan test"])
])
def test_tokenize_sentences_function(text, expected):
    assert tokenize_sentences(text) == expected

@pytest.mark.parametrize("text, expected", [
    ("Ovo je test", ["Ovo", "je", "test"])
])
def test_tokenize_words_function(text, expected):
    assert tokenize_words(text) == expected
