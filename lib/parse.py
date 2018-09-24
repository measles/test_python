import re

# Symbols which can separate in line one word from anotherz
SEPARATORS = ",.;:?! "

def process_the_data(data, regular_expression):
    unique_words = []
    non_unique_words = []
    match_re = []
    if regular_expression:
        re_compiled = re.compile(regular_expression)
    else:
        re_compiled = None
    for line in data:
        if re_compiled:
            match = look_for_re(line, re_compiled)
            if match:
                match_re.append(line)

        unique_words, non_unique_words = find_unique(line, unique_words, non_unique_words)

    return unique_words, match_re

def look_for_re(line, regular_expression):
    return regular_expression.search(line)

def find_unique(line, unique_words, non_unique_words):
    words = []
    word = ''
    for symbol in line:
        if symbol not in SEPARATORS:
            word += symbol
        else:
            if len(word):
                words.append(word)
            word = ''

    if len(word):
        words.append(word)

    for word in words:
        if word not in unique_words:
            if word not in non_unique_words:
                unique_words.append(word)
        else:
            unique_words.remove(word)
            non_unique_words.append(word)

    return unique_words, non_unique_words
