from sentence_count import * 
from word_count import * 

anzahl_sätze = count_sentences("datei.txt")
print(f"Anzahl der Sätze: {anzahl_sätze}")

anzahl_wörter = count_words("datei.txt")
print(f"Anzahl der Wörter: {anzahl_wörter}")
