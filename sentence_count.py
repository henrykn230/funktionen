def count_sentences(text):
    with open(text, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
    
    sentences = content.strip().split(".")
    sentences = [s for s in sentences if s.strip()]
    
    return len(sentences)

anzahl = count_sentences("datei.txt")
print(f"Anzahl der Sätze: {anzahl}")