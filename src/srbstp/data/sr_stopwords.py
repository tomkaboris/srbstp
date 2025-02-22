# textblob_sr/data/sr_stopwords.py

# Za početak, neka bude jednostavna lista ili set

SR_STOPWORDS = {
    "i", "a", "ali", "da", "do", "ga", "hoće", "hoću", "hoćemo",
    "hoćete", "hoćeš", "hoćeju", "je", "ji", "li", "mi", "moj",
    "na", "ne", "nego", "ni", "o", "od", "po", "s", "se", "si", 
    "su", "ti", "to", "u", "vi", "za", "će", "ću", "ćeš", "ćemo", 
    "ćete", "ćeju", "što", "šta", "kako", "koji", "ko", "koja",
    "koga", "šta", "one", "oni", "ona", "ono", "on", "ja",
    # Ovde se mogu dodati još mnoge varijacije
}

def is_stopword(token: str) -> bool:
    """
    Proverava da li je data reč (token) u listi stop reči za srpski jezik.
    """
    # Najjednostavniji pristup:
    return token.lower() in SR_STOPWORDS

def get_stopwords() -> set[str]:
    """
    Vraća skup srpskih stop reči.
    """
    return SR_STOPWORDS
