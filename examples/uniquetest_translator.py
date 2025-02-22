from srbstp.translations.sr_translator import SrTranslator

sr_text_cyr = "Ово је неки ћирилички пример."
sr_text_lat = "Ovo je neki latinički primer."

translator = SrTranslator(ensure_latin=True)

# 1) Prevod sa srpskog na engleski
print(translator.translate_to_language(sr_text_cyr, dest_lang="en"))
# -> "This is some Cyrillic example."

# 2) Prevod sa engleskog na srpski (ćirilica)
eng_text = "Hello, how are you today?"
translated_cyr = translator.translate_from_language(eng_text, src_lang="en", to_cyrillic=True)
print(translated_cyr)
# -> "Здраво, како си данас?"

# 3) Prevod sa francuskog na srpski (latinica)
fr_text = "Bonjour, comment allez-vous?"
translated_lat = translator.translate_from_language(fr_text, src_lang="fr", to_cyrillic=False)
print(translated_lat)
# -> "Zdravo, kako ste?"
