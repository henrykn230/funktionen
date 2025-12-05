def count_sentences(text):
    with open(text, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)

count_sentences("datei.txt")
