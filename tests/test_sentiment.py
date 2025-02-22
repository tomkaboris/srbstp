import pytest
from srbstp.sentiments.sr_sentiment_analyzer import SrSentimentAnalyzer

@pytest.fixture
def analyzer():
    return SrSentimentAnalyzer()

def test_positive_sentiment(analyzer):
    text = "Ovo je zaista dobar i odličan dan!"
    score = analyzer.analyze(text)
    assert score > 0  # Ocekujemo da bude pozitivan

def test_negative_sentiment(analyzer):
    text = "Ovo je užasno loše i grozno."
    score = analyzer.analyze(text)
    assert score < 0  # Ocekujemo da bude negativan

def test_neutral_sentiment(analyzer):
    text = "Danas je ponedeljak."
    score = analyzer.analyze(text)
    assert score == 0  # Ili bar blizu 0
