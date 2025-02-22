import re

class SrTokenizer:
    """
    Klasa za osnovnu tokenizaciju srpskog jezika.
    Omogućava podelu teksta na rečenice i reči.
    """

    # Regex za pronalaženje granice rečenica:
    # - Podela na tačku, uzvičnik, upitnik (i eventualne kombinacije)
    sentence_split_regex = re.compile(r'[.!?]+')

    # Regex za podelu rečenice na reči:
    # - U najjednostavnijoj varijanti: sve što nije slovo ili broj tretiramo kao znak za razdvajanje
    # - U obzir uzimamo i srpska slova sa dijakritičkim znacima
    word_split_regex = re.compile(r'[^a-zA-ZčČćĆžŽšŠđĐА-Яа-я0-9]+')

    def __init__(self, keep_empty: bool = False):
        """
        :param keep_empty: Da li da čuvamo prazne stringove nakon razdvajanja (uglavnom False).
        """
        self.keep_empty = keep_empty

    def tokenize_sentences(self, text: str) -> list[str]:
        """
        Podela teksta na rečenice na osnovu osnovnih znakova interpunkcije (., !, ?).
        """
        # Razdvajamo tekst na osnovu definisanog regexa
        raw_sentences = self.sentence_split_regex.split(text)
        # Uklanjamo vodeće i prateće praznine
        sentences = [s.strip() for s in raw_sentences]

        # Ako nije uključeno čuvanje praznih stringova, uklanjamo ih
        if not self.keep_empty:
            sentences = [s for s in sentences if s]

        return sentences

    def tokenize_words(self, text: str) -> list[str]:
        """
        Podela teksta (ili pojedinačne rečenice) na reči. 
        Koristi osnovni regex koji razdvaja po svemu što nije slovo/broj.
        """
        # Splitujemo na osnovu regexa
        raw_tokens = self.word_split_regex.split(text)
        tokens = [t.strip() for t in raw_tokens]

        if not self.keep_empty:
            tokens = [t for t in tokens if t]

        return tokens

# Ako želimo da ponudimo i funkcije van klase, možemo dodati i nešto poput:
def tokenize_sentences(text: str, keep_empty: bool = False) -> list[str]:
    tokenizer = SrTokenizer(keep_empty=keep_empty)
    return tokenizer.tokenize_sentences(text)

def tokenize_words(text: str, keep_empty: bool = False) -> list[str]:
    tokenizer = SrTokenizer(keep_empty=keep_empty)
    return tokenizer.tokenize_words(text)
