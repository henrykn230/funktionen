import os

def count_sentences(text):
    os.system('clear')
    with open(text, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)

    sentences = 0

    for char in content:
        if char in [".", "?", "!"]:
            sentences += 1

    return sentences