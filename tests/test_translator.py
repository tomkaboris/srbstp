# tests/test_translator.py

import pytest
from srbstp.translations.sr_translator import SrTranslator

@pytest.fixture
def translator():
    # Kreiramo translator sa ensure_latin=True
    # (pretpostavljamo da ćemo testirati i ćirilični ulaz)
    return SrTranslator(ensure_latin=True)

def test_translate_sr_to_en_basic(translator):
    """
    Testira prevod sa srpskog (latinica) na engleski.
    Očekujemo da rezultat nije prazan i da se razlikuje
    od originala.
    """
    sr_text = "Ovo je test."
    result = translator.translate_to_language(sr_text, dest_lang="en")

    assert isinstance(result, str)
    assert len(result.strip()) > 0
    assert result != sr_text  # Trebalo bi da bude različit od originala

def test_translate_sr_cyr_to_en_basic(translator):
    """
    Testira prevod sa srpskog (ćirilica) na engleski.
    Pošto smo postavili ensure_latin=True,
    ćirilica se prvo konvertuje u latinicu, pa se onda prevodi.
    """
    sr_cyr_text = "Ово је тест."
    result = translator.translate_to_language(sr_cyr_text, dest_lang="en")

    assert isinstance(result, str)
    assert len(result.strip()) > 0
    # Gugl ponekad vrati "This is a test." ali može varirati
    # Ovde proveravamo samo da rezultat nije identičan ćiriličnom ulazu
    assert result != sr_cyr_text  

def test_translate_en_to_sr_cyrillic(translator):
    """
    Testira prevod sa engleskog na srpski (ćirilica).
    """
    eng_text = "Hello, how are you?"
    # Koristimo parametar to_cyrillic=True
    result = translator.translate_from_language(eng_text, src_lang="en", to_cyrillic=True)

    assert isinstance(result, str)
    assert len(result.strip()) > 0
    # Ne možemo uvek garantovati tačnu rečenicu,
    # ali obično dobijemo nešto tipa "Здраво, како си?"
    # Proverićemo da li ima makar neki ćirilični karakter.
    assert any("А" <= ch <= "я" for ch in result.upper()), "Očekujemo bar neko ćirilično slovo"

def test_translate_en_to_sr_latin(translator):
    """
    Testira prevod sa engleskog na srpski (latinica).
    """
    eng_text = "I love programming."
    # to_cyrillic=False (default), znači da ćemo konvertovati na latinicu
    result = translator.translate_from_language(eng_text, src_lang="en", to_cyrillic=False)

    assert isinstance(result, str)
    assert len(result.strip()) > 0
    # Proverićemo da li je rezultat verovatno latinica (nema ćiriličnih slova).
    cyrillic_chars = [ch for ch in result if "А" <= ch <= "я"]
    assert len(cyrillic_chars) == 0, f"Rezultat sadrži ćirilične karaktere: {cyrillic_chars}"
    assert "programiranje" in result.lower() or "programisanje" in result.lower() \
        or "program" in result.lower(), "Očekujemo da se u prevodu pojavi reč 'programiranje' ili slično"

def test_translate_fr_to_sr(translator):
    """
    Testira prevod sa francuskog na srpski, na latinici.
    """
    fr_text = "Bonjour, comment allez-vous?"
    result = translator.translate_from_language(fr_text, src_lang="fr", to_cyrillic=False)
    
    assert isinstance(result, str)
    assert len(result.strip()) > 0
    # Često Google Translate vrati nešto poput "Zdravo, kako ste?"
    # Ovde nećemo strogo porediti, ali proveravamo da nije ostalo na francuskom
    assert "bonjour" not in result.lower(), "Ne bi trebalo da ostane 'bonjour' u prevodu"
    # Proveravamo da li su u pitanju isključivo latinična slova
    cyr_chars = [ch for ch in result if "А" <= ch <= "я"]
    assert not cyr_chars, f"Očekujemo latinicu, a našli smo ćirilične karaktere: {cyr_chars}"
