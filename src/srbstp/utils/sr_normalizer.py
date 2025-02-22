import unicodedata
import re

# Zvanična srpska ćirilica: а б в г д ђ е ж з и ј к л љ м н њ о п р с т ћ у ф х ц ч џ ш
# Zvanična srpska latinica: a b v g d đ e ž z i j k l lj m n nj o p r s t ć u f h c č dž š

# Napomena: Da bi se obezbedilo ispravno mapiranje "lj" -> "љ", "nj" -> "њ" i "dž" -> "џ"
# i obrnuto, treba paziti na redosled zamena.

CIR2LAT_SINGLE = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D',
    'Ђ': 'Đ', 'Е': 'E', 'Ж': 'Ž', 'З': 'Z', 'И': 'I',
    'Ј': 'J', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
    'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
    'Ћ': 'Ć', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'C',
    'Ч': 'Č', 'Џ': 'Dž', 'Ш': 'Š', 'Љ': 'Lj', 'Њ': 'Nj',
    'Ђ': 'Dj',

    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
    'ђ': 'đ', 'е': 'e', 'ж': 'ž', 'з': 'z', 'и': 'i',
    'ј': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
    'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
    'ћ': 'ć', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c',
    'ч': 'č', 'џ': 'dž', 'ш': 'š', 'љ': 'lj', 'њ': 'nj'
}

# Obrnuto, za prelazak iz zvanične srpske latinice u ćirilicu
# Za digrafe treba posebno voditi računa.
LAT2CIR = {
    'lj': 'љ', 'Lj': 'Љ', 'LJ': 'Љ',
    'nj': 'њ', 'Nj': 'Њ', 'NJ': 'Њ',
    'dž': 'џ', 'Dž': 'Џ', 'DŽ': 'Џ', 'Đ': 'Ђ',
    'a': 'а',  'b': 'б',  'c': 'ц',  'č': 'ч',  'ć': 'ћ',
    'd': 'д',  'đ': 'ђ',  'e': 'е',  'f': 'ф',  'g': 'г',
    'h': 'х',  'i': 'и',  'j': 'ј',  'k': 'к',  'l': 'л',
    'm': 'м',  'n': 'н',  'o': 'о',  'p': 'п',  'r': 'р',
    's': 'с',  'š': 'ш',  't': 'т',  'u': 'у',  'v': 'в',
    'z': 'з',  'ž': 'ж'
}

def cyr_to_lat(text: str) -> str:
    """
    Konverzija srpske ćirilice u srpsku latinicu.
    U obzir uzima i slova tipa 'Џ' (Dž), 'Љ' (Lj), 'Њ' (Nj), 
    ali ovde treba imati na umu da su to jedni karakteri. 
    Dvocifrene sekvence 'lj', 'nj', 'dž' *ne* postoje u ćirilici
    kao dva karaktera nego kao jedan (Љ, Њ, Џ).

    Ako u tekstu zaista postoji jedan karakter 'Љ', 
    to se mapira u 'Lj' ili 'lj' u zavisnosti od velikog/malog slova.

    Ipak, većina srpskih fontova/rasporeda ih unosi kao poseban karakter.
    """
    # Prolazimo karakter po karakter:
    latinized = []
    for ch in text:
        if ch in CIR2LAT_SINGLE:
            latinized.append(CIR2LAT_SINGLE[ch])
        else:
            latinized.append(ch)
    return "".join(latinized)

def lat_to_cyr(text: str) -> str:
    """
    Konverzija srpske latinice u srpsku ćirilicu.
    Ovde moramo obratiti pažnju na digrafe "lj", "nj" i "dž"
    koji predstavljaju jedno ćirilično slovo.
    """
    # Najprije ćemo tretirati potencijalne digrafe ("dž", "lj", "nj"),
    # a zatim preostala slova. Da bismo to olakšali, preći ćemo
    # od najdužih mogućih sekvenci do kraćih (dž ima 2 karaktera, 
    # a i "nj", "lj" takođe).
    #
    # Jedan od načina je da se pokuša "ručno" iterirati kroz string,
    # ili da koristimo re.sub sa custom funkcijom.
    
    # Redosled: 'dž' -> 'џ', pa onda 'lj' -> 'љ', 'nj' -> 'њ', 
    # pa onda single slova. Pazimo na velika slova i sl.
    
    # Jednostavniji način je da uradimo više .replace() 
    # (ali to treba raditi pažljivo da se ne pokvari nešto).
    
    # Da bismo bili sigurni u slučajevima mešovitih slova (Dž, dŽ, DŽ...),
    # možemo probati da svedemo sve u lower, pa da pratimo originalni case,
    # ali to zna da bude kompleksno. Za demonstraciju:
    
    # 1) Regex pristup za digrafe:
    text = re.sub(r'DŽ', 'Џ', text)
    text = re.sub(r'dž', 'џ', text)
    text = re.sub(r'Dž', 'Џ', text)  # varijacije velikih/malih slova
    
    text = re.sub(r'LJ', 'Љ', text)
    text = re.sub(r'lj', 'љ', text)
    text = re.sub(r'Lj', 'Љ', text)  # i ovde varijacije
    
    text = re.sub(r'NJ', 'Њ', text)
    text = re.sub(r'nj', 'њ', text)
    text = re.sub(r'Nj', 'Њ', text)

    # 2) Sada prelazimo sva preostala slova
    # Najbolje proći karakter po karakter i mapirati:
    cyrillic = []
    for ch in text:
        # pokušavamo lower varijantu
        lower_ch = ch.lower()
        if lower_ch in LAT2CIR:
            # Ako je original bio veliko slovo, koristimo upper varijantu
            mapped = LAT2CIR[lower_ch]
            if ch.isupper():
                mapped = mapped.upper()
            cyrillic.append(mapped)
        else:
            # ne mapiramo
            cyrillic.append(ch)
    return "".join(cyrillic)

def remove_diacritics(text: str) -> str:
    """
    Uklanja sve dijakritike iz stringa (npr. š -> s, č -> c, ć -> c, đ -> d, ž -> z)
    Korisno u slučajevima kada želimo da uporedimo reči 'cokolada' i 'čokolada'.
    
    Upozorenje: gubi se razlika koja je potencijalno bitna
    (npr. 'đ' i 'd' više nisu isto).
    """
    # Jedan od načina: normalizujemo Unicode, a zatim uklonimo oznake za dijakritike
    normalized = unicodedata.normalize('NFD', text)
    # uklanjamo sve karaktere koji imaju "Mn" (mark, nonspacing)
    without_diacritics = "".join(ch for ch in normalized if unicodedata.category(ch) != 'Mn')
    return without_diacritics

def normalize_text(text: str, to_lat: bool = True, lowercase: bool = True, strip_diacritics: bool = False) -> str:
    """
    Centralna funkcija za normalizaciju:
    - Može da prebaci sve u latinicu (to_lat=True) ili u ćirilicu (to_lat=False).
    - lowercasing (ako je `lowercase=True`)
    - uklanjanje dijakritika (ako je `strip_diacritics=True`)

    Pomoćno rešenje kako ne bismo pisali sve konverzije "ručno" više puta.
    """
    # 1) Odlučujemo da li radimo cir->lat ili lat->cir
    if to_lat:
        text = cyr_to_lat(text)
    else:
        text = lat_to_cyr(text)

    # 2) lowercasing po želji
    if lowercase:
        text = text.lower()

    # 3) eventualno uklanjanje dijakritika
    if strip_diacritics:
        text = remove_diacritics(text)

    return text
