import googletrans
from googletrans import Translator

from srbstp.utils.sr_normalizer import cyr_to_lat, lat_to_cyr

class SrTranslator:
    """
    Demonstraciona klasa za prevođenje srpskog teksta
    koristeći (nezvanični) googletrans klijent.
    """

    def __init__(self, ensure_latin=True):
        """
        :param ensure_latin: Da li da konvertujemo ćirilični ulaz u latinicu
                             pre slanja na prevod (googletrans ponekad
                             bolje prepoznaje latinični ulaz).
        """
        self.ensure_latin = ensure_latin
        self.translator = Translator()  # googletrans objekat

    def translate_to_language(self, text: str, dest_lang: str = "en") -> str:
        """
        Prevod sa srpskog na 'dest_lang' jezik (podrazumevano engleski).
        """
        # Opcionalno konvertujemo ćirilicu u latinicu
        if self.ensure_latin:
            text = cyr_to_lat(text)

        result = self.translator.translate(text, src="sr", dest=dest_lang)
        return result.text

    def translate_from_language(self, text: str, src_lang: str = "en", to_cyrillic=False) -> str:
        """
        Prevod sa 'src_lang' jezika na srpski.
        :param to_cyrillic: Da li rezultat želimo u ćirilici (ako je False, dobićemo latinicu).
        """
        result = self.translator.translate(text, src=src_lang, dest="sr")
        translated_text = result.text

        # Google Translate obično vraća srpski ispisan ćirilicom, 
        # ali ponekad i latiničnim pismom. Za svaki slučaj možemo 
        # detektovati ili konvertovati...
        #
        # Ako želimo obavezno ćirilicu, konvertovaćemo
        # iz latinice u ćirilicu. Ako želimo obavezno latinicu,
        # konvertovaćemo iz ćirilice u latinicu.

        if to_cyrillic:
            # Ukoliko je rezultat stigao u latinici, prelazimo ga u ćirilicu
            # (ili ako je stigao delimično mešano, svodimo na ćirilicu).
            translated_text = lat_to_cyr(translated_text)
        else:
            # U obrnutom slučaju, prelazimo sve u latinicu
            translated_text = cyr_to_lat(translated_text)

        return translated_text
