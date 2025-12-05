def count_sentences(text):
    with open(text, 'r', encoding='utf-8') as file:
        inhalt = file.read()
        print(inhalt)

count_sentences("datei.txt")