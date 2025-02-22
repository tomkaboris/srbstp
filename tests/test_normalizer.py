# tests/test_normalizer.py

import pytest
from srbstp.utils.sr_normalizer import (
    cyr_to_lat,
    lat_to_cyr,
    remove_diacritics,
    normalize_text
)

def test_cyr_to_lat_basic():
    text_cyr = "Ово је неки ћирилични текст Људи."
    expected_lat = "Ovo je neki ćirilični tekst Ljudi."
    assert cyr_to_lat(text_cyr) == expected_lat

def test_cyr_to_lat_special_characters():
    # Testiraćemo i karaktere poput Џ, Њ, Љ
    text_cyr = "Џем, Његош, Љиљана"
    expected_lat = "Džem, Njegoš, Ljiljana"
    assert cyr_to_lat(text_cyr) == expected_lat

def test_lat_to_cyr_basic():
    text_lat = "Ovo je neki ćirilični tekst Ljudi."
    # Ovde treba obratiti pažnju na digraf "Lj" -> "Љ"
    expected_cyr = "Ово је неки ћирилични текст Људи."
    assert lat_to_cyr(text_lat) == expected_cyr

def test_lat_to_cyr_digraphs():
    # Testiraćemo "dž", "lj", "nj" (uključujući velika slova)
    text_lat = "Džem, NJegoš, ljiljana"
    # Rezultat: "Џем, Његош, љиљана"
    expected_cyr = "Џем, Његош, љиљана"
    assert lat_to_cyr(text_lat) == expected_cyr

def test_remove_diacritics():
    text = "Šđćčž Ćirilica Đavo žurka"
    # Uklanja sve dijakritike: Š->S, đ->d, ć->c, č->c, ž->z...
    # Rezultat: "Sdccz Cirilica Djavo zurka"
    expected = "Sdccz Cirilica Djavo zurka"
    assert remove_diacritics(text) == expected

def test_normalize_text_to_lat_lower_strip():
    text_cyr = "Ово ЈЕ ТЕСТ са ЋИРИЛИЦОМ i latinicom"
    # Koristimo normalize_text da odmah:
    # 1) prebacimo sve na latinicu
    # 2) spustimo sva slova u mala (lowercase)
    # 3) uklonimo dijakritike
    # Očekujemo "ovo je test sa cirilicom i latinicom"
    expected = "ovo je test sa cirilicom i latinicom"
    result = normalize_text(
        text_cyr,
        to_lat=True,
        lowercase=True,
        strip_diacritics=True
    )
    assert result == expected

def test_normalize_text_to_cyr_no_lower_no_strip():
    # Prebacujemo latinicu u ćirilicu, ne diramo velika slova
    # ni dijakritike
    text_lat = "Ovo JE Test Sa Latinicom i Ćirilicom"
    # Nakon lat->cyr
    # "Ovo" -> "Ово"
    # "JE" -> "ЈЕ"
    # "Test" -> "Тест"
    # "Sa" -> "Са"
    # "Latinicom" -> "Латиницом"
    # "i" -> "и"
    # "Ćirilicom" -> "Ћирилицом"
    expected = "Ово ЈЕ Тест Са Латиницом и Ћирилицом"
    result = normalize_text(
        text_lat,
        to_lat=False,     # Znači lat->cyr
        lowercase=False,  # Zadržavamo veličinu slova
        strip_diacritics=False
    )
    assert result == expected
