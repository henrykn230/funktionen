def count_words(text):
    with open(text, 'r', encoding='utf-8') as file:
        content = file.read()

    words = content.split()

    return len(words)