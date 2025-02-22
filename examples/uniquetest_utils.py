from srbstp.utils.sr_normalizer import cyr_to_lat, lat_to_cyr, remove_diacritics, normalize_text

text_cyr = "Ово је неки ћирилични текст људи."
lat = cyr_to_lat(text_cyr)
print(lat)
# "Ovo je neki ćirilični tekst Ljudi."

back_to_cyr = lat_to_cyr(lat)
print(back_to_cyr)
# "Ово је неки ћирилични текст Људи."

# Lowercase + uklanjanje dijakritika
normalized = normalize_text(text_cyr, to_lat=True, lowercase=True, strip_diacritics=True)
print(normalized)
# "ovo je neki cirilicni tekst ljudi."
