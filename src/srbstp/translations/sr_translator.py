import googletrans
from googletrans import Translator
import asyncio

from srbstp.utils.sr_normalizer import cyr_to_lat, lat_to_cyr

class SrTranslator:
    """
    Klasa za prevođenje srpskog teksta koristeći googletrans klijent.
    """
    def __init__(self, ensure_latin=True):
        self.ensure_latin = ensure_latin
        self.translator = Translator()

    async def translate_to_language(self, text: str, dest_lang: str = "en") -> str:
        """
        Asinhroni prevod sa srpskog na 'dest_lang' jezik.
        """
        if self.ensure_latin:
            text = cyr_to_lat(text)

        result = await self.translator.translate(text, src="sr", dest=dest_lang)
        return result.text

    async def translate_from_language(self, text: str, src_lang: str = "en", to_cyrillic=False) -> str:
        """
        Asinhroni prevod sa 'src_lang' jezika na srpski.
        """
        result = await self.translator.translate(text, src=src_lang, dest="sr")
        translated_text = result.text

        if to_cyrillic:
            translated_text = lat_to_cyr(translated_text)
        else:
            translated_text = cyr_to_lat(translated_text)

        return translated_text
