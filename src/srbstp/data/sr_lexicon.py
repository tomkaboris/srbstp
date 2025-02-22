# textblob_sr/data/sr_lexicon.py

# Recnik sa osnovnim ocenama sentimenta
# kljuc: rec (u donjem obliku), vrednost: polaritet
# gde je -1 negativno, 0 neutralno, +1 pozitivno
SENTIMENT_LEXICON = {
    "dobar": 1,
    "odličan": 1,
    "najbolji": 1,
    "sjajno": 1,
    "pozitivno": 1,
    "loš": -1,
    "užasan": -1,
    "užasno": -1,
    "grozan": -1,
    "grozno": -1,
    "negativno": -1,
    # itd...
    # Ovaj primer je naravno minimalan 
    # u praksi se kreira sveobuhvatniji leksikon (pozitivnih, negativnih, neutralnih reči, fraza, itd.), 
    # a vrednosti mogu biti i realni brojevi (na primer 0.5, -0.75 itd.).
}

def get_sentiment_polarity(word: str) -> float:
    """
    Vraća polaritet date reči (u rasponu -1 do +1),
    ili 0 ukoliko nije definisan u rečniku.
    """
    return SENTIMENT_LEXICON.get(word.lower(), 0.0)
