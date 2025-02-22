from srbstp.tokenizers.sr_tokenizer import SrTokenizer

sample_text = "Ovo je prva rečenica. Da li je ovo druga rečenica?! Treća rečenica je ovde."

tokenizer = SrTokenizer()

# Tokenizacija na rečenice
sentences = tokenizer.tokenize_sentences(sample_text)
print(sentences)
# Očekivani rezultat:
# ["Ovo je prva rečenica", "Da li je ovo druga rečenica", "Treća rečenica je ovde"]

# Tokenizacija na reči (prva rečenica)
words = tokenizer.tokenize_words(sentences[0])
print(words)
# Očekivani rezultat:
# ["Ovo", "je", "prva", "rečenica"]
