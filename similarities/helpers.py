from nltk.tokenize import sent_tokenize

def lines(a, b):
    """Return lines in both a and b"""
    # lines_a = a.split("\n")
    # lines_b = b.split("\n")

    # common_lines = []
    # for line in lines_a:
    #     if line in lines_b:
    #         if line not in common_lines:
    #             common_lines.append(line)

    # return common_lines

    lines_a = set(a.split("\n"))
    lines_b = set(b.split("\n"))

    return list({line for line in lines_a if line in lines_b})

def sentences(a, b):
    """Return sentences in both a and b"""

    sentences_a = sent_tokenize(a)
    sentences_b = sent_tokenize(b)

    common_sentences = []

    for sentences in sentences_a:
        if sentences in sentences_b:
            if sentences not in common_sentences:
                common_sentences.append(sentences)

    return common_sentences


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    common_substrings = []
    substrings_a = []
    substrings_b = []

    for i in range(len(a) - (n - 1)):
        substring_a = a[i:n + i]
        substrings_a.append(substring_a)

    for j in range(len(b) - (n - 1)):
        substring_b = b[j:n + j]
        substrings_b.append(substring_b)

    for substring in substrings_a:
        if substring in substrings_b:
            if substring not in common_substrings:
                common_substrings.append(substring)

    return common_substrings