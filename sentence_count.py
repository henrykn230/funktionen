import os

def count_sentences(text):
    os.system('cls')
    file = open(text, 'r', encoding='utf-8')
    content = file.read()
    print(content)
    
    sentences1 = content.strip().split(".")
    sentences1.pop()

    sentences2 = content.strip().split("!")
    sentences2.pop()

    sentences3 = content.strip().split("?")
    sentences3.pop()

    sentences = sentences1 + sentences2 + sentences3
    
    return len(sentences)

anzahl = count_sentences("datei.txt")
print(f"Anzahl der Sätze: {anzahl}")